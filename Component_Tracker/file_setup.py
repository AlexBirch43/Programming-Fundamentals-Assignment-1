import csv
import os

CSV_FILE = 'inventory.csv'

#  Create CSV with set headers if non-existant
def check_csv():
    if not os.path.exists(CSV_FILE):
        print("No CSV file found. Creating a new inventory file for you.")
        with open(CSV_FILE, mode='w', newline='') as file:
            fieldnames = ['name', 'type', 'quantity']
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
        print("New CSV file created.")
