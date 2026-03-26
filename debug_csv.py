import csv
import sys

def check_file(filename):
    print(f"--- Checking {filename} ---")
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            reader = csv.reader(f)
            header = next(reader)
            print(f"Header length: {len(header)}")
            for i, row in enumerate(reader, 1):
                if len(row) != len(header):
                    print(f"Error on line {i+1}: expected {len(header)} cols, got {len(row)}")
                    print(row)
            print("Done checking.")
    except Exception as e:
        print(f"Exception: {e}")

check_file('DB/Chuong_4_Tiet_1.csv')
check_file('DB/Chuong_5_Tiet_1.csv')

# Writing output to a file to ensure it's captured
with open('debug_out.txt', 'w', encoding='utf-8') as out:
    import sys
    sys.stdout = out
    check_file('DB/Chuong_4_Tiet_1.csv')
    check_file('DB/Chuong_5_Tiet_1.csv')
