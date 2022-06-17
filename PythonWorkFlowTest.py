import numpy as NP
import CoolProp.CoolProp as CP
bongo = NP.ones(3)
h = CP.PropsSI('H', 'P', 101325, 'T', 273.15, 'CO2')
print(h)
