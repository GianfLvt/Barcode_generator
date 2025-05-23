from flask import Flask, render_template, request, send_file
import os
import barcode
from barcode.writer import ImageWriter
from io import BytesIO
from PIL import Image

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    barcode_path = None
    if request.method == "POST":
        code = request.form["barcode"]
        if code:
            CODE128 = barcode.get_barcode_class("code128")
            barcode_obj = CODE128(code, writer=ImageWriter())
            buffer = BytesIO()
            barcode_obj.write(buffer)
            buffer.seek(0)
            image = Image.open(buffer)
            image.save("static/barcode.png")
            barcode_path = "static/barcode.png"
    return render_template("index.html", barcode_path=barcode_path)

@app.route("/print")
def print_pdf():
    from fpdf import FPDF

    pdf = FPDF()
    pdf.add_page()
    pdf.image("static/barcode.png", x=10, y=10, w=100)
    pdf.output("static/barcode.pdf")

    return send_file("static/barcode.pdf", as_attachment=False)

if __name__ == "__main__":
    os.makedirs("static", exist_ok=True)
    app.run(debug=True, port=5050)
