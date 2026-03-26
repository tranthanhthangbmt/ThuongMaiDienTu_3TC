import csv
import glob

with open('result.txt', 'w', encoding='utf-8') as out:
    files = glob.glob('DB/Chuong_5_Tiet_*.csv')
    for file in files:
        out.write(f"Checking {file}...\n")
        try:
            with open(file, 'r', encoding='utf-8') as f:
                reader = csv.reader(f)
                for i, row in enumerate(reader):
                    if len(row) != 12:
                        out.write(f"File: {file}, Row {i+1} has {len(row)} cols instead of 12.\n")
                        out.write(f"Row content: {row}\n")
        except Exception as e:
            out.write(f"Error parsing {file}: {e}\n")
