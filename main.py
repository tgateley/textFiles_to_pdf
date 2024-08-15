from fpdf import FPDF
from pathlib import Path
import glob

filepaths = glob.glob("Text_Files/*.txt")
pdf = FPDF(orientation='P', unit="mm", format="A4")
for filepath in filepaths:
    pdf.add_page()
    with open(filepath) as file:
        content = file.read()
    filename = Path(filepath).stem
    name = filename.title()

    pdf.set_font(family="Times", size=16, style="B")
    pdf.cell(w=0, h=8, txt=name, ln=1)

pdf.output("output.pdf")
