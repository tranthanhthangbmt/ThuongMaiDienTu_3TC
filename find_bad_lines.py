import csv

files = [
    'DB/Chuong_4_Tiet_1.csv',
    'DB/Chuong_4_Tiet_2.csv',
    'DB/Chuong_4_Tiet_3.csv',
    'DB/Chuong_5_Tiet_1.csv',
    'DB/Chuong_5_Tiet_2.csv',
    'DB/Chuong_5_Tiet_3.csv'
]

with open("bad_lines.txt", "w", encoding="utf-8") as out:
    for file in files:
        out.write(f"--- {file} ---\n")
        try:
            with open(file, 'r', encoding='utf-8') as f:
                reader = csv.reader(f)
                header = next(reader)
                for i, row in enumerate(reader, 1):
                    if len(row) != 12:
                        out.write(f"Line {i+1} cols {len(row)}: {','.join(row)}\n")
        except Exception as e:
            out.write(f"Error: {e}\n")
