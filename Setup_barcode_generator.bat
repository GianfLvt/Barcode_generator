@echo off
python -m venv venv
call venv\Scripts\activate
pip install flask python-barcode pillow fpdf
echo Setup completato.
pause
