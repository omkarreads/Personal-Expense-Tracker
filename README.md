# Personal Expense Tracker

A simple command-line Python application designed to help users log, view, search, and analyze their daily expenses. Built as part of the Python Essentials coursework using basic control flow, data structures, and the NumPy library.

## Features

- **Add New Expense**: Log individual expenses with date, category, and spent amount.
- **View All Expenses**: Display all logged expenses in an organized list format.
- **Expense Statistics**: Uses NumPy to calculate total expenditure, average spend per transaction, and maximum spend.
- **Search by Category**: Filter and view spending under specific categories (e.g., Food, Travel, Books).
- **Delete Expense**: Remove specific expense entries by line number.

## Project Structure
├── main.py          # Primary Python script containing menu logic and functions
├── requirements.txt # External library dependencies
└── README.md        # Setup and execution instructions

## Setup and Installation

### Prerequisites

- Python 3.x installed on your system.
- Terminal / Command Prompt access.

### Step 1: Clone or Download the Repository

Download the source code files into a local folder or clone the repository using:

```bash
git clone https://github.com/omkarreads/Personal-Expense-Tracker.git
cd Personal-Expense-Tracker
pip install -r requirements.txt
python main.py
