import csv

import pytest

from main import somar, dividir, subtrair


def ler_csv(arquivo_csv):
    dados_csv = []
    try:
        with open(arquivo_csv, newline='') as massa:
            campos = csv.reader(massa, delimiter=',')
            next(campos)
            for linha in campos:
                dados_csv.append(linha)
        return dados_csv
    except FileNotFoundError:
        print(f'Arquivo não encontrado: {arquivo_csv}')
    except Exception as fail:
        print(f'Falha imprevista: {fail}')


def teste_somar():
    numero_a = 8
    numero_b = 7
    resultado_esperado = 15

    resultado_obtido = somar(numero_a, numero_b)

    assert resultado_obtido == resultado_esperado


def teste_dividir_positivo():
    numero_a = 27
    numero_b = 3
    resultado_esperado = 9

    resultado_obtido = dividir(numero_a, numero_b)

    assert resultado_obtido == resultado_esperado




def teste_dividir_negativo():
    numero_a = 27
    numero_b = 0
    resultado_esperado = 'Não dividirás por zero'

    resultado_obtido = dividir(numero_a, numero_b)

    assert resultado_obtido == resultado_esperado


# lista para uso como massa de teste
lista_de_valores = [
    (8, 7, 15),
    (20, 30, 50),
    (25, 0, 25),
    (-5, 12, 7),
    (6, -3, 3)

]


@pytest.mark.parametrize('numero_a, numero_b, resultado_esperado', lista_de_valores)
def teste_somar_leitura_de_lista(numero_a, numero_b, resultado_esperado):
    resultado_obtido = somar(numero_a, numero_b)

    assert resultado_obtido == resultado_esperado


@pytest.mark.parametrize('numero_a, numero_b, resultado_esperado', ler_csv('C:\\Users\\user\\PycharmProjects\\134inicial\\vendors\\csv\\massa_teste_somar_positivo.csv'))
def teste_somar_leitura_de_csv(numero_a, numero_b, resultado_esperado):
    resultado_obtido = somar(int(numero_a), int(numero_b))

    assert resultado_obtido == int(resultado_esperado)

@pytest.mark.parametrize('numero_a, numero_b, resultado_esperado', ler_csv('C:\\Users\\user\\PycharmProjects\\134inicial\\vendors\\csv\\massa_teste_subtrair_positivo.csv'))
def teste_subtrair_leitura_csv(numero_a, numero_b, resultado_esperado):

    resultado_obtido = subtrair(int(numero_a), int(numero_b))

    assert resultado_obtido == int(resultado_esperado)
