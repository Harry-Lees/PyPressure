import pytest

from pypressure import Pressure

def test_from_pa():
    assert Pressure(100).pa == 100

def test_from_psi():
    assert Pressure.frompsi(100).psi == 100

def test_from_bar():
    assert Pressure.frombar(100).bar == 100

def test_mul():
    assert Pressure(100) * Pressure(100) == Pressure(10000)

def test_add():
    assert Pressure(100) + Pressure(100) == Pressure(200)

def test_lt():
    assert Pressure(100) < Pressure(150)

def test_mt():
    assert Pressure(150) > Pressure(100)

def test_sub():
    assert Pressure(100) - Pressure(100) == Pressure(0)

def test_repr():
    assert Pressure(100).__repr__() == 'Pressure(pa=100, psi=0.015, bar=0.001)'

def test_psi_to_bar():
    assert pytest.approx(Pressure.psitobar(1)) == 0.0689476

def test_psi_to_pa():
    assert pytest.approx(Pressure.psitopa(1)) == 6894.76

def test_pa_to_psi():
    assert pytest.approx(Pressure.patopsi(1)) == 0.0001450377

def test_pa_to_bar():
    assert pytest.approx(Pressure.patobar(1)) == 1e-5

def test_bar_to_psi():
    assert pytest.approx(Pressure.bartopsi(1)) == 14.503773773

def test_bar_to_pa():
    assert pytest.approx(Pressure.bartopa(1)) == 1e5