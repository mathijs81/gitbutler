#!/usr/bin/env python3

import json
from collections import defaultdict

# package-info.json has JSON info for all rust packages.
# the info object has name, path, category, summary, description

output_file = "rust-packages.md"

with open("package-info.json", "r") as f:
    data = json.load(f)

# Organize packages by category
packages_by_category = defaultdict(list)
for package in data['packages']:
    packages_by_category[package['category']].append(package)

# Sort categories by their order
categories_sorted = sorted(data['categories'], key=lambda x: x['order'])

import subprocess
import shlex

def analyze_cloc(directory_path: str):
    """
    Analyzes lines of code in a directory using cloc.

    Args:
        directory_path: The path to the directory to analyze.

    Returns:
        A dictionary containing:
        - code_lines: The number of lines of code (excluding comments/blanks)
        - kloc: Lines of code in thousands (K)
    """
    command = [
        "cloc",
        "--json",
        "--exclude-dir=tests,target",
        "--exclude-ext=json,css,yaml,scss,svg,html,csv,txt,xml,md",
        directory_path
    ]

    try:
        process = subprocess.run(
            command,
            capture_output=True,
            text=True,
            check=True
        )
        cloc_output = process.stdout.strip()

        # Parse JSON output
        cloc_data = json.loads(cloc_output)

        # Get the SUM.code value
        if 'SUM' in cloc_data and 'code' in cloc_data['SUM']:
            code_lines = cloc_data['SUM']['code']
            kloc = code_lines / 1000.0
            return {
                "code_lines": code_lines,
                "kloc": kloc
            }
        else:
            return {
                "code_lines": 0,
                "kloc": 0.0,
                "note": "No code found"
            }
    except subprocess.CalledProcessError as e:
        return {
            "error": f"cloc command failed: {e.stderr.strip()}",
            "code_lines": 0,
            "kloc": 0.0
        }
    except FileNotFoundError:
        return {
            "error": "cloc command not found. Ensure cloc is installed.",
            "code_lines": 0,
            "kloc": 0.0
        }
    except json.JSONDecodeError as e:
        return {
            "error": f"Failed to parse cloc output: {str(e)}",
            "code_lines": 0,
            "kloc": 0.0
        }

def analyze_git_dir_activity(directory_path: str):
    """
    Analyzes a directory's commit history for the last 30 days.

    Args:
        directory_path: The path to the directory within the repository
                        to analyze.

    Returns:
        A dictionary containing:
        - commit_count: The number of non-merge commits touching the directory
                        in the last 30 days.
        - most_common_committer: The name of the most frequent committer.
        - recent_commits_summary: A list of the first sentences of the 5 most
                                  recent non-merge commits touching the directory.
    """
    results = {}
    
    # --- 1. Get all relevant commit hashes for analysis (most time-consuming part) ---
    # We use a single, comprehensive `git log` command to fetch the data
    # to avoid repeating the directory, date, and merge filtering.
    # --since='30 days ago': Filters commits within the last 30 days.
    # --no-merges: Excludes merge commits.
    # --pretty=format:'%an|%s': Custom format: Author Name, then | separator, then Subject (first line of commit message).
    # --max-count=9999: Set a high limit to ensure we get all commits for the 30-day period.
    # --: Separator to ensure the following argument is treated as a path.
    command_str_all = f"git log --since='30 days ago' --no-merges --pretty=format:'%an|%s' --max-count=9999 -- {directory_path}"
    
    try:
        # shlex.split is used to safely split the command string into a list of arguments
        process = subprocess.run(
            shlex.split(command_str_all),
            capture_output=True,
            text=True,
            check=True
        )
        log_output = process.stdout.strip()
    except subprocess.CalledProcessError as e:
        return {
            "error": f"Git command failed: {e.stderr.strip()}",
            "command": command_str_all
        }
    except FileNotFoundError:
        return {"error": "Git command not found. Ensure Git is installed and in your PATH."}

    if not log_output:
        return {
            "commit_count": 0,
            "most_common_committer": "N/A",
            "recent_commits_summary": [],
            "note": "No non-merge commits found for the specified directory in the last 30 days."
        }

    # Split the output into individual commit lines
    commit_lines = log_output.split('\n')
    
    # The number of commits is simply the count of lines
    results['commit_count'] = len(commit_lines)
    
    # Separate authors and subjects for further processing
    authors = []
    subjects = []
    
    for line in commit_lines:
        # Split using the | separator
        parts = line.split('|', 1)
        if len(parts) == 2:
            authors.append(parts[0])
            subjects.append(parts[1])

    # --- 2. Find the most common committer ---
    if authors:
        from collections import Counter
        author_counts = Counter(authors)
        most_common_author = author_counts.most_common(1)[0][0]
        results['most_common_committer'] = most_common_author
    else:
        results['most_common_committer'] = "N/A"

    # --- 3. Get the first sentences of the 5 most recent commits ---
    # The `git log` output is already ordered from newest to oldest.
    recent_summaries = []
    for subject in subjects[:5]:
        # The 'subject' is the first line of the commit message.
        # We need to extract the first sentence.
        # Simple heuristic: find the first period, exclamation mark, or question mark.
        sentence_end_index = -1
        for char in ['.', '!', '?']:
            index = subject.find(char)
            if index != -1 and (sentence_end_index == -1 or index < sentence_end_index):
                sentence_end_index = index
        
        if sentence_end_index != -1:
            # Add 1 to include the punctuation mark and strip any leading/trailing whitespace
            first_sentence = subject[:sentence_end_index + 1].strip()
        else:
            # If no punctuation is found, the whole subject line is the "sentence"
            first_sentence = subject.strip()
        
        recent_summaries.append(first_sentence)
        
    results['recent_commits_summary'] = recent_summaries

    return results

