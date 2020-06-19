from notas import notas

def test_nota_menor_que_38():
    # assert notas(32) == 32
    # assert notas(12) == 12
    lista = [32, 12]
    assert notas(lista) == lista


# def test_nota_fora_do_range_0_100():
#     assert notas(132) == 'Precisa ser uma nota entre 0 e 100'
#     assert notas(101) == 'Precisa ser uma nota entre 0 e 100'
#     assert notas(-1) == 'Precisa ser uma nota entre 0 e 100'


def test_nota_arredondada():
    # assert notas(73) == 75
    # assert notas(67) == 67
    # assert notas(38) == 40
    lista = [73, 67, 38]
    assert notas(lista) == [75, 67, 40]
