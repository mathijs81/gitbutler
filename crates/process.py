import json
import os
from collections import defaultdict

def get_first_level_dir(file_path):
    """
    Extracts the first-level directory name from a file path.
    """
    # Remove leading './' if it exists, as cloc often adds it
    if file_path.startswith('./') and len(file_path) > 2:
        file_path = file_path[2:]

    normalized_path = os.path.normpath(file_path)
    parts = normalized_path.split(os.sep)
    
    # If there's only one part, it's a file in the root
    if len(parts) == 1:
        return '.'  # Represents the root directory

    # The first part is the first-level directory
    return parts[0]


def process_cloc_json(json_file_path="cloc_data.json"):
    """
    Loads cloc JSON data and calculates LOC totals per first-level directory.
    """
    try:
        with open(json_file_path, 'r') as f:
            data = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"Error loading or parsing JSON: {e}")
        return
    
    dir_totals = defaultdict(int)
    
    # --- FIX APPLIED HERE ---
    # Iterate through all top-level keys in the JSON
    for key, file_data in data.items():
        # Skip metadata keys like 'header', 'SUM', and any others that aren't file paths
        if key in ('header', 'SUM', 'total', 'files'):
            continue
        
        # The key is now assumed to be a file path
        file_path = key
        
        # Get the first-level directory name
        dir_name = get_first_level_dir(file_path)
        
        # The 'code' key holds the actual lines of source code
        loc_count = file_data.get('code', 0)
        
        # Aggregate the LOC
        dir_totals[dir_name] += loc_count
            
    # Sort and Print Logic (remains the same)
    # ----------------------------------------
    sorted_totals = sorted(dir_totals.items(), key=lambda item: item[1], reverse=True)
    
    print("\n--- LOC Totals Per First-Level Subdirectory ---")
    
    # Calculate the maximum width needed for the directory names for clean formatting
    max_dir_width = max(len(dir) for dir, loc in sorted_totals) if sorted_totals else 10
    
    # Header
    header = f"{'Directory':<{max_dir_width}} | {'Lines of Code (LOC)':>15}"
    print("-" * (len(header) + 2))
    print(header)
    print("-" * (len(header) + 2))

    # Data Rows
    for directory, total_loc in sorted_totals:
        print(f"{directory:<{max_dir_width}} | {total_loc:>15,}")
        
    print("-" * (len(header) + 2))
    
    # Print the grand total from the cloc summary, if available
    try:
        total_loc_summary = data['SUM']['code']
        total_files = data['header']['n_files']
        print(f"\nSummary: {total_files} files processed, Total LOC: {total_loc_summary:,}")
    except (KeyError, TypeError):
        pass # Ignore if summary data is missing

# Execute the script
if __name__ == "__main__":
    process_cloc_json("cloc_data.json")
