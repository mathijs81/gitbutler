# GitButler Rust Packages

## Quick Reference

### Core Infrastructure
- [**but-core**](#but-core) - Core algorithms and types for Git operations (5.5K LOC)
- [**but-error**](#but-error) - Error handling utilities (0.1K LOC)
- [**but-oxidize**](#but-oxidize) - Bridge between git2 (libgit2) and gix (gitoxide) (0.2K LOC)
- [**but-serde**](#but-serde) - Serialization utilities for Git types (0.3K LOC)

### Database & Storage
- [**but-db**](#but-db) - SQLite database layer with Diesel ORM (1.2K LOC)
- [**but-forge-storage**](#but-forge-storage) - Persistent storage for forge information (0.3K LOC)
- [**but-secret**](#but-secret) - Secrets management using keyring (0.3K LOC)

### Settings & Configuration
- [**but-settings**](#but-settings) - Application settings management with file watching (0.7K LOC)
- [**but-path**](#but-path) - Path handling utilities (0.1K LOC)

### Filesystem & I/O
- [**but-fs**](#but-fs) - Filesystem operations with TOML support (0.2K LOC)
- [**but-status**](#but-status) - Git status operations using gitoxide (0.2K LOC)

### Graph & Visualization
- [**but-graph**](#but-graph) - Git commit graphs as connected segments with graph operations (6.0K LOC)
- [**but-feedback**](#but-feedback) - Feedback collection system with diagnostic bundling (0.1K LOC)

### Hunk Management
- [**but-hunk-dependency**](#but-hunk-dependency) - Analyzes dependencies between code hunks (1.2K LOC)
- [**but-hunk-assignment**](#but-hunk-assignment) - Assigns hunks to branches and stacks (1.0K LOC)

### Workspace & Branch Operations
- [**but-workspace**](#but-workspace) - Core workspace management (8.0K LOC)
- [**but-worktrees**](#but-worktrees) - Git worktree management operations (0.5K LOC)

### Rebase & Cherry-Pick
- [**but-rebase**](#but-rebase) - Git rebase operations with Gerrit support (1.0K LOC)
- [**but-cherry-apply**](#but-cherry-apply) - Cherry-pick application logic (0.1K LOC)

### Metadata & Context
- [**but-meta**](#but-meta) - Metadata operations for Git entities (1.2K LOC)
- [**but-ctx**](#but-ctx) - Repository-specific context management (0.5K LOC)

### Operations Log
- [**but-oplog**](#but-oplog) - Undo/redo functionality through operation logging (0.1K LOC)

### AI Integration
- [**but-action**](#but-action) - AI-powered actions system with LLM integration (2.4K LOC)
- [**but-claude**](#but-claude) - Claude AI integration with MCP support (4.7K LOC)
- [**but-cursor**](#but-cursor) - Cursor editor integration (0.5K LOC)
- [**but-bot**](#but-bot) - Bot functionality for automated operations (0.8K LOC)
- [**but-tools**](#but-tools) - Collection of AI-powered tools (2.0K LOC)

### Rules & Automation
- [**but-rules**](#but-rules) - Rule-based automation system with regex support (0.5K LOC)

### Forge Integration
- [**but-forge**](#but-forge) - Generic forge abstraction layer (0.5K LOC)
- [**but-github**](#but-github) - GitHub API integration (1.0K LOC)
- [**but-gerrit**](#but-gerrit) - Gerrit code review platform integration (0.8K LOC)

### API & Server
- [**but-api**](#but-api) - Main API layer with modular functionality (3.6K LOC)
- [**but-api-macros**](#but-api-macros) - Procedural macros for API code generation (0.4K LOC)
- [**but-server**](#but-server) - HTTP server with WebSocket support (0.8K LOC)

### CLI Tools
- [**but**](#but) - Main CLI binary with rich TUI support (11.1K LOC)
- [**but-clap**](#but-clap) - Alternative CLI interface using Clap (0.2K LOC)
- [**gitbutler-cli**](#gitbutler-cli) - Legacy CLI tool (0.6K LOC)

### Testing & Debugging
- [**but-testsupport**](#but-testsupport) - Testing utilities with snapshot testing (1.3K LOC)
- [**but-testing**](#but-testing) - Binary for testing scenarios (1.7K LOC)
- [**but-debugging**](#but-debugging) - Debugging utilities (0.1K LOC)
- [**gitbutler-testsupport**](#gitbutler-testsupport) - Legacy test support (1.1K LOC)

### Legacy GitButler Crates
- [**gitbutler-tauri**](#gitbutler-tauri) - Main Tauri desktop application (2.1K LOC)
- [**gitbutler-watcher**](#gitbutler-watcher) - File monitoring and change detection (0.3K LOC)
- [**gitbutler-filemonitor**](#gitbutler-filemonitor) - Low-level file monitoring with debouncing (1.0K LOC)
- [**gitbutler-workspace**](#gitbutler-workspace) - Legacy workspace operations (0.3K LOC)
- [**gitbutler-stack**](#gitbutler-stack) - Stack (branch series) management (2.2K LOC)
- [**gitbutler-branch**](#gitbutler-branch) - Branch operations and management (0.2K LOC)
- [**gitbutler-branch-actions**](#gitbutler-branch-actions) - High-level branch operations (6.2K LOC)
- [**gitbutler-repo**](#gitbutler-repo) - Repository operations (1.4K LOC)
- [**gitbutler-repo-actions**](#gitbutler-repo-actions) - High-level repository actions (0.5K LOC)
- [**gitbutler-project**](#gitbutler-project) - Project management and configuration (1.1K LOC)
- [**gitbutler-operating-modes**](#gitbutler-operating-modes) - Different operating modes for the application (0.2K LOC)
- [**gitbutler-edit-mode**](#gitbutler-edit-mode) - Edit mode functionality (0.4K LOC)
- [**gitbutler-oplog**](#gitbutler-oplog) - Legacy oplog implementation (1.6K LOC)
- [**gitbutler-sync**](#gitbutler-sync) - Synchronization operations for remote repositories (0.4K LOC)
- [**gitbutler-git**](#gitbutler-git) - Git operations wrapper with platform-specific features (1.2K LOC)
- [**gitbutler-commit**](#gitbutler-commit) - Commit operations (0.2K LOC)
- [**gitbutler-cherry-pick**](#gitbutler-cherry-pick) - Cherry-pick operations (0.2K LOC)
- [**gitbutler-diff**](#gitbutler-diff) - Diff operations and hunk management (1.2K LOC)
- [**gitbutler-hunk-dependency**](#gitbutler-hunk-dependency) - Legacy hunk dependency analysis (2.4K LOC)
- [**gitbutler-reference**](#gitbutler-reference) - Git reference management (0.4K LOC)
- [**gitbutler-url**](#gitbutler-url) - URL parsing and validation for Git remotes (0.4K LOC)
- [**gitbutler-user**](#gitbutler-user) - User management and authentication (0.2K LOC)
- [**gitbutler-time**](#gitbutler-time) - Time utilities (0.0K LOC)

---

## Detailed Descriptions

### Core Infrastructure

#### but-core
A fundamental leaf-crate containing core algorithms and types for Git operations. This package serves as a building block for the entire GitButler ecosystem, providing essential data structures and algorithms without external dependencies. It includes features for testing and TypeScript export, making it suitable for both backend and frontend integration.

**Lines of Code:** 5,489 (5.5K)

**Recent Activity (last 30 days):** 24 commits (most active: Sebastian Thiel)

**Recent changes:**
- refactor
- Fix spelling and grammatical errors across repository
- Rename the macro to the absolute epic.
- Make `but_api::legacy::diff::commit_details()` non-legacy.
- Update to `gix@main` to see URL related fixes (#11419)

#### but-error
A minimal error handling utilities crate that provides common error types and handling patterns. With only anyhow as a dependency, it keeps error handling lightweight while maintaining consistency across the codebase.

**Lines of Code:** 125 (0.1K)

**Recent Activity (last 30 days):** 3 commits (most active: copilot-swe-agent[bot])

**Recent changes:**
- Fix spelling and grammatical errors across repository
- Handle network errors when fetching GitHub user
- Migrate `gitbutler-error` into the `but` world.

#### but-oxidize
Provides conversion utilities between git2 (libgit2 bindings) and gix (gitoxide) libraries. This crate is crucial for the ongoing migration from the legacy git2 implementation to the modern Rust-native gitoxide library, allowing both systems to coexist during the transition.

**Lines of Code:** 240 (0.2K)

**Recent Activity (last 30 days):** 3 commits (most active: Sebastian Thiel)

**Recent changes:**
- Create a mixed-mode non-legacy apply.
- Fold `gitbutler-command-context` into `but-ctx`.
- Rename `gitbutler-oxidize` to `but-oxidize`.

#### but-serde
Serialization and deserialization utilities specifically designed for Git types. It handles the conversion of Git objects to and from various formats, with support for legacy git2 features to maintain backward compatibility.

**Lines of Code:** 273 (0.3K)

**Recent Activity (last 30 days):** 1 commits (most active: Sebastian Thiel)

**Recent changes:**
- Turn `gitbutler-serde` into `but-serde` with legacy feature

### Database & Storage

#### but-db
A SQLite database layer built on top of the Diesel ORM. This crate manages all persistent storage needs, including migrations support. It bundles libsqlite3 on Windows to ensure consistent behavior across platforms.

**Lines of Code:** 1,247 (1.2K)

**Recent Activity (last 30 days):** 6 commits (most active: Caleb Owens)

**Recent changes:**
- Bump the rust-updates group with 15 updates
- Fold `gitbutler-command-context` into `but-ctx`.
- Add option to have wildcard permissions
- Session-wise
- UI for permissions :D

#### but-forge-storage
Manages persistent storage for forge information (GitHub, GitLab, etc.). This crate stores and retrieves metadata about connected forges, including authentication tokens, API endpoints, and repository mappings.

**Lines of Code:** 288 (0.3K)

**Recent Activity (last 30 days):** 2 commits (most active: Sebastian Thiel)

**Recent changes:**
- Elevate `github` module from commmands into the top-level.
- Elevate `gitbutler-fs` and merge `gitbutler-storage` into it.

#### but-secret
Handles secure storage and retrieval of sensitive information using the system keyring. This crate ensures that credentials and secrets are stored securely using platform-native secure storage mechanisms.

**Lines of Code:** 290 (0.3K)

**Recent Activity (last 30 days):** 1 commits (most active: Sebastian Thiel)

**Recent changes:**
- Migrate `gitbutler-error` into the `but` world.

### Settings & Configuration

#### but-settings
Manages application settings and configuration with built-in file watching support using the notify library. It handles JSON configuration files with lenient parsing to accommodate user modifications and provides reactive updates when settings files change.

**Lines of Code:** 702 (0.7K)

**Recent Activity (last 30 days):** 4 commits (most active: Sebastian Thiel)

**Recent changes:**
- but-actions is no more
- Elevate `github` module from commmands into the top-level.
- Elevate `gitbutler-fs` and merge `gitbutler-storage` into it.
- Move `but_workspace::branch::safe_checkout()` to `but_core::worktree::safe_checkout()`

#### but-path
Provides path handling utilities and platform-specific path operations. It includes functionality for opening paths in default system applications and normalizing path representations across different operating systems.

**Lines of Code:** 132 (0.1K)

**Recent Activity (last 30 days):** 2 commits (most active: estib)

**Recent changes:**
- Deeplink: Add timestamp for to the deeplink
- Correctly detect the application type

### Filesystem & I/O

#### but-fs
Handles filesystem operations with TOML support. This crate provides abstractions over common file operations and includes a legacy feature flag for backward compatibility with older code.

**Lines of Code:** 151 (0.2K)

**Recent Activity (last 30 days):** 2 commits (most active: Sebastian Thiel)

**Recent changes:**
- Fold `gitbutler-command-context` into `but-ctx`.
- Elevate `gitbutler-fs` and merge `gitbutler-storage` into it.

#### but-status
Implements Git status operations using the modern gitoxide library. It efficiently determines the working directory state, tracking changes, untracked files, and staging area contents.

**Lines of Code:** 170 (0.2K)

**Recent Activity (last 30 days):** 1 commits (most active: copilot-swe-agent[bot])

**Recent changes:**
- Fix spelling and grammatical errors across repository

### Graph & Visualization

#### but-graph
Represents Git commit graphs as connected segments and provides various graph operations. Using the petgraph library for graph data structures, it supports revision walking, ancestry queries, and topology analysis. This is essential for visualizing branch relationships and commit history.

**Lines of Code:** 6,022 (6.0K)

**Recent Activity (last 30 days):** 20 commits (most active: Sebastian Thiel)

**Recent changes:**
- Fix spelling and grammatical errors across repository
- Add tests for single-branch `but branch apply`
- Add missing tests for `apply()` to be sure it works without extra metadata.
- Bump the rust-updates group with 15 updates
- Add `but_core::ref_metadata::Workspace::target_commit_id` as field.

#### but-feedback
Implements a feedback collection system that bundles diagnostic information. It uses zip compression to create comprehensive feedback bundles that include logs, configurations, and error reports for debugging purposes.

**Lines of Code:** 142 (0.1K)

**Recent Activity (last 30 days):** 5 commits (most active: Sebastian Thiel)

**Recent changes:**
- Fold `gitbutler-command-context` into `but-ctx`.
- Auto-add the targets from workspaces to remove the need for `to_graph_options()` for extra targets.
- Allow `Context` to be created by `(Legacy)ProjectId`.
- Allow `but-graph` to be used in `but-meta` by inverting dependency.
- Move the `RefMetadata` implementation into `but-meta`

### Hunk Management

#### but-hunk-dependency
Analyzes dependencies between code hunks to determine which changes depend on others. Supporting both git2 and gix backends, it's crucial for intelligent merging and conflict detection. It helps determine if hunks can be applied independently or require specific ordering.

**Lines of Code:** 1,182 (1.2K)

**Recent Activity (last 30 days):** 11 commits (most active: Sebastian Thiel)

**Recent changes:**
- Fix spelling and grammatical errors across repository
- Make `but_api::legacy::diff::commit_details()` non-legacy.
- Move all Commands and code that depends on legacy behind a default-on legacy feature toggle.
- Fold `gitbutler-command-context` into `but-ctx`.
- Replace `.

#### but-hunk-assignment
Assigns code hunks to specific branches or stacks based on various criteria. Integrated with the database layer, it maintains persistent mappings between hunks and their target branches.

**Lines of Code:** 992 (1.0K)

**Recent Activity (last 30 days):** 8 commits (most active: Sebastian Thiel)

**Recent changes:**
- but-hunk-assignment: clarify return value of `assignments_with_fallback`
- but-hunk-assignment: clarify ret.
- reconcile: clarify return type of `assignments`
- Move all Commands and code that depends on legacy behind a default-on legacy feature toggle.
- Fold `gitbutler-command-context` into `but-ctx`.

### Workspace & Branch Operations

#### but-workspace
Core workspace management functionality that serves as the foundation for GitButler's virtual branch system. It supports legacy features through feature flags and includes SPMC (Single Producer, Multiple Consumer) channels for communication. The export-ts feature enables TypeScript type generation.

**Lines of Code:** 7,975 (8.0K)

**Recent Activity (last 30 days):** 36 commits (most active: Sebastian Thiel)

**Recent changes:**
- refactor
- Fix spelling and grammatical errors across repository
- Make `but_api::legacy::diff::commit_details()` non-legacy.
- Update to `gix@main` to see URL related fixes (#11419)
- Add missing tests for `apply()` to be sure it works without extra metadata.

#### but-worktrees
Manages Git worktree operations, allowing multiple working directories for a single repository. This enables parallel work on different branches without constant switching overhead.

**Lines of Code:** 539 (0.5K)

**Recent Activity (last 30 days):** 11 commits (most active: Sebastian Thiel)

**Recent changes:**
- refactor
- Fix spelling and grammatical errors across repository
- Move all Commands and code that depends on legacy behind a default-on legacy feature toggle.
- pnpm rustfmt
- Fold `gitbutler-command-context` into `but-ctx`.

### Rebase & Cherry-Pick

#### but-rebase
Implements Git rebase operations with Gerrit support. Using gix for merge operations, it provides both interactive and non-interactive rebasing capabilities with support for Gerrit's Change-Id workflow.

**Lines of Code:** 995 (1.0K)

**Recent Activity (last 30 days):** 7 commits (most active: Sebastian Thiel)

**Recent changes:**
- Fix spelling and grammatical errors across repository
- Update to `gix@main` to see URL related fixes (#11419)
- Bump the rust-updates group with 15 updates
- Fold `gitbutler-command-context` into `but-ctx`.
- Rename `gitbutler-oxidize` to `but-oxidize`.

#### but-cherry-apply
Contains the logic for applying commits through cherry-picking. This crate handles the complexities of applying changes from one branch to another, including conflict detection and resolution.

**Lines of Code:** 149 (0.1K)

**Recent Activity (last 30 days):** 10 commits (most active: Sebastian Thiel)

**Recent changes:**
- refactor
- Fix spelling and grammatical errors across repository
- Move all Commands and code that depends on legacy behind a default-on legacy feature toggle.
- pnpm rustfmt
- Fold `gitbutler-command-context` into `but-ctx`.

### Metadata & Context

#### but-meta
Provides metadata operations for Git entities by implementing traits from but-core. With a legacy feature that includes extensive dependencies, it serves as a bridge between modern and legacy code paths while providing rich metadata about commits, branches, and other Git objects.

**Lines of Code:** 1,246 (1.2K)

**Recent Activity (last 30 days):** 14 commits (most active: Sebastian Thiel)

**Recent changes:**
- Address Copilot review notes
- IdMap unit'y test with assignments (and add `but-testsupport::Sandbox`)
- Add `legacy::IdDb` unit tests
- Add tests for single-branch `but branch apply`
- Bump the rust-updates group with 15 updates

#### but-ctx
Implements repository-specific context management. This crate maintains the operational context for working with a specific repository, including configuration, state, and cached metadata. It supports integration with legacy project structures.

**Lines of Code:** 506 (0.5K)

**Recent Activity (last 30 days):** 14 commits (most active: Sebastian Thiel)

**Recent changes:**
- Add `legacy::IdDb` unit tests
- Add support for converting select types automatically by code injection.
- Create a mixed-mode non-legacy apply.
- Add workspace reconcilation in the workspace adapter.
- Revert "Bring back the extra-target setup so branch creation works like before.

### Operations Log

#### but-oplog
Implements an undo queue through restore-points, providing comprehensive undo/redo functionality. This operation log tracks all changes made to the workspace, allowing users to revert to previous states. A legacy wrapper maintains compatibility with older code.

**Lines of Code:** 56 (0.1K)

**Recent Activity (last 30 days):** 3 commits (most active: Sebastian Thiel)

**Recent changes:**
- Create a mixed-mode non-legacy apply.
- Provide a non-legacy version of `branch apply`
- Create a minimal version of `but-oplog` that is mostly legacy, to enable `but-api`

### AI Integration

#### but-action
An AI-powered actions system using async-openai for LLM integration. This crate enables AI-driven operations on the codebase, with a builtin-but feature for embedding functionality directly into the CLI.

**Lines of Code:** 2,369 (2.4K)

**Recent Activity (last 30 days):** 15 commits (most active: Sebastian Thiel)

**Recent changes:**
- Fix spelling and grammatical errors across repository
- Make `but_api::legacy::diff::commit_details()` non-legacy.
- refactor
- Port code to async-openai 0.
- Move all Commands and code that depends on legacy behind a default-on legacy feature toggle.

#### but-claude
Integrates Claude AI with MCP (Model Context Protocol) support. This crate provides access to Claude's capabilities within GitButler, including desktop notifications for AI-generated suggestions and operations.

**Lines of Code:** 4,698 (4.7K)

**Recent Activity (last 30 days):** 35 commits (most active: Sebastian Thiel)

**Recent changes:**
- Fix spelling and grammatical errors across repository
- simplify git clone implementation
- Suggest using `but --json` flag in codegen system prompt
- Improve the Claude system prompt
- Improve Claude Code git usage instructions in bridge

#### but-cursor
Provides integration with the Cursor editor. Using MD5 for session management, it enables bidirectional communication between GitButler and Cursor for enhanced editing experiences.

**Lines of Code:** 514 (0.5K)

**Recent Activity (last 30 days):** 7 commits (most active: Sebastian Thiel)

**Recent changes:**
- Fix spelling and grammatical errors across repository
- Bump the rust-updates group with 15 updates
- Move all Commands and code that depends on legacy behind a default-on legacy feature toggle.
- Fold `gitbutler-command-context` into `but-ctx`.
- Move the `RefMetadata` implementation into `but-meta`

#### but-bot
Implements bot functionality for automated operations. This crate enables programmatic interactions with repositories through scripted or AI-driven workflows.

**Lines of Code:** 812 (0.8K)

**Recent Activity (last 30 days):** 3 commits (most active: Sebastian Thiel)

**Recent changes:**
- Fix spelling and grammatical errors across repository
- Move all Commands and code that depends on legacy behind a default-on legacy feature toggle.
- Fold `gitbutler-command-context` into `but-ctx`.

#### but-tools
A collection of AI-powered tools that integrate with OpenAI and the operation log. These tools provide intelligent assistance for common Git operations and code management tasks.

**Lines of Code:** 2,021 (2.0K)

**Recent Activity (last 30 days):** 15 commits (most active: Sebastian Thiel)

**Recent changes:**
- refactor
- Fix spelling and grammatical errors across repository
- Make `but_api::legacy::diff::commit_details()` non-legacy.
- Port code to async-openai 0.
- Create a mixed-mode non-legacy apply.

### Rules & Automation

#### but-rules
A rule-based automation system with regex support. Using serde_regex for pattern serialization, it allows users to define custom rules that automatically trigger actions based on repository events or file changes.

**Lines of Code:** 511 (0.5K)

**Recent Activity (last 30 days):** 12 commits (most active: Sebastian Thiel)

**Recent changes:**
- Fix spelling and grammatical errors across repository
- Create a mixed-mode non-legacy apply.
- Move all Commands and code that depends on legacy behind a default-on legacy feature toggle.
- Fold `gitbutler-command-context` into `but-ctx`.
- Auto-add the targets from workspaces to remove the need for `to_graph_options()` for extra targets.

### Forge Integration

#### but-forge
Provides a generic abstraction layer for interacting with different forges (GitHub, GitLab, Gerrit, etc.). This crate defines common interfaces that specific forge implementations can implement, enabling forge-agnostic code.

**Lines of Code:** 535 (0.5K)

**Recent Activity (last 30 days):** 3 commits (most active: estib)

**Recent changes:**
- Forge Review: Check whether it's open
- GB GitHub: Get PR by ID
- Elevate `github` module from commmands into the top-level.

#### but-github
GitHub API integration using the octorust library. This crate provides comprehensive GitHub functionality including repository management, pull requests, issues, and authentication. It includes legacy user support for backward compatibility.

**Lines of Code:** 1,006 (1.0K)

**Recent Activity (last 30 days):** 8 commits (most active: Sebastian Thiel)

**Recent changes:**
- Fold `gitbutler-command-context` into `but-ctx`.
- GB GitHub: Get PR by ID
- Elevate `github` module from commmands into the top-level.
- Elevate `gitbutler-fs` and merge `gitbutler-storage` into it.
- Clean github module token handling to consistently use `Sensitive<String>`

#### but-gerrit
Integrates with the Gerrit code review platform. Using SHA-1 hashing for change tracking, it implements Gerrit's specific workflows including Change-Ids and review workflows.

**Lines of Code:** 806 (0.8K)

**Recent Activity (last 30 days):** 2 commits (most active: Sebastian Thiel)

**Recent changes:**
- Move all Commands and code that depends on legacy behind a default-on legacy feature toggle.
- Fold `gitbutler-command-context` into `but-ctx`.

### API & Server

#### but-api
The main API layer with multiple features including Tauri, path-bytes, and legacy support. With extensive optional dependencies, it provides modular functionality that can be selectively enabled based on deployment needs.

**Lines of Code:** 3,625 (3.6K)

**Recent Activity (last 30 days):** 64 commits (most active: Sebastian Thiel)

**Recent changes:**
- refactor
- Fix spelling and grammatical errors across repository
- Address review by Kiril
- Address Copilot review comments
- Rename the macro to the absolute epic.

#### but-api-macros
Procedural macros for API code generation. Using convert_case for naming conventions, it automatically generates boilerplate API code, reducing manual coding and ensuring consistency.

**Lines of Code:** 407 (0.4K)

**Recent Activity (last 30 days):** 13 commits (most active: Sebastian Thiel)

**Recent changes:**
- Document paramter transformations of the `but_api` procmacro.
- Address review by Kiril
- Rename the macro to the absolute epic.
- Remove the legacy version of `commit_details` in favor of the modern version.
- Add support for converting select types automatically by code injection.

#### but-server
An HTTP server built with Axum, featuring WebSocket support for real-time communication. It includes CORS support for web clients and integrates both feedback collection and Claude AI functionality.

**Lines of Code:** 787 (0.8K)

**Recent Activity (last 30 days):** 30 commits (most active: Sebastian Thiel)

**Recent changes:**
- refactor
- Address review by Kiril
- Remove the legacy version of `commit_details` in favor of the modern version.
- simplify git clone implementation
- Bump the rust-updates group with 15 updates

### CLI Tools

#### but
The main CLI binary featuring a rich terminal UI built with ratatui and crossterm. It includes a pager (minus) for viewing large outputs, telemetry via PostHog, and extensive legacy feature support to maintain compatibility with older workflows.

**Lines of Code:** 11,124 (11.1K)

**Recent Activity (last 30 days):** 148 commits (most active: Sebastian Thiel)

**Recent changes:**
- refactor
- Fix spelling and grammatical errors across repository
- IdMap unit'y test with assignments (and add `but-testsupport::Sandbox`)
- refactor
- id: cleanup `parse_str` branch handling

#### but-clap
An alternative CLI interface using the Clap argument parser. This provides a more traditional command-line argument parsing approach compared to the main but binary's interactive TUI.

**Lines of Code:** 226 (0.2K)

**Recent Activity (last 30 days):** 7 commits (most active: Scott Chacon)

**Recent changes:**
- Make `but` tests work in non-legacy mode and the capability to CI
- Fold `gitbutler-command-context` into `but-ctx`.
- Use Args::command() directly and export args module
- rustfmt rust linter wanted this
- move commit utilities into utils/commits.

#### gitbutler-cli
The legacy CLI tool with testing features. Using gix with max-performance and tracing enabled, it represents the earlier command-line interface before the transition to the newer but binary.

**Lines of Code:** 599 (0.6K)

**Recent Activity (last 30 days):** 13 commits (most active: Sebastian Thiel)

**Recent changes:**
- Fix spelling and grammatical errors across repository
- IdMap unit'y test with assignments (and add `but-testsupport::Sandbox`)
- Create a mixed-mode non-legacy apply.
- Move all Commands and code that depends on legacy behind a default-on legacy feature toggle.
- Fold `gitbutler-command-context` into `but-ctx`.

### Testing & Debugging

#### but-testsupport
Testing utilities with optional snapbox support for snapshot testing. The termtree feature enables visualization of test results in tree format, making it easier to understand complex test scenarios.

**Lines of Code:** 1,291 (1.3K)

**Recent Activity (last 30 days):** 15 commits (most active: Sebastian Thiel)

**Recent changes:**
- Address Copilot review notes
- IdMap unit'y test with assignments (and add `but-testsupport::Sandbox`)
- Add `legacy::IdDb` unit tests
- Add tests for single-branch `but branch apply`
- Simplify testsupport mode normalization

#### but-testing
A binary specifically designed for testing scenarios. It includes features for generating stable commits, ensuring reproducible tests regardless of system time or user configuration.

**Lines of Code:** 1,719 (1.7K)

**Recent Activity (last 30 days):** 19 commits (most active: Sebastian Thiel)

**Recent changes:**
- IdMap unit'y test with assignments (and add `but-testsupport::Sandbox`)
- Make `but_api::legacy::diff::commit_details()` non-legacy.
- Create a mixed-mode non-legacy apply.
- Move all Commands and code that depends on legacy behind a default-on legacy feature toggle.
- Fold `gitbutler-command-context` into `but-ctx`.

#### but-debugging
Minimal debugging utilities for development and troubleshooting. As a lightweight crate with no dependencies, it provides basic debugging helpers.

**Lines of Code:** 125 (0.1K)

**Recent Activity (last 30 days):** 1 commits (most active: copilot-swe-agent[bot])

**Recent changes:**
- Fix spelling and grammatical errors across repository

#### gitbutler-testsupport
Legacy test support with project setup utilities. Including keyring and gix-testtools, it provides comprehensive testing infrastructure for the older gitbutler-* crates.

**Lines of Code:** 1,114 (1.1K)

**Recent Activity (last 30 days):** 8 commits (most active: Sebastian Thiel)

**Recent changes:**
- IdMap unit'y test with assignments (and add `but-testsupport::Sandbox`)
- Move all Commands and code that depends on legacy behind a default-on legacy feature toggle.
- Fold `gitbutler-command-context` into `but-ctx`.
- Elevate `gitbutler-fs` and merge `gitbutler-storage` into it.
- Move the `RefMetadata` implementation into `but-meta`

### Legacy GitButler Crates

#### gitbutler-tauri
The main Tauri desktop application with an extensive plugin ecosystem. It includes updater, file system access, HTTP client, and other Tauri plugins. macOS-specific features include traffic lights positioner for window chrome. The builtin-but feature embeds the new CLI, while devtools enables development tools.

**Lines of Code:** 2,098 (2.1K)

**Recent Activity (last 30 days):** 46 commits (most active: Sebastian Thiel)

**Recent changes:**
- refactor
- Fix spelling and grammatical errors across repository
- Remove the legacy version of `commit_details` in favor of the modern version.
- Add support for converting select types automatically by code injection.
- Bump the rust-updates group with 15 updates

#### gitbutler-watcher
File monitoring and change detection using gitbutler-filemonitor. This crate watches the repository for changes and triggers rule evaluation and workspace updates automatically.

**Lines of Code:** 307 (0.3K)

**Recent Activity (last 30 days):** 5 commits (most active: estib)

**Recent changes:**
- Move all Commands and code that depends on legacy behind a default-on legacy feature toggle.
- Fold `gitbutler-command-context` into `but-ctx`.
- TS RS: Generate TS types from the Rust types
- File Monitor: Emit git activity events on ref updates
- Watcher: Watch for the HEAD SHA

#### gitbutler-filemonitor
Low-level file monitoring with debouncing using the notify library. It implements a backoff strategy to avoid excessive notifications during rapid file changes and enforces strict clippy lints for code quality.

**Lines of Code:** 963 (1.0K)

**Recent Activity (last 30 days):** 4 commits (most active: Sebastian Thiel)

**Recent changes:**
- Fix spelling and grammatical errors across repository
- pnpm rustfmt
- Fold `gitbutler-command-context` into `but-ctx`.
- File Monitor: Emit git activity events on ref updates

#### gitbutler-workspace
Legacy workspace operations focused on stack and repository management. This represents the older implementation before the transition to but-workspace.

**Lines of Code:** 276 (0.3K)

**Recent Activity (last 30 days):** 8 commits (most active: Sebastian Thiel)

**Recent changes:**
- refactor
- Fix spelling and grammatical errors across repository
- Create a mixed-mode non-legacy apply.
- Move all Commands and code that depends on legacy behind a default-on legacy feature toggle.
- pnpm rustfmt

#### gitbutler-stack
Manages stacks (series of related branches) with TOML persistence. Stacks allow grouping related branches and managing them as a unit, with configuration stored in TOML files.

**Lines of Code:** 2,180 (2.2K)

**Recent Activity (last 30 days):** 13 commits (most active: Sebastian Thiel)

**Recent changes:**
- Fix spelling and grammatical errors across repository
- Update to `gix@main` to see URL related fixes (#11419)
- Create a mixed-mode non-legacy apply.
- Move all Commands and code that depends on legacy behind a default-on legacy feature toggle.
- Fold `gitbutler-command-context` into `but-ctx`.

#### gitbutler-branch
Branch operations and management using lazy_static for shared state. This crate provides the foundation for GitButler's virtual branch system in the legacy codebase.

**Lines of Code:** 235 (0.2K)

**Recent Activity (last 30 days):** 4 commits (most active: Sebastian Thiel)

**Recent changes:**
- Fold `gitbutler-command-context` into `but-ctx`.
- Dissolve`gitbutler-tagged-string` crate as it's only used in one place.
- Move the `RefMetadata` implementation into `but-meta`
- Move `but_workspace::branch::safe_checkout()` to `but_core::worktree::safe_checkout()`

#### gitbutler-branch-actions
High-level branch operations including create, update, delete, and other actions. Integrated with oplog, all branch operations are tracked for undo/redo functionality.

**Lines of Code:** 6,236 (6.2K)

**Recent Activity (last 30 days):** 31 commits (most active: Sebastian Thiel)

**Recent changes:**
- refactor
- Fix spelling and grammatical errors across repository
- IdMap unit'y test with assignments (and add `but-testsupport::Sandbox`)
- Update to `gix@main` to see URL related fixes (#11419)
- Create a mixed-mode non-legacy apply.

#### gitbutler-repo
Comprehensive repository operations including status, rebase, Gerrit support, fuzzy matching, and file ignore patterns. This is one of the core legacy crates handling direct Git repository interactions.

**Lines of Code:** 1,433 (1.4K)

**Recent Activity (last 30 days):** 8 commits (most active: Sebastian Thiel)

**Recent changes:**
- Fix spelling and grammatical errors across repository
- Support `core.
- Create a mixed-mode non-legacy apply.
- Move all Commands and code that depends on legacy behind a default-on legacy feature toggle.
- Fold `gitbutler-command-context` into `but-ctx`.

#### gitbutler-repo-actions
High-level repository actions with async tokio support. This crate provides asynchronous versions of common repository operations for better performance in the desktop application.

**Lines of Code:** 450 (0.5K)

**Recent Activity (last 30 days):** 9 commits (most active: Sebastian Thiel)

**Recent changes:**
- Remove gitbutler-git based signing
- Use git to clone projects
- Create a mixed-mode non-legacy apply.
- Move all Commands and code that depends on legacy behind a default-on legacy feature toggle.
- Fold `gitbutler-command-context` into `but-ctx`.

#### gitbutler-project
Project management and configuration, including forge integration. Using reqwest for HTTP transport, it manages project-level settings and remote connections.

**Lines of Code:** 1,099 (1.1K)

**Recent Activity (last 30 days):** 17 commits (most active: Sebastian Thiel)

**Recent changes:**
- Fix spelling and grammatical errors across repository
- IdMap unit'y test with assignments (and add `but-testsupport::Sandbox`)
- Add `legacy::IdDb` unit tests
- Fold `gitbutler-command-context` into `but-ctx`.
- Elevate `github` module from commmands into the top-level.

#### gitbutler-operating-modes
Defines different operating modes for the application (edit mode, workspace mode, etc.). This allows GitButler to switch between different operational paradigms based on user needs.

**Lines of Code:** 167 (0.2K)

**Recent Activity (last 30 days):** 7 commits (most active: Sebastian Thiel)

**Recent changes:**
- Move all Commands and code that depends on legacy behind a default-on legacy feature toggle.
- Fold `gitbutler-command-context` into `but-ctx`.
- Elevate `github` module from commmands into the top-level.
- Elevate `gitbutler-fs` and merge `gitbutler-storage` into it.
- Move `but_workspace::branch::safe_checkout()` to `but_core::worktree::safe_checkout()`

#### gitbutler-edit-mode
Implements edit mode functionality for direct Git operations. In edit mode, GitButler acts more like a traditional Git client, allowing direct manipulation of branches and commits.

**Lines of Code:** 398 (0.4K)

**Recent Activity (last 30 days):** 8 commits (most active: Sebastian Thiel)

**Recent changes:**
- refactor
- Make `but_api::legacy::diff::commit_details()` non-legacy.
- Create a mixed-mode non-legacy apply.
- Fold `gitbutler-command-context` into `but-ctx`.
- rustfmt nightly for cleaner imports

#### gitbutler-oplog
Legacy oplog implementation with branch and stack support. This predates but-oplog and maintains compatibility with the older workspace system.

**Lines of Code:** 1,596 (1.6K)

**Recent Activity (last 30 days):** 12 commits (most active: Sebastian Thiel)

**Recent changes:**
- Fix spelling and grammatical errors across repository
- Make `but_api::legacy::diff::commit_details()` non-legacy.
- Create a mixed-mode non-legacy apply.
- Create a minimal version of `but-oplog` that is mostly legacy, to enable `but-api`
- pnpm rustfmt

#### gitbutler-sync
Synchronization operations for remote repositories. This crate handles fetching, pulling, and pushing operations with remote repositories.

**Lines of Code:** 416 (0.4K)

**Recent Activity (last 30 days):** 10 commits (most active: Sebastian Thiel)

**Recent changes:**
- Fix spelling and grammatical errors across repository
- Update to `gix@main` to see URL related fixes (#11419)
- Create a mixed-mode non-legacy apply.
- Move all Commands and code that depends on legacy behind a default-on legacy feature toggle.
- Fold `gitbutler-command-context` into `but-ctx`.

#### gitbutler-git
Git operations wrapper with askpass and setsid binaries. It includes platform-specific features for Unix and Windows, with a test-askpass-path feature for testing credential workflows. Strict clippy lints ensure code quality.

**Lines of Code:** 1,241 (1.2K)

**Recent Activity (last 30 days):** 11 commits (most active: Sebastian Thiel)

**Recent changes:**
- Fix local relative upstream path
- Fix spelling and grammatical errors across repository
- Minor refactor for more 'gixomatic' config access.
- Remove gitbutler-git based signing
- simplify git clone implementation

#### gitbutler-commit
Commit operations with support for stable commit generation during testing. This ensures reproducible commits in tests by controlling timestamps and other variable data.

**Lines of Code:** 202 (0.2K)

**Recent Activity (last 30 days):** No commits

#### gitbutler-cherry-pick
Cherry-pick operations using both git2 and gix libraries. This dual support allows gradual migration to gitoxide while maintaining compatibility with existing git2-based code.

**Lines of Code:** 170 (0.2K)

**Recent Activity (last 30 days):** 3 commits (most active: Sebastian Thiel)

**Recent changes:**
- Create a mixed-mode non-legacy apply.
- Fold `gitbutler-command-context` into `but-ctx`.
- Rename `gitbutler-oxidize` to `but-oxidize`.

#### gitbutler-diff
Diff operations and hunk management using the diffy library. MD5 hashing generates change IDs for tracking specific modifications across operations.

**Lines of Code:** 1,179 (1.2K)

**Recent Activity (last 30 days):** 3 commits (most active: Sebastian Thiel)

**Recent changes:**
- Create a mixed-mode non-legacy apply.
- Fold `gitbutler-command-context` into `but-ctx`.
- Turn `gitbutler-serde` into `but-serde` with legacy feature

#### gitbutler-hunk-dependency
Legacy hunk dependency analysis that wraps but-hunk-dependency. This maintains the older API while delegating to the newer implementation.

**Lines of Code:** 2,375 (2.4K)

**Recent Activity (last 30 days):** 3 commits (most active: Sebastian Thiel)

**Recent changes:**
- Fix spelling and grammatical errors across repository
- Fold `gitbutler-command-context` into `but-ctx`.
- Turn `gitbutler-serde` into `but-serde` with legacy feature

#### gitbutler-reference
Git reference management using both git2 and gix. This crate handles branches, tags, and other Git references, supporting both implementation backends.

**Lines of Code:** 402 (0.4K)

**Recent Activity (last 30 days):** 1 commits (most active: Sebastian Thiel)

**Recent changes:**
- Dissolve`gitbutler-tagged-string` crate as it's only used in one place.

#### gitbutler-url
URL parsing and validation specifically for Git remotes. It handles various Git URL formats (HTTPS, SSH, git://) and validates remote configurations.

**Lines of Code:** 369 (0.4K)

**Recent Activity (last 30 days):** No commits

#### gitbutler-user
User management and authentication using keyring for credential storage. This crate manages user profiles, authentication tokens, and identity information.

**Lines of Code:** 199 (0.2K)

**Recent Activity (last 30 days):** 2 commits (most active: Sebastian Thiel)

**Recent changes:**
- Fold `gitbutler-command-context` into `but-ctx`.
- Elevate `gitbutler-fs` and merge `gitbutler-storage` into it.

#### gitbutler-time
A minimal time utilities crate with no dependencies. It provides simple time-related helpers needed across the legacy codebase.

**Lines of Code:** 32 (0.0K)

**Recent Activity (last 30 days):** No commits

---

## Architecture Notes

The codebase shows an ongoing transition from legacy `gitbutler-*` crates to newer `but-*` crates. Many packages include "legacy" feature flags to maintain backward compatibility during this migration. The newer crates use `gix` (gitoxide - a pure Rust Git implementation) while legacy code uses `git2` (libgit2 bindings), with `but-oxidize` providing conversion utilities between the two approaches.

**Total packages: 64**
