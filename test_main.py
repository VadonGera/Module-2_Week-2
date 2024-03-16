from main import info_print


def test_if_info_print():
    assert info_print('fhfghfh') == "Неизвестный тип принтера."
    assert info_print('Inkjet') == "Документ печатается на струйном принтере."
    assert info_print('Laser') == "Документ печатается на лазерном принтере."
