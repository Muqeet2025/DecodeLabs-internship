# Expense Tracker (Python Project 2)

## Overview

A simple command-line Expense Tracker built in Python using a single file. The program allows users to enter expenses continuously, calculates the total, and displays the final amount spent.

This project demonstrates fundamental programming concepts such as loops, user input, and accumulator logic.

---

## Features

* Continuous expense input
* Automatic total calculation
* Simple and beginner-friendly
* Single-file implementation

---

## Tech Stack

* Python 3

---

## Project Structure

```id="k8p3o1"
expense-tracker/
│
└── main.py
```

---

## How It Works

1. Program starts with total = 0
2. User enters expense values
3. Each value is added to total
4. User enters `'q'` to stop
5. Final total is displayed

---

## How to Run

### Step 1: Navigate to folder

```bash id="g9k2v4"
cd expense-tracker
```

### Step 2: Run the program

```bash id="z1x7lp"
python main.py
```

---

## Example Usage

```id="y2n8qa"
Enter expense (or 'q' to quit): 100
Enter expense (or 'q' to quit): 50
Enter expense (or 'q' to quit): q

Total spent: 150.0
```

---

## Learning Outcomes

* Understanding accumulator (`total += value`)
* Working with loops
* Handling user input

---

## Future Improvements

* Add error handling for invalid input
* Add categories (food, travel, etc.)
* Save expenses to a file

---

## Author

Muqeet Shah

---

## License

This project is for educational purposes as part of the DecodeLabs Internship Program.
