from fpdf import FPDF
import pandas as pd


class PDFGenerator:
    def __init__(self, file_path):
        self.pdf = FPDF(orientation="P", unit="mm", format="A4")
        self.df = pd.read_csv(file_path)

    def generate_pdf(self, output_path="output.pdf"):
        for index, row in self.df.iterrows():
            self.pdf.add_page()
            self._add_topic(row["Topic"])
            self._add_pages(row["Pages"] - 1)

        self.pdf.output(output_path)

    def _add_topic(self, topic):
        self.pdf.set_font('Arial', 'B', 24)
        self.pdf.set_text_color(100, 100, 100)
        self.pdf.cell(0, 12, topic, align="L", ln=1)
        self.pdf.line(10, 21, 200, 21)

    def _add_pages(self, num_pages):
        for i in range(num_pages):
            self.pdf.add_page()


if __name__ == "__main__":
    pdf_generator = PDFGenerator("topics.csv")
    pdf_generator.generate_pdf()
