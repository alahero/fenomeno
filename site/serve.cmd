@echo off
REM Sirve esta carpeta (site) en http://127.0.0.1:8080/ — no uses Stitch Prototype para ver la web.
cd /d "%~dp0"
python -m http.server 8080
