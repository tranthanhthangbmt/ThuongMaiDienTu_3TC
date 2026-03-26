import re
import sys
import traceback

with open('fix_log.txt', 'w', encoding='utf-8') as lg:
    sys.stdout = lg
    sys.stderr = lg

    files = [
        r'D:\MY_CODE\GIFT_to_QTI\ThuongMaiDienTu_3TC\DB\Chuong_4_Tiet_1.csv',
        r'D:\MY_CODE\GIFT_to_QTI\ThuongMaiDienTu_3TC\DB\Chuong_4_Tiet_2.csv',
        r'D:\MY_CODE\GIFT_to_QTI\ThuongMaiDienTu_3TC\DB\Chuong_4_Tiet_3.csv',
        r'D:\MY_CODE\GIFT_to_QTI\ThuongMaiDienTu_3TC\DB\Chuong_5_Tiet_1.csv',
        r'D:\MY_CODE\GIFT_to_QTI\ThuongMaiDienTu_3TC\DB\Chuong_5_Tiet_2.csv',
        r'D:\MY_CODE\GIFT_to_QTI\ThuongMaiDienTu_3TC\DB\Chuong_5_Tiet_3.csv'
    ]

    for file in files:
        print(f"Processing {file}")
        try:
            with open(file, 'r', encoding='utf-8') as f:
                lines = f.readlines()
                
            out = [lines[0].strip()]
            changes = 0
            for line in lines[1:]:
                line = line.strip()
                if not line: continue
                
                match_prefix = re.match(r'^(\d+,(?:Module|Chương)[^,]+,\d+,\d+,)(.*)', line)
                if match_prefix:
                    prefix = match_prefix.group(1)
                    rest = match_prefix.group(2)
                    
                    match_ans = re.search(r',([ABCD]),', rest)
                    if match_ans:
                        left = rest[:match_ans.start()]
                        right = rest[match_ans.end():]
                        ans_letter = match_ans.group(1)
                        
                        tokens = []
                        current = ""
                        in_quote = False
                        for char in left:
                            if char == '"':
                                in_quote = not in_quote
                                current += char
                            elif char == ',' and not in_quote:
                                tokens.append(current)
                                current = ""
                            else:
                                current += char
                        tokens.append(current)
                        
                        if len(tokens) > 5:
                            changes += 1
                            print(f"Found unquoted commas in QuestionContent for token count {len(tokens)}: {left[:20]}...")
                            q_content = ",".join(tokens[:-4])
                            A = tokens[-4]
                            B = tokens[-3]
                            C = tokens[-2]
                            D = tokens[-1]
                            
                            q_content = q_content.replace('"', '""')
                            q_content = f'"{q_content}"'
                            
                            left = f"{q_content},{A},{B},{C},{D}"
                            
                        new_line = f"{prefix}{left},{ans_letter},{right}"
                        out.append(new_line)
                    else:
                        out.append(line)
                else:
                    out.append(line)
                    
            with open(file, 'w', encoding='utf-8') as f:
                f.write('\n'.join(out) + '\n')
            print(f"File {file} saved with {changes} changes.")
                
        except Exception as e:
            print(f"Error on {file}: {e}")
            traceback.print_exc()
