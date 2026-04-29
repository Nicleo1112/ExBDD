# language: pt

Funcionalidade: Filtrar livros na biblioteca
  Como um usuário do sistema
  Eu quero filtrar livros por título, autor e ano
  Para encontrar obras específicas rapidamente

  Cenário: Filtrar livros por nome parcial
    Dado que eu tenho uma lista de livros padrão
    Quando eu filtro pelo título "Harry Potter"
    Então o sistema deve retornar 2 livros

  Cenário: Filtrar livros por autor
    Dado que eu tenho uma lista de livros padrão
    Quando eu filtro pelo autor "J.K Rowling"
    Então o sistema deve retornar 2 livros

  Cenário: Filtrar livros por intervalo de anos
    Dado que eu tenho uma lista de livros padrão
    Quando eu filtro pelo intervalo de anos entre 1970 e 2000
    Então o sistema deve retornar 2 livros
