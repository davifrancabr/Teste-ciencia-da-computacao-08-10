

lista = [5, 42, 12, 9, 73, 51, 22]


def top_tres_maiores(lista: list[int]):
    lista_ordenada = sorted(lista, reverse=True)
    return lista_ordenada[:3]


resultado = top_tres_maiores(lista)
print(resultado)
