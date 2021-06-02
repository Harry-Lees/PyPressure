from __future__ import annotations
from typing import Type
from numbers import Real

class Pressure:
    def __init__(self, pressure: Real) -> None:
        self._p = pressure

    def __repr__(self, precision=3) -> str:
        return f'Pressure(pa={round(self.pa, precision)}, psi={round(self.psi, precision)}, bar={round(self.bar, precision)})'

    def __add__(self, other: Pressure) -> Pressure:
        return Pressure(self.pa + other.pa)

    def __mul__(self, other: Pressure) -> Pressure:
        return Pressure(self.pa * other.pa)

    def __sub__(self, other: Pressure) -> Pressure:
        return Pressure(self.pa - other.pa)

    def __div__(self, other: Pressure) -> Pressure:
        return Pressure(self.pa / other.pa)

    def __lt__(self, other: Pressure) -> bool:
        return self.pa < other.pa

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Pressure):
            return NotImplemented

        return self.pa == other.pa

    @classmethod
    def frompsi(cls: Type[Pressure], pressure: Real) -> Pressure:
        return cls(Pressure.psitopa(pressure))

    @classmethod
    def frombar(cls: Type[Pressure], pressure: Real) -> Pressure:
        return cls(Pressure.bartopa(pressure))

    @property
    def pa(self) -> Real:
        return self._p

    @pa.setter
    def pa(self, pressure: Real) -> None:
        self._p = pressure

    @property
    def psi(self) -> Real:
        return self.patopsi(self._p)

    @psi.setter
    def psi(self, pressure: Real) -> None:
        self._p = self.psitopa(pressure)

    @property
    def bar(self):
        return self.patobar(self._p)

    @bar.setter
    def bar(self, pressure: Real) -> None:
        self._p = self.bartopa(pressure)

    @staticmethod
    def bartopsi(pressure: Real) -> Real:
        return pressure * 14.503773773

    @staticmethod
    def bartopa(pressure: Real) -> Real:
        return pressure * 100000

    @staticmethod
    def psitobar(pressure: Real) -> Real:
        return pressure / 14.503773773

    @staticmethod
    def psitopa(pressure: Real) -> Real:
        return pressure * 6894.7572931783

    @staticmethod
    def patobar(pressure: Real) -> Real:
        return pressure / 100000

    @staticmethod
    def patopsi(pressure: Real) -> Real:
        return pressure / 6894.7572931783