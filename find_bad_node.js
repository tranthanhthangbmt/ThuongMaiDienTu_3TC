const fs = require('fs');
const files = [
    'DB/Chuong_4_Tiet_1.csv',
    'DB/Chuong_4_Tiet_2.csv',
    'DB/Chuong_4_Tiet_3.csv',
    'DB/Chuong_5_Tiet_1.csv',
    'DB/Chuong_5_Tiet_2.csv',
    'DB/Chuong_5_Tiet_3.csv'
];

let out = "";
for (let file of files) {
    if (!fs.existsSync(file)) continue;
    let content = fs.readFileSync(file, 'utf8');
    let lines = content.split('\n');
    out += `--- ${file} ---\n`;
    for (let i = 1; i < lines.length; i++) {
        let line = lines[i].trim();
        if (!line) continue;
        
        // A naive split to see how many fields
        // This is exactly what naive parsers do, but PapaParse handles quotes.
        // Let's just use a simple regex to split by comma outside quotes
        let parts = line.split(/,(?=(?:(?:[^"]*"){2})*[^"]*$)/);
        if (parts.length > 12) {
            out += `Line ${i + 1} (${parts.length} cols): ${line}\n`;
        }
    }
}
fs.writeFileSync('bad_lines.txt', out, 'utf8');
