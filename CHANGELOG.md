# Changelog

All notable changes to DevLog are documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

Each release corresponds to the completion of a curriculum phase.

---

## [Unreleased]

### In progress — Phase 3: Functions & Modules
- Variadic functions with `*args` and `**kwargs`
- A `make_task()` factory to centralise task construction
- Splitting DevLog into multiple modules
- Restructuring into an installable package layout (`python -m devlog`)

---

## [0.2.0] — Phase 2: Data Structures

### Added
- Tasks stored as structured dictionaries in a list
- Each task carries `id`, `title`, `status`, `priority`, and `tags`
- List all tasks with formatted output
- Filter tasks by status
- Filter tasks by tag using set operations
- Mark a task as complete
- Delete a task

### Changed
- Task data moved from single variables into in-memory collections

<!--
  Replace the date below with the actual tag date when you cut the release:
  ## [0.2.0] - 2026-xx-xx
-->

---

## [0.1.0] — Phase 1: Foundations

### Added
- Interactive terminal menu with a welcome banner and version
- Numbered menu options: Add Task, List Tasks, Quit
- User input handling for menu selection
- Input validation for empty input and invalid choices
- Core menu loop that runs until the user quits

---

<!--
  Template for future phase releases — copy this block when cutting a new version:

  ## [0.X.0] - YYYY-MM-DD  (Phase N: Name)

  ### Added
  - new features

  ### Changed
  - changes to existing behaviour

  ### Fixed
  - bug fixes

  ### Removed
  - removed features
-->

[Unreleased]: https://github.com/muhib/devlog/compare/v0.2.0...HEAD
[0.2.0]: https://github.com/muhib/devlog/compare/v0.1.0...v0.2.0
[0.1.0]: https://github.com/muhib/devlog/releases/tag/v0.1.0