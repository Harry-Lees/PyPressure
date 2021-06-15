# PyPressure

![Workflow](https://github.com/Harry-Lees/PyPressure/actions/workflows/workflow.yml/badge.svg)
[![Downloads](https://pepy.tech/badge/pypressure)](https://pepy.tech/project/pypressure)

A simple pressure conversion library for Python 3.

## Installation

This project can be installed from PyPi

```python
python3 -m pip install pypressure
```

## Examples

Easy Conversions:

```python
>> from pypressure import Pressure
>> pa: float = 25.0
>> psi: float = Pressure.patopsi(pa)
>> psi
0.003625943443250004
```

Simple Math and Comparisons built in:

```python
>> from pypressure import Pressure
>> start: Pressure = Pressure.frompsi(55.5)
>> end: Pressure = Pressure.frompsi(50.0)
>> delta_p = start - end
>> delta_p
Pressure(pa=37921.165, psi=5.5, bar=0.379)
```

For more examples please see the examples folder.

## Supported Units

Currently the supported units are:
* Bar
* Pounds Per Square Inch (psi)
* Pascals (Pa)

Future Support for:
* Atmospheres (atm)
* Inch of Mercury Column (inHg)
* Kilogram per Centimeter (KgCm)

## License

This project is released under the MIT license.
