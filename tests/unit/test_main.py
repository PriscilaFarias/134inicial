from main import somar, dividir


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


