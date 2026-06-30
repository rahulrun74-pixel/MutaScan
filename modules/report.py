from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def generate_report(summary, filename="mutascan_report.pdf"):

    c = canvas.Canvas(filename, pagesize=letter)

    c.drawString(100, 750, "MutaScan Report")
    c.drawString(100, 730, f"Substitutions: {summary['Substitution']}")
    c.drawString(100, 710, f"Insertions: {summary['Insertion']}")
    c.drawString(100, 690, f"Deletions: {summary['Deletion']}")
    c.drawString(100, 670, f"Total: {summary['Total']}")

    c.save()

    return filename