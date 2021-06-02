from __future__ import annotations
from numbers import Real

class Pressure:
    def __init__(self, pressure: Real) -> None:
        self._p = pressure

    def __add__(self, other) -> Pressure:
        return Pressure(self.pa + other.pa)

    def __mul__(self, other) -> Pressure:
        return Pressure(self.pa * other.pa)

    def __sub__(self, other) -> Pressure:
        return Pressure(self.pa - other.pa)

    def __div__(self, other) -> Pressure:
        return Pressure(self.pa / other.pa)

    def __lt__(self, other) -> bool:
        return self.pa < other.pa

    @classmethod
    def frompsi(cls: Pressure, pressure: Real) -> Pressure:
        return cls(Pressure.psitopa(pressure))

    @classmethod
    def frombar(cls: Pressure, pressure: Real) -> Pressure:
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

    def bartopsi(self, pressure: Real) -> Real:
        return pressure * 14.504

    def bartopa(self, pressure: Real) -> Real:
        return pressure * 100000

    def psitobar(self, pressure: Real) -> Real:
        return pressure / 14.504

    def psitopa(self, pressure: Real) -> Real:
        return pressure * 6895

    def patobar(self, pressure: Real) -> Real:
        return pressure / 100000

    def patopsi(self, pressure: Real) -> Real:
        return pressure / 6895