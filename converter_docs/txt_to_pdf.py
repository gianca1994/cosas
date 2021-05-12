from fpdf import FPDF


def main():
    name_file_txt = "test"
    extension_file_text = ".txt"
    extension_file_pdf = ".pdf"

    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    file_txt = open(name_file_txt + extension_file_text, "r")

    for line in file_txt:
        pdf.cell(200, 10, txt=line, ln=1)

    pdf.output(name_file_txt + extension_file_pdf)


if __name__ == '__main__':
    main()
