@echo off
echo Chiusura del servizio Barcode Generator...

REM Termina il processo pythonw.exe solo se è legato al tuo progetto
REM ATTENZIONE: chiude TUTTI i pythonw.exe in esecuzione, usa con cautela se ne hai altri in uso

taskkill /f /im pythonw.exe >nul 2>&1

echo Servizio terminato.
pause
