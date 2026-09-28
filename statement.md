# Problem Statement & Project Scope

## Problem Statement
Students and individuals often struggle to track daily micro-expenses, leading to poor budgeting and unexpected financial stress. Existing commercial tools are frequently overly complex, require cloud account syncing, or lack simple local expense breakdown tools.

## Target Users
- Undergraduate college students
- Individuals looking for a simple, fast, command-line budgeting solution
- Users who prefer offline data tracking without complex setups

## Scope of the Project
The Personal Expense Tracker provides a minimal, terminal-based workflow to capture expense transactions in real-time. Built using object-oriented principles, it enables users to categorize items, search past entries, calculate aggregate spending statistics using NumPy, persist data locally in JSON format, and delete unwanted logs.

## High-Level Features
1. **Transaction Logging**: Record date, category, tag, and monetary value using OOP inheritance (`Transaction` -> `Expense`).
2. **Data Presentation**: Formatted list rendering of historical records.
3. **Numerical Analytics**: Execution of sum, average, max, and min transaction math via NumPy and itertools.
4. **Targeted Filtering**: Case-insensitive search across category labels.
5. **Data Persistence**: Local storage and recovery using JSON files.
6. **Record Removal**: Deletion of entries by index with validation bounds.
7. **Automated Testing**: Test suite built with native assertions.
