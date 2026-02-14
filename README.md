# Python Core Homework 04

Solutions for Python Core homework assignment, module 4. Includes file processing, data handling, and a CLI application.

## Quick Start

### 1. Activate Virtual Environment

**Windows:**

```bash
.venv/Scripts/activate
```

**Mac/Linux:**

```bash
source .venv/bin/activate
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Run Tasks

```bash
# Task 1: Salary Analysis
python task_1/task_1.py

# Task 2: Cat Information
python task_2/task_2.py

# Task 3: Directory Structure Visualization
python task_3/task_3.py <path_to_directory>

# Task 4: CLI Contact Assistant Bot
python task_4/main.py
```

## Implemented Functions

### Task 1: `total_salary(path)`

Calculates total and average salary from a text file.

- **Input:** Path to data file (format: "Name,Salary")
- **Output:** Tuple (total_salary, average_salary)
- **Features:** Uses Decimal for precise calculations, error handling

### Task 2: `get_cats_info(path)`

Reads cat information from a file and returns a list of dictionaries.

- **Input:** Path to file (format: "id,name,age")
- **Output:** List of dictionaries with keys "id", "name", "age"
- **Features:** Data validation, handling of malformed records

### Task 3: `print_directory_structure(path)`

Displays a colored tree visualization of directory structure.

- **Input:** Path to directory
- **Output:** Tree of files and folders with color formatting
- **Features:** Recursive traversal, sorting, color highlighting (colorama)

### Task 4: CLI Contact Assistant Bot

Interactive console application for managing contacts.

**Available Commands:**

- `hello` - greeting
- `add <name> <phone>` - add contact
- `change <name> <phone>` - change phone number
- `phone <name>` - show phone number
- `all` - show all contacts
- `close` / `exit` - exit program

**Module Structure:**

- `input_parser.py` - user command parsing
- `handlers.py` - command handlers (add, change, view contacts)
- `main.py` - main entry point

## Project Structure

```
goit-pycore-hw-04/
├── task_1/
│   ├── task_1.py           # Salary analysis
│   └── salaries.txt        # Test data
├── task_2/
│   ├── task_2.py           # Cat information
│   └── cats.txt            # Test data
├── task_3/
│   └── task_3.py           # Directory visualization
├── task_4/
│   ├── main.py             # CLI bot entry point
│   ├── input_parser.py     # Command parser
│   └── handlers.py         # Contact handlers
├── requirements.txt        # Dependencies
└── README.md              # Documentation
```

## Technologies

- Python 3.12+
- pathlib for path operations
- Decimal for precise financial calculations
- colorama for colored output
- Type hints for type safety
