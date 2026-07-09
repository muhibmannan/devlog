# Changelog

All notable changes to DevLog are documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

Each release corresponds to the completion of a curriculum phase.

---

## [Unreleased]

### In progress — Phase 4: Object-Oriented Python

- `Task` class with instance attributes
- Instance methods and class/static methods
- Properties, inheritance, and magic methods
- `Note` subclass and dataclass equivalents

---

## [0.3.0] — Phase 3: Functions & Modules

### Added

- Variadic `make_task()` factory supporting flexible tags via `*args`/`**kwargs`
- Multi-criteria task sorting via a dispatch table
- Package entry point enabling `python -m devlog`

### Changed

- Restructured project into an installable `devlog` package with `__init__.py` and `__main__.py`
- Split the monolithic script into modules by responsibility: `tasks.py` (data and core logic), `display.py` (output), `input.py` (user input), `utils.py` (shared constants and debug state)
- Extracted pure task logic out of the entry point into `tasks.py`
- Replaced named sort key functions with lambdas
- Refactored `handle_choice` from an if/elif chain into a dict dispatch table, with consistent `handler(tasks) -> bool` signatures across all handlers

### Known debt

- `find_task_by_id` and `filter_by_status` in `tasks.py` still call `input()`/`print()` directly — mixed functions not yet fully separated from display concerns. Tracked for cleanup in a later phase.

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

[Unreleased]: https://github.com/muhibmannan/devlog/compare/v0.3.0...HEAD
[0.3.0]: https://github.com/muhibmannan/devlog/compare/v0.2.0...v0.3.0
[0.2.0]: https://github.com/muhibmannan/devlog/compare/v0.1.0...v0.2.0
[0.1.0]: https://github.com/muhibmannan/devlog/releases/tag/v0.1.0
