Get-Content "<input_filename.txt>" | ForEach-Object {
    if ($_ -match '[a-zA-ZñÑ]+') {
        $matches[0].ToLower()
    }
} | Where-Object {
    $_.Length -gt 3
} | Sort-Object -Unique | Set-Content "<destination_filename.txt>"