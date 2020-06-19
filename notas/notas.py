def notas(lista):
    nova_lista = []
    for nota in lista:
        resto = nota % 5
        arredonda = 5 - resto
        if nota < 38 or nota % 5 == 0 or arredonda >= 3:
            nova_lista.append(nota)
        else:
            nova_lista.append(nota + arredonda)
    return nova_lista



"""
def notas(nota):
    if not 0 < nota < 100:
        return 'Precisa ser uma nota entre 0 e 100'
    else:
        resto = nota % 5
        arredonda = 5 - resto
        if nota < 38 or nota % 5 == 0 or arredonda >= 3:
            return nota
        return nota + arredonda

"""
