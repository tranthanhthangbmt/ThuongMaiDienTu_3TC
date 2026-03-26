import re
import os

files = [
    r'D:\MY_CODE\GIFT_to_QTI\ThuongMaiDienTu_3TC\DB\Chuong_4_Tiet_1.csv',
    r'D:\MY_CODE\GIFT_to_QTI\ThuongMaiDienTu_3TC\DB\Chuong_4_Tiet_2.csv',
    r'D:\MY_CODE\GIFT_to_QTI\ThuongMaiDienTu_3TC\DB\Chuong_4_Tiet_3.csv',
    r'D:\MY_CODE\GIFT_to_QTI\ThuongMaiDienTu_3TC\DB\Chuong_5_Tiet_1.csv',
    r'D:\MY_CODE\GIFT_to_QTI\ThuongMaiDienTu_3TC\DB\Chuong_5_Tiet_2.csv',
    r'D:\MY_CODE\GIFT_to_QTI\ThuongMaiDienTu_3TC\DB\Chuong_5_Tiet_3.csv'
]

def quote(s):
    s = s.strip()
    if s and s[0] == '"' and s[-1] == '"':
        return s
    # if it has commas, wrap in quotes
    if ',' in s:
        # replace double quotes inside with """ (escaped)
        s = s.replace('"', '""')
        return f'"{s}"'
    return s

for file in files:
    if not os.path.exists(file):
        continue
        
    with open(file, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        
    out_lines = [lines[0].strip()] # Header
    
    for line in lines[1:]:
        if not line.strip():
            continue
            
        line = line.strip()
        # Find the Answer column (e.g. ,A, , ,B, , ,C, , ,D, )
        match = re.search(r',([ABCD]),', line)
        
        if not match:
            out_lines.append(line)
            continue
            
        # Left of the match
        left = line[:match.start()]
        ans = match.group(1)
        right = line[match.end():]
        
        # In left, we expect: ID, CourseContentId, IdContent, QuestionType, QuestionContent, A, B, C, D
        # Wait, if QuestionContent has commas, I originally wrapped it in quotes, let's hope so.
        # But maybe we can parse left using a smart trick:
        # ID, CourseContentId, 4, 1, 
        
        # Let's just find the first 4 commas (ID, Course, Sub, Type)
        # 1,Module 4. An toàn,4,1,
        # The 5th item is QuestionContent.
        # So first split by comma 4 times.
        parts_1 = left.split(',', 4)
        if len(parts_1) < 5:
            out_lines.append(line)
            continue
            
        id_val = parts_1[0]
        course = parts_1[1]
        id_content = parts_1[2]
        q_type = parts_1[3]
        
        # The rest is QuestionContent, A, B, C, D
        rest = parts_1[4]
        
        # A, B, C, D and QuestionContent.
        # But this is hard if they all have commas.
        # I actually have the raw text generated. It's much easier to just use the LLM to rewrite the files properly.
