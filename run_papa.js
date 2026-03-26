const Papa = require('papaparse');
const fs = require('fs');

function checkFile(filename) {
    const fileContent = fs.readFileSync(filename, 'utf8');
    const res = Papa.parse(fileContent, {
        header: true,
        skipEmptyLines: true
    });
    if (res.errors && res.errors.length > 0) {
        console.log(`Errors in ${filename}:`);
        console.log(JSON.stringify(res.errors, null, 2));
    } else {
        console.log(`No errors in ${filename}`);
    }
}

checkFile('DB/Chuong_4_Tiet_1.csv');
checkFile('DB/Chuong_5_Tiet_1.csv');
