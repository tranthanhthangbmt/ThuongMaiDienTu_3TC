import csv
import re
import os

def read_csv_file(path):
    rows = []
    header = None
    with open(path, 'r', encoding='utf-8-sig') as f:
        reader = csv.reader(f)
        try:
            header = next(reader)
        except StopIteration:
            return None, []
        for row in reader:
            if any(cell.strip() for cell in row):
                rows.append(row)
    return header, rows

def merge_csvs():
    with open('script.js', 'r', encoding='utf-8') as f:
        text = f.read()

    matches = re.findall(r'file:\s*["\'](DB/.*?\.csv)[^"\']*["\']', text)
    
    # Remove duplicates but preserve order
    seen = set()
    unique_matches = []
    for m in matches:
        if m not in seen:
            unique_matches.append(m)
            seen.add(m)

    all_rows = []
    master_header = None
    header_length = 0

    for p in unique_matches:
        path = p.replace('/', os.sep)
        if os.path.exists(path):
            print("Reading:", path)
            header, rows = read_csv_file(path)
            if header and master_header is None:
                master_header = header
                header_length = len(header)
            
            # Normalize row length
            for row in rows:
                padded_row = row + [''] * max(0, header_length - len(row))
                padded_row = padded_row[:header_length]
                all_rows.append(padded_row)
        else:
            print("Not found:", path)

    if master_header:
        out_path = os.path.join('DB', 'Tong_hop_toan_bo.csv')
        with open(out_path, 'w', encoding='utf-8-sig', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(master_header)
            writer.writerows(all_rows)
        print("\nMerged successfully to", out_path)
        print("Total questions merged:", len(all_rows))
    else:
        print("Failed to merge. No valid CSVs found.")

if __name__ == "__main__":
    merge_csvs()
