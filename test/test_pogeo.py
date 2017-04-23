#!/usr/bin/env python3

from array import array

from pogeo import Location, get_cell_ids, get_distance

cells = get_cell_ids(Location(40.12345, -110.6789))
print(cells)
assert cells == array('Q', [9749833325740032000, 9749833327887515648, 9749833336477450240, 9749833338624933888, 9749833340772417536, 9749833342919901184, 9749833345067384832, 9749833347214868480, 9749833349362352128, 9749833351509835776, 9749833353657319424, 9749833355804803072, 9749833357952286720, 9749833360099770368, 9749833383722090496, 9749833385869574144, 9749833388017057792, 9749833390164541440, 9749833392312025088, 9749833437409181696, 9749833439556665344])

miles = get_distance(Location(-37.12345, 73.6789), Location(-37.54321, 73.9876), 1)
print(miles)
assert 33.596 < miles < 33.598

kilometers = get_distance(Location(.5, .5), Location(-.5, -.5), 2)
print(kilometers)
assert 157.251 < kilometers < 157.254

meters = get_distance(Location(88, 188), Location(89, 189), 3)
print(meters)
assert 111225 < meters < 111231