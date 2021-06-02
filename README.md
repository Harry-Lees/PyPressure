# PyPressure

A simple pressure conversion library for Python 3.

## Examples

Easy Conversions

```python
>> from pypressure import Pressure
>> pa: float = 25.0
>> psi: float = Pressure.patopsi(pa)
>> psi
0.00362594
```

Simple Math and Comparisons built in

```python
>> from pypressure import Pressure
>> start: Pressure = Pressure.frompsi(55.5)
>> end: Pressure = Pressure.frompsi(50.0)
>> delta_p = start - end
>> delta_p
Pressure(Pa=37921.2, psi=5.5, bar=0.38)
```

For more examples please see the examples folder

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