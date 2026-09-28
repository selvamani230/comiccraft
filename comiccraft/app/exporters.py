from fpdf import FPDF
import os, datetime

def save_pdf(layout):
    pdf = FPDF()
    for item in layout:
        pdf.add_page()
        pdf.set_font("Arial", 'B', 16)
        pdf.cell(0, 10, item['title'], ln=True)
        if os.path.exists(item['image_path']):
            pdf.image(item['image_path'], x=10, w=180)
        pdf.set_font("Arial", '', 12)
        pdf.multi_cell(0, 10, item['scene_description'] + "\n" + item['text'])

    os.makedirs("static/exports", exist_ok=True)
    filename = f"static/exports/comic_{datetime.datetime.now().strftime('%Y%m%d%H%M%S')}.pdf"
    pdf.output(filename)
    return filename