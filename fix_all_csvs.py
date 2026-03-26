import os
import re

files = [
    r'D:\MY_CODE\GIFT_to_QTI\ThuongMaiDienTu_3TC\DB\Chuong_4_Tiet_1.csv',
    r'D:\MY_CODE\GIFT_to_QTI\ThuongMaiDienTu_3TC\DB\Chuong_4_Tiet_2.csv',
    r'D:\MY_CODE\GIFT_to_QTI\ThuongMaiDienTu_3TC\DB\Chuong_4_Tiet_3.csv',
    r'D:\MY_CODE\GIFT_to_QTI\ThuongMaiDienTu_3TC\DB\Chuong_5_Tiet_1.csv',
    r'D:\MY_CODE\GIFT_to_QTI\ThuongMaiDienTu_3TC\DB\Chuong_5_Tiet_2.csv',
    r'D:\MY_CODE\GIFT_to_QTI\ThuongMaiDienTu_3TC\DB\Chuong_5_Tiet_3.csv'
]

def quote_field(s):
    if not s or s == ',': return s
    if s.startswith('"') and s.endswith('"') and s.count('"') % 2 == 0:
        return s
    if ',' in s:
        s = s.replace('"', '""')
        return f'"{s}"'
    return s

for f in files:
    if not os.path.exists(f): continue
    with open(f, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        
    out = [lines[0].strip()]
    for line in lines[1:]:
        line = line.strip()
        if not line: continue
        
        match = re.search(r',([ABCD]),', line)
        if not match:
            out.append(line)
            continue
            
        ans_letter = match.group(1)
        left = line[:match.start()]
        right = line[match.end():]
        
        p_indices = []
        in_quote = False
        for i, char in enumerate(left):
            if char == '"':
                in_quote = not in_quote
            elif char == ',' and not in_quote:
                p_indices.append(i)
                
        if len(p_indices) >= 8:
            p1 = left[:p_indices[0]]
            p2 = left[p_indices[0]+1:p_indices[1]]
            p3 = left[p_indices[1]+1:p_indices[2]]
            p4 = left[p_indices[2]+1:p_indices[3]]
            
            p5 = left[p_indices[3]+1:p_indices[-4]]
            pA = left[p_indices[-4]+1:p_indices[-3]]
            pB = left[p_indices[-3]+1:p_indices[-2]]
            pC = left[p_indices[-2]+1:p_indices[-1]]
            pD = left[p_indices[-1]+1:]
            
            r_indices = []
            in_quote = False
            for i, char in enumerate(right):
                if char == '"':
                    in_quote = not in_quote
                elif char == ',' and not in_quote:
                    r_indices.append(i)
            
            if r_indices:
                pRA = right[:r_indices[0]]
                pExp = right[r_indices[0]+1:]
            else:
                pRA = right
                pExp = ""
                
            pA = quote_field(pA)
            pB = quote_field(pB)
            pC = quote_field(pC)
            pD = quote_field(pD)
            pRA = quote_field(pRA)
            pExp = quote_field(pExp)
            p5 = quote_field(p5)
            
            new_line = f"{p1},{p2},{p3},{p4},{p5},{pA},{pB},{pC},{pD},{ans_letter},{pRA},{pExp}"
            out.append(new_line)
        else:
            out.append(line)
            
    with open(f, 'w', encoding='utf-8') as fw:
        fw.write('\n'.join(out) + '\n')
