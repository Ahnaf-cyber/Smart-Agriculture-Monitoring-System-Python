Smart Agriculture Monitoring System (Python Project)
Overview

This is a Python-based Smart Agriculture Monitoring System developed as a university project.

The system allows users to manage farmers, technicians, agricultural tasks, observations, and financial records in an organized way.

It supports:

GUI-based interface (Tkinter)

File handling for persistent data storage

Object-Oriented Programming structure

Technologies Used

Python

OOP (Object-Oriented Programming)

Tkinter (GUI)

Pillow (Image handling)

Pickle (File storage)

OS Module

Features

Add new farmers

View farmer list

Remove farmers

Add technicians

View technicians

Remove technicians

Create and manage tasks

Assign technicians to tasks

Mark tasks as completed

Add and manage farmer observations

Add financial transactions

View transactions

Calculate total revenue

What I Learned

Applying OOP concepts in a real project

Building GUI applications using Tkinter

Handling files using Pickle

Managing structured data in Python

Designing multi-class applications

How to Run

Make sure Python is installed.

Install Pillow library:

pip install pillow

Run the program:

python main.py
Project Structure
main.py
sams_data.pkl   (auto created when program runs)
background.jpg  (optional)
README.md
Notes

All data is stored locally using Pickle.

The system automatically saves data when the application closes.

Duplicate IDs are prevented for better data integrity.

If the background image path is invalid, a default background color is used.
