import pandas as pd
from fpdf import FPDF
import glob
from pathlib import Path

# Get filepath of the invoice files
filepaths = glob.glob("invoices/*.xlsx")

for filepath in filepaths:
    # Page setup
    pdf = FPDF(orientation="P", unit="mm", format="A4")
    filename = Path(filepath).stem
    invoice_no = filename.split("-")[0]
    invoice_date = filename.split("-")[1]
    pdf.add_page()

    # Add invoice number and date
    pdf.set_font(family="Times", size=16, style="B")
    pdf.cell(w=50, h=8, txt=f"Invoice No. {invoice_no}", ln=1)
    pdf.cell(w=50, h=8, txt=f"Date: {invoice_date}", ln=1)
    pdf.cell(w=0, h=8, txt="", ln=1)

    # Add header
    df = pd.read_excel(filepath, sheet_name="Sheet 1")
    header = list(df.columns)
    header = [item.replace("_", " ").title() for item in header]
    pdf.set_font(family="Times", size=10.5, style="B")
    pdf.set_text_color(0, 0, 0)
    pdf.cell(w=30, h=12, txt=header[0], border=1, align="L")
    pdf.cell(w=65, h=12, txt=header[1], border=1, align="L")
    pdf.cell(w=35, h=12, txt=header[2], border=1, align="L")
    pdf.cell(w=30, h=12, txt=header[3], border=1, align="L")
    pdf.cell(w=30, h=12, txt=header[4], border=1, align="L", ln=1)

    # Add rows
    for index, row in df.iterrows():
        pdf.set_font(family="Times", size=10)
        pdf.set_text_color(80, 80, 80)
        pdf.cell(w=30, h=12, txt=str(row["product_id"]), border=1)
        pdf.cell(w=65, h=12, txt=str(row["product_name"]), border=1)
        pdf.cell(w=35, h=12, txt=str(row["amount_purchased"]), border=1)
        pdf.cell(w=30, h=12, txt=str(row["price_per_unit"]), border=1)
        pdf.cell(w=30, h=12, txt=str(row["total_price"]), border=1, ln=1)

    # Calculate total sum
    total_price = df["total_price"].sum()

    # Display sum in table
    pdf.cell(w=30, h=12, txt="", border=1)
    pdf.cell(w=65, h=12, txt="", border=1)
    pdf.cell(w=35, h=12, txt="", border=1)
    pdf.cell(w=30, h=12, txt="", border=1)
    pdf.cell(w=30, h=12, txt=str(total_price), border=1, ln=1)

    pdf.set_font(family="Times", size=14, style="B")
    pdf.set_text_color(0, 0, 0)
    pdf.cell(w=0, h=8, txt="", ln=1)
    pdf.cell(w=0, h=8, txt="", ln=1)
    pdf.cell(w=30, h=12, txt=f"The total amount due is {total_price} Euros", align="L")

    # Save the pdf file
    pdf.output(f"Pdf/{filename}.pdf")
