import csv

students = [
    {"Name": "Alice", "Age": 20, "Grade": "A", "City": "New York"},
    {"Name": "Bob", "Age": 22, "Grade": "B", "City": "Los Angeles"},
    {"Name": "Charlie", "Age": 19, "Grade": "A", "City": "Chicago"},
    {"Name": "Diana", "Age": 21, "Grade": "C", "City": "Houston"},
    {"Name": "Ethan", "Age": 23, "Grade": "B", "City": "Phoenix"},
    {"Name": "Fiona", "Age": 20, "Grade": "A", "City": "Philadelphia"},
    {"Name": "George", "Age": 22, "Grade": "B", "City": "San Antonio"},
    {"Name": "Hannah", "Age": 19, "Grade": "C", "City": "San Diego"},
]
fieldnames = ['Name', 'Age', 'Grade','City']

with open('data.csv','w') as file:
    
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader() # Writes the header row
    writer.writerows(students)