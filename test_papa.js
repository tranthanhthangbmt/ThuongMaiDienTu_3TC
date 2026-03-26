const Papa = require('papaparse');
const fs = require('fs');

const files = ['DB/Chuong_5_Tiet_1.csv', 'DB/Chuong_5_Tiet_2.csv', 'DB/Chuong_5_Tiet_3.csv'];

for (let file of files) {
    console.log(`Testing ${file}`);
    const fileContent = fs.readFileSync(file, 'utf8');
    const res = Papa.parse(fileContent, {
        header: true,
        skipEmptyLines: true
    });
    if (res.errors.length > 0) {
        console.log(`Errors in ${file}:`);
        console.log(JSON.stringify(res.errors, null, 2));
    } else {
        console.log(`No errors in ${file}`);
    }
}
