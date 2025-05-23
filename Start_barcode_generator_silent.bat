@echo off
REM Vai nella cartella del progetto
cd /d C:\Users\plusd\Desktop\barcode_generator

REM Attiva l'ambiente virtuale
call venv\Scripts\activate

REM Avvia la webapp in modalità silenziosa
start "" venv\Scripts\pythonw.exe Barcode_Generator.py
