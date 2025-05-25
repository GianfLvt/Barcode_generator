@echo off
REM Avvia app Flask senza mostrare terminale usando pythonw.exe con ambiente virtuale attivo

REM Controlla se la cartella venv esiste; se no, crea l'ambiente virtuale e installa dipendenze
IF NOT EXIST "venv" (
    echo Creazione ambiente virtuale...
    python -m venv venv
    if errorlevel 1 (
        echo Errore nella creazione dell'ambiente virtuale. Assicurati che Python sia installato e nel PATH.
        pause
        exit /b 1
    )
    echo Ambiente virtuale creato.
    echo Installazione dipendenze...
    call venv\Scripts\activate.bat
    python -m pip install --upgrade pip
    pip install flask python-barcode pillow fpdf
    if errorlevel 1 (
        echo Errore nell'installazione delle dipendenze.
        pause
        exit /b 1
    )
    echo Dipendenze installate.
) ELSE (
    echo Ambiente virtuale gia' esistente.
)

REM Attiva l'ambiente virtuale
echo Avvio ambiente virtuale...
call venv\Scripts\activate.bat

REM Avvia l'app con pythonw.exe per non mostrare console
start "" "venv\Scripts\pythonw.exe" "barcode_generator.pyw"

REM Esci dallo script .bat
exit
