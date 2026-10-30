from calculadora import calcular_disponibilidad

def test_disponibilidad_perfecta():
    assert calcular_disponibilidad(100, 0) == 100.0

def test_disponibilidad_con_caida():
    assert calcular_disponibilidad(100, 10) == 90.0