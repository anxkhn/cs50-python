from fpdf import FPDF

class PDF():
    def __init__(self, name):
        self._pdf = FPDF()
        self._pdf.add_page()
        self._pdf.set_font("helvetica", size=48)
        self._pdf.cell(w=0, h=64, txt="CS50 Shirtificate",
                       new_x="LMARGIN", new_y="NEXT", align="C")
        self._pdf.image("shirtificate.png", w=self._pdf.epw,
                        alt_text="CS50 Shirtificate")
        self._pdf.set_font_size(32)
        self._pdf.set_text_color(255, 255, 255)
        self._pdf.text(x=48, y=140, txt=f"{name} took CS50")
    def save(self, name):
        self._pdf.output(name)

name = input("Name: ")
pdf = PDF(name)
pdf.save("shirtificate.pdf")