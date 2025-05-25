from flask import Flask, render_template, request, send_file
import os
import barcode
from barcode.writer import ImageWriter
from io import BytesIO
from PIL import Image
import webbrowser
import threading
import os

app = Flask(__name__)

from flask import redirect, url_for

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        code = request.form["barcode"]
        product_name = request.form.get("product_name", "")
        if code:
            CODE128 = barcode.get_barcode_class("code128")
            barcode_obj = CODE128(code, writer=ImageWriter())
            buffer = BytesIO()
            barcode_obj.write(buffer)
            buffer.seek(0)
            image = Image.open(buffer)
            image.save("static/barcode.png")
            return redirect(url_for('index', product_name=product_name, code=code))
    else:
        product_name = request.args.get("product_name", "")
        code = request.args.get("code", "")
        barcode_path = None
        if code:
            CODE128 = barcode.get_barcode_class("code128")
            barcode_obj = CODE128(code, writer=ImageWriter())
            buffer = BytesIO()
            barcode_obj.write(buffer)
            buffer.seek(0)
            image = Image.open(buffer)
            image.save("static/barcode.png")
            barcode_path = "static/barcode.png"
        return render_template("index.html", barcode_path=barcode_path, product_name=product_name)

@app.route("/print")
def print_pdf():
    from fpdf import FPDF

    product_name = request.args.get("product_name", "")

    pdf = FPDF()
    pdf.add_page()
    if product_name:
        pdf.set_font("Arial", size=12)
        # Center the product name horizontally
        page_width = pdf.w - 2 * pdf.l_margin
        pdf.set_xy(pdf.l_margin, 10)
        pdf.cell(page_width, 10, product_name, ln=True, align='C')
    # Center the barcode image horizontally
    image_width = 100
    x_position = (pdf.w - image_width) / 2
    pdf.image("static/barcode.png", x=x_position, y=20, w=image_width)
    pdf.output("static/barcode.pdf")

    return send_file("static/barcode.pdf", as_attachment=False)

def open_browser():
    webbrowser.open_new("http://127.0.0.1:5050")

if __name__ == "__main__":
    os.makedirs("static", exist_ok=True)
    threading.Timer(1.0, open_browser).start()
    app.run(debug=True, port=5050, use_reloader=False)
