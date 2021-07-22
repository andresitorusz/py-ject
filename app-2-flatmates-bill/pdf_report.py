import os
import webbrowser

from fpdf import FPDF


class PdfReport:
    """
    Creates a Pdf file that contains data about
    the flatmates such as their names, their due amounts
    and the period of the bill.
    """

    def __init__(self, filename):
        self.filename = filename

    def generate(self, flatmate, co_flatmate, bill):
        flatmate_pay = f"${str(round(flatmate.pays(bill, co_flatmate), 2))}"
        co_flatmate_pay = f"${str(round(co_flatmate.pays(bill, flatmate), 2))}"

        pdf = FPDF(orientation='P', unit='pt', format='A4')
        pdf.add_page()

        # Add icon
        # pdf.image("files/house.png", w=30, h=30)

        # Insert title
        pdf.set_font(family='Times', size=24, style='B')
        pdf.cell(w=0, h=80, txt="Flatmates Bill", border=0, align="C", ln=1)

        # Insert Period label and value
        pdf.set_font(family="Times", size=14, style='B')
        pdf.cell(w=100, h=40, txt=f"Payment for {bill.period}", border=0, ln=1)

        # Insert name and due amount of the first flatmate
        pdf.set_font(family="Times", size=12)
        pdf.cell(w=100, h=25, txt=flatmate.name, border=0)
        pdf.cell(w=150, h=25, txt=flatmate_pay, border=0, ln=1)

        # Insert name and due amount of the first flatmate
        pdf.cell(w=100, h=25, txt=co_flatmate.name, border=0)
        pdf.cell(w=150, h=25, txt=co_flatmate_pay, border=0, ln=1)

        # Change directory to files, generate and open the PDF
        # os.chdir("files")
        pdf.output("output/" + self.filename)
        webbrowser.open("output/" + self.filename)