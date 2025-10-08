def criar_pessoa(name: str, age: int, id: int):
    return {'id': id, 'nome': name, 'idade': age, }


gostos = [
    {"id": 1, "gostos": ["Música", "Futebol"]},
    {"id": 2, "gostos": ["Leitura", "Cinema"]},
    {"id": 3, "gostos": ["Viagem"]},
    {"id": 4, "gostos": ["Dança", "Esportes"]},
    {"id": 5, "gostos": ["Tecnologia", "Culinária"]},
    {"id": 6, "gostos": ["Moda"]}
]

pessoas = [
    criar_pessoa('Davi', 19, 1),
    criar_pessoa('Carlos', 21, 2),
    criar_pessoa('Marcos', 22, 3),
    criar_pessoa('Vinicius', 25, 4),
    criar_pessoa('Rogerio', 25, 5),
    criar_pessoa('Arthur', 25, 6)
]


def adicionar_gosto(pessoas: list, gostos: list):
    for pessoa in pessoas:
        print(pessoa)
        for gosto in gostos:
            if pessoa['id'] == gosto['id']:
                pessoa['gostos'] = gosto['gostos']
    return pessoas


resultado = adicionar_gosto(pessoas, gostos)
print(resultado)
