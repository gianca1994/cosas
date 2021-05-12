def converter_txt_to_csv(amount_files_txt):
    for i in range(amount_files_txt):
        with open(f"ListaDeEmails/Lista{i + 380}.csv", "w", encoding="UTF-8") as csv:
            with open(f'TXT/{i}.txt', 'r', encoding="UTF-8") as txt:
                for line in txt:
                    csv.write(line.split(":")[0] + "\n")
            txt.close()
        csv.close()



def main():
    converter_txt_to_csv(int(input("Ingrese la cantidad de txt que hay en la carpeta 'TXT':")))


if __name__ == '__main__':
    main()
