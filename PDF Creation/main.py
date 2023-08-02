from fpdf import FPDF
import pandas as pd

pdf = FPDF(orientation='P', unit='mm', format='A4')
pdf.set_auto_page_break(auto=False, margin=0)
df = pd.read_csv('topics.csv')

for index, row in df.iterrows():
    pdf.add_page()
    pdf.set_font(family="Times", size=14, style='B')
    pdf.cell(w=0, h=12, txt=row['Topic'], align='L', ln=1)
    pdf.line(10, 20, 200, 20)

    for i in range(20, 280, 10):
        pdf.line(10, i, 200, i)

    # Add footer
    pdf.ln(260)
    pdf.set_font(family="arial", size=10, style='I')
    pdf.set_text_color(100, 100, 100)
    pdf.cell(w=0, h=10, txt=row['Topic'], align='R')

    # Add sub pages
    for j in range(row['Pages']-1):
        pdf.add_page()
        pdf.ln(273)
        pdf.set_font(family="arial", size=10, style='I')
        pdf.set_text_color(100, 100, 100)
        pdf.cell(w=0, h=10, txt=row['Topic'], align='R')
        for i in range(20, 280, 10):
            pdf.line(10, i, 200, i)

pdf.output("output.pdf")
