import re

files = [
    r'D:\MY_CODE\GIFT_to_QTI\ThuongMaiDienTu_3TC\DB\Chuong_4_Tiet_1.csv',
    r'D:\MY_CODE\GIFT_to_QTI\ThuongMaiDienTu_3TC\DB\Chuong_4_Tiet_2.csv',
    r'D:\MY_CODE\GIFT_to_QTI\ThuongMaiDienTu_3TC\DB\Chuong_4_Tiet_3.csv',
    r'D:\MY_CODE\GIFT_to_QTI\ThuongMaiDienTu_3TC\DB\Chuong_5_Tiet_1.csv',
    r'D:\MY_CODE\GIFT_to_QTI\ThuongMaiDienTu_3TC\DB\Chuong_5_Tiet_2.csv',
    r'D:\MY_CODE\GIFT_to_QTI\ThuongMaiDienTu_3TC\DB\Chuong_5_Tiet_3.csv'
]

# We will read each line. If the 5th field is not quoted, and there's a comma, it breaks CSV.
# We know the first 4 fields are digits and simple text, e.g. `1,Module 4. An toàn,4,1,`
# So we can match `^(\d+,[^,]+,\d+,\d+,)`
for file in files:
    try:
        with open(file, 'r', encoding='utf-8') as f:
            lines = f.readlines()
            
        out = [lines[0].strip()]
        for line in lines[1:]:
            line = line.strip()
            if not line: continue
            
            # match the prefix: id, module, idcontent, type
            match_prefix = re.match(r'^(\d+,(?:Module|Chương)[^,]+,\d+,\d+,)(.*)', line)
            if match_prefix:
                prefix = match_prefix.group(1)
                rest = match_prefix.group(2)
                
                # Now we need to find QuestionContent.
                # It is the text up to the 4 choices.
                # We know the answers A,B,C,D are followed by the AnswerLetter (A|B|C|D), ResultAnswer, Explanation.
                # Let's search from the right!
                # ResultAnswer and Explanation are the last two. They might be quoted if they have commas.
                # To be absolutely sure, it's easier to find the `,[ABCD],` token.
                match_ans = re.search(r',([ABCD]),', rest)
                if match_ans:
                    left = rest[:match_ans.start()]
                    right = rest[match_ans.end():]
                    ans_letter = match_ans.group(1)
                    
                    # 'left' contains QuestionContent, A, B, C, D
                    # A,B,C,D are the last 4 comma-separated values.
                    # HOWEVER, they might be quoted if they have commas.
                    # We can use csv module to parse 'left' if we do it backwards? No.
                    # Let's write a simple parser that correctly tokenizes 'left':
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
                    
                    # We expect QuestionContent, A, B, C, D -> 5 tokens!
                    # If there are MORE than 5 tokens, it means QuestionContent was NOT quoted and contains commas!
                    if len(tokens) > 5:
                        # The last 4 tokens are definitely A, B, C, D (unless they had unquoted commas, which we fixed earlier!)
                        # Wait, if they had unquoted commas, my earlier script quoted them, so they are now 1 token each!
                        # This means ANY extra tokens must belong to QuestionContent!
                        q_content = ",".join(tokens[:-4])
                        A = tokens[-4]
                        B = tokens[-3]
                        C = tokens[-2]
                        D = tokens[-1]
                        
                        # Quote Q_content!
                        q_content = q_content.replace('"', '""')
                        q_content = f'"{q_content}"'
                        
                        # Reconstruct left
                        left = f"{q_content},{A},{B},{C},{D}"
                        
                    new_line = f"{prefix}{left},{ans_letter},{right}"
                    out.append(new_line)
                else:
                    out.append(line)
            else:
                out.append(line)
                
        with open(file, 'w', encoding='utf-8') as f:
            f.write('\n'.join(out) + '\n')
            
    except Exception as e:
        print(f"Error on {file}: {e}")
