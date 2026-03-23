import csv

input_file = 'MD4.csv'
output_prefix = 'Chuong_4_Tiet_'

try:
    with open(input_file, 'r', encoding='utf-8') as f_in:
        reader = csv.reader(f_in)
        header = next(reader)
        
        files = {}
        writers = {}
        
        for row in reader:
            if not row: continue
            q_type = row[3] # QuestionType is at index 3
            if q_type not in files:
                file_name = f"{output_prefix}{q_type}.csv"
                files[q_type] = open(file_name, 'w', encoding='utf-8', newline='')
                writers[q_type] = csv.writer(files[q_type])
                writers[q_type].writerow(header)
            writers[q_type].writerow(row)
            
        for f in files.values():
            f.close()
            
    print("Files split successfully.")
except Exception as e:
    print(f"Error: {e}")
