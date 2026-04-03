# Sirve esta carpeta en http://127.0.0.1:8080/ (equivalente a serve.cmd).
Set-Location $PSScriptRoot
python -m http.server 8080
