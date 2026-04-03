def filtrar_livros(criterio):
    resultado = []
    livros = criterio["livros"]

    for livro in livros:
        if criterio["Titulo"] != "" and criterio["Titulo"].lower() not in livro["Titulo"].lower():
            continue
        if criterio["Autor"] != "" and criterio["Autor"].lower() not in livro["Autor"].lower():
            continue
        if criterio["Ano"] != []:
            if livro["Ano"] < criterio["Ano"][0] or livro["Ano"] > criterio["Ano"][1]:
                continue
        resultado.append(livro)

    return resultado


livros = [
    {"Titulo": "Harry Potter e a Pedra Filosofal", "Autor": "J.K Rowling", "Ano": 1997},
    {"Titulo": "Harry Potter e a Câmara Secreta", "Autor": "J.K Rowling", "Ano": 1998},
    {"Titulo": "O Hobbit", "Autor": "Tolkien", "Ano": 1937},
    {"Titulo": "Python para Iniciantes", "Autor": "Autor X", "Ano": 2020}
]


if __name__ == "__main__":
    criterio = {
        "Titulo": "Harry Potter",
        "Autor": "J.K Rowling",
        "Ano": [1970, 2000],
        "livros": livros
    }

    resultado = filtrar_livros(criterio)
    print(resultado)
