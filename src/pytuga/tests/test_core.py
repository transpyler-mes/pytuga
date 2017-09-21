import pytest
from pytuga.core import compile, transpile, exec

def test_transpile():
    py = transpile('enquanto verdadeiro ou falso: prosseguir')
    assert py == 'while True or False: pass'
