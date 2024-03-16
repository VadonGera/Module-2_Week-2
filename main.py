class InkjetPrinter:

    def print_page(self):
        return f"Документ печатается на струйном принтере."


class LaserPrinter:

    def print_page(self):
        return f"Документ печатается на лазерном принтере."


class Document:
    @staticmethod
    def print_document(printer_type):
        if printer_type == "Inkjet":
            return InkjetPrinter().print_page()
        elif printer_type == "Laser":
            return LaserPrinter().print_page()
        else:
            return "Неизвестный тип принтера."


# Функция, которую будем тестировать
def info_print(printer_type):
    return Document.print_document(printer_type)


if __name__ == "__main__":
    print(info_print("Laser"))
    print(info_print("Ineeeeeeeeeeeeeekjet"))
    print(info_print("Inkjet"))
