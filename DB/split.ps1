$csv = Import-Csv "MD5.csv" -Encoding UTF8
$csv | Group-Object QuestionType | ForEach-Object {
    $filename = "Chuong_5_Tiet_$($_.Name).csv"
    $_.Group | Export-Csv $filename -NoTypeInformation -Encoding UTF8
}
Write-Host "Done splitting."
