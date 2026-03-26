const fs = require('fs');
const readline = require('readline');

async function splitCSV() {
    const fileStream = fs.createReadStream('D:\\MY_CODE\\GIFT_to_QTI\\ThuongMaiDienTu_3TC\\DB\\MD5.csv', { encoding: 'utf-8' });
    const rl = readline.createInterface({
        input: fileStream,
        crlfDelay: Infinity
    });

    let header = null;
    const files = {};

    for await (const line of rl) {
        if (!line.trim()) continue;
        if (!header) {
            header = line;
            continue;
        }
        
        let cols = [];
        let inQuotes = false;
        let buf = "";
        for (let i = 0; i < line.length; i++) {
            if (line[i] === '"') inQuotes = !inQuotes;
            else if (line[i] === ',' && !inQuotes) {
                cols.push(buf);
                buf = "";
            } else {
                buf += line[i];
            }
        }
        cols.push(buf);
        
        const q_type = cols[3];
        if (!files[q_type]) {
            const fileName = `D:\\MY_CODE\\GIFT_to_QTI\\ThuongMaiDienTu_3TC\\DB\\Chuong_5_Tiet_${q_type}.csv`;
            files[q_type] = fs.createWriteStream(fileName, { encoding: 'utf-8' });
            files[q_type].write(header + '\n');
        }
        files[q_type].write(line + '\n');
    }

    for (const key in files) {
        files[key].end();
    }
    console.log("Done splitting.");
}

splitCSV();
