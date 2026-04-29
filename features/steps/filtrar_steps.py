from behave import given, when, then
from main import filtrar_livros, livros

@given('que eu tenho uma lista de livros padrão')
def step_impl(context):
    context.lista_livros = livros
    context.criterio = {
        "Titulo": "",
        "Autor": "",
        "Ano": [],
        "livros": context.lista_livros
    }

@when('eu filtro pelo título "{titulo}"')
def step_impl(context, titulo):
    context.criterio["Titulo"] = titulo
    context.resultado = filtrar_livros(context.criterio)

@when('eu filtro pelo autor "{autor}"')
def step_impl(context, autor):
    context.criterio["Autor"] = autor
    context.resultado = filtrar_livros(context.criterio)

@when('eu filtro pelo intervalo de anos entre {inicio:d} e {fim:d}')
def step_impl(context, inicio, fim):
    context.criterio["Ano"] = [inicio, fim]
    context.resultado = filtrar_livros(context.criterio)

@then('o sistema deve retornar {quantidade:d} livros')
def step_impl(context, quantidade):
    assert len(context.resultado) == quantidade
