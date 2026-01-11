# tests/test_utils.py
import pytest 
from src.utils import normalize

@pytest.mark.unit
def test_normalize_basic():
    # Arrange (Preparar los datos)
    input_list = [1, 2, 3]
    expected = [0.0, 0.5, 1.0]
    
    # Act (Ejecutar la función)
    result = normalize(input_list)
    
    # Assert (Verificar el resultado)
    assert result == expected

import pytest # Necesario para approx

def test_normalize_empty():
    """Prueba que una lista vacía no rompa el código"""
    assert normalize([]) == []

def test_normalize_floats():
    """Prueba con decimales usando tolerancia numérica"""
    # Usamos pytest.approx porque los floats pueden tener errores ínfimos de precisión
    result = normalize([1.5, 2.5, 3.5])
    assert result == pytest.approx([0.0, 0.5, 1.0])

@pytest.mark.parametrize("input_list, expected", [
    ([0, 50, 100], [0.0, 0.5, 1.0]),
    ([5, 5, 5], [0.0, 0.0, 0.0]), # Caso de división por cero evitada
    ([10], [0.0]),
])
def test_normalize_parametrized(input_list, expected):
    assert normalize(input_list) == expected