from main import filtrar_livros, livros


def teste_filtrar_por_nome():
    criterio = {"Titulo": "Harry Potter", "Autor": "", "Ano": [], "livros": livros}
    resultado = filtrar_livros(criterio)
    assert len(resultado) == 2


def teste_filtrar_por_autor():
    criterio = {"Titulo": "", "Autor": "J.K Rowling", "Ano": [], "livros": livros}
    resultado = filtrar_livros(criterio)
    assert len(resultado) == 2


def teste_filtrar_por_ano():
    criterio = {"Titulo": "", "Autor": "", "Ano": [1970, 2000], "livros": livros}
    resultado = filtrar_livros(criterio)
    assert len(resultado) == 2


def teste_filtrar_combinado():
    criterio = {"Titulo": "Harry Potter", "Autor": "J.K Rowling", "Ano": [1970, 2000], "livros": livros}
    resultado = filtrar_livros(criterio)
    assert len(resultado) == 2


if __name__ == "__main__":
    teste_filtrar_por_nome()
    teste_filtrar_por_autor()
    teste_filtrar_por_ano()
    teste_filtrar_combinado()
    print("Todos os testes passaram")
