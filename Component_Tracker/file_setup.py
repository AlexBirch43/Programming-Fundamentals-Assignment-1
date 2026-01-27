import csv
import os

CSV_FILE = 'inventory.csv'

#  Create CSV with set headers if non-existant
# ******WOULD LIKE TO ADD IN CHECK HERE IF NOT EXISTING "WOULD YOU LIKE TO CREATE NEW CSV"
def check_csv():
    if not os.path.exists(CSV_FILE):
        with open(CSV_FILE, mode='w', newline='') as file:
            fieldnames = ['name', 'type', 'quantity']
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
