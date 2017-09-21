import pytest

import pytuga.lib.tuga_strings as strings

def test_concatenar():

	assert(strings.concatenar('x = ', 2) == 'x = 2')


def test_concatenar_lista():

	assert(strings.concatenar_lista(['a', 'b', 'c', 1, 2, 3]) == 'abc123')


def test_unir_valores():

	assert(strings.unir_valores(', ', 1, 2, 3) == '1, 2, 3')


def test_unir_lista():

	assert(strings.unir_lista(', ', [1, 2, 3]) == '1, 2, 3')


def test_formatar():

	assert(strings.formatar('%i = %.2f', 42, 42) == '42 = 42.00')
	assert(strings.formatar('{0} = {1}', 42, 42) == '42 = 42')

def test_substituir():

	assert(strings.substituir('Olá, pessoal!', 'pessoal', 'mundo') == 'Olá, mundo!')

def test_maiúsculas():

	assert(strings.maiúsculas('olá, mundo!') == 'OLÁ, MUNDO!')

def test_minúsculas():

	assert(strings.minúsculas('OLÁ, MUNDO!') == 'olá, mundo!')




