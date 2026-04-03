@echo off
REM Sirve el sitio estático desde la raíz del repositorio (http://127.0.0.1:8080/).
cd /d "%~dp0"
python -m http.server 8080
