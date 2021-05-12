from docx2pdf import convert

name_file_word = "test"
extension_file_word = ".docx"
extension_file_pdf = ".pdf"


def main():
    route_word = rf"C:\Users\Gianca\Desktop\test\{name_file_word + extension_file_word}"
    route_pdf = rf"C:\Users\Gianca\Desktop\test\{name_file_word + extension_file_pdf}"

    convert(route_word, route_pdf)


if __name__ == '__main__':
    main()