for package in data['packages']:
    package['git_data'] = analyze_git_dir_activity(package['path'])
    package['cloc_data'] = analyze_cloc(package['path'])

with open(output_file, "w") as f:
    # Main title
    f.write("# GitButler Rust Packages\n\n")

    # Quick Reference section
    f.write("## Quick Reference\n\n")

    for category in categories_sorted:
        category_name = category['name']
        if category_name not in packages_by_category:
            continue

        f.write(f"### {category_name}\n")

        for package in packages_by_category[category_name]:
            # Create anchor link (lowercase, replace spaces with hyphens)
            anchor = package['name'].lower()

            # Get KLOC info if available
            kloc_str = ""
            if 'cloc_data' in package:
                cloc_data = package['cloc_data']
                if 'error' not in cloc_data:
                    kloc = cloc_data.get('kloc', 0.0)
                    if kloc > 0:
                        kloc_str = f" ({kloc:.1f}K LOC)"

            f.write(f"- [**{package['name']}**](#{anchor}) - {package['summary']}{kloc_str}\n")

        f.write("\n")

    # Separator
    f.write("---\n\n")

    # Detailed Descriptions section
    f.write("## Detailed Descriptions\n\n")

    for category in categories_sorted:
        category_name = category['name']
        if category_name not in packages_by_category:
            continue

        f.write(f"### {category_name}\n\n")

        for package in packages_by_category[category_name]:
            f.write(f"#### {package['name']}\n")
            f.write(f"{package['description']}\n\n")

            # Add lines of code data if available
            if 'cloc_data' in package:
                cloc_data = package['cloc_data']
                if 'error' in cloc_data:
                    f.write(f"**Lines of Code:** Error - {cloc_data['error']}\n\n")
                else:
                    code_lines = cloc_data.get('code_lines', 0)
                    kloc = cloc_data.get('kloc', 0.0)
                    if code_lines > 0:
                        f.write(f"**Lines of Code:** {code_lines:,} ({kloc:.1f}K)\n\n")
                    else:
                        f.write(f"**Lines of Code:** No code found\n\n")

            # Add git activity data if available
            if 'git_data' in package:
                git_data = package['git_data']

                # Check if there's an error
                if 'error' in git_data:
                    f.write(f"**Git Activity:** Error retrieving data - {git_data['error']}\n\n")
                else:
                    # Write commit count and most common committer
                    commit_count = git_data.get('commit_count', 0)
                    committer = git_data.get('most_common_committer', 'N/A')

                    if commit_count > 0:
                        f.write(f"**Recent Activity (last 30 days):** {commit_count} commits")
                        if committer != 'N/A':
                            f.write(f" (most active: {committer})")
                        f.write("\n\n")

                        # Add recent commits summary if available
                        recent_commits = git_data.get('recent_commits_summary', [])
                        if recent_commits:
                            f.write("**Recent changes:**\n")
                            for commit_summary in recent_commits:
                                f.write(f"- {commit_summary}\n")
                            f.write("\n")
                    else:
                        f.write(f"**Recent Activity (last 30 days):** No commits\n\n")

    # Separator
    f.write("---\n\n")

    # Architecture Notes section
    f.write("## Architecture Notes\n\n")
    f.write(f"{data['metadata']['architecture_notes']}\n\n")
    f.write(f"**Total packages: {data['metadata']['total_packages']}**\n")