#!/usr/bin/env python
# encoding: utf-8

name = "Surface_Carbonate_F_CO_Decomposition/groups"
shortDesc = u""
longDesc = u"""
"""

template(reactants=["CarbonateRing","SurfaceSite1","SurfaceSite2"], products=["FX","CO","ORROX"], ownReverse=False)

reverse = "Surface_Carbonate_F_CO_Addition"

#autoGenerated=True
reactantNum=3
productNum=3

recipe(actions=[
    ['BREAK_BOND', '*2', 1, '*3'],
    ['BREAK_BOND', '*2', 1, '*4'],
    ['BREAK_BOND', '*6', 1, '*7'],
    ['FORM_BOND', '*8', 1, '*7'],
    ['FORM_BOND', '*3', 1, '*9'],
    ['CHANGE_BOND', '*4', 1, '*6'],
    ['CHANGE_BOND', '*1', 1, '*2'],
    ['LOSE_PAIR', '*1', '1'],
    ['GAIN_PAIR', '*2', '1'],
])

entry(
    index = 1,
    label = "CarbonateRing",
    group =
"""
1  *1 O u0 p2 {2,D}
2  *2 C u0 p0 {1,D} {3,S} {4,S}
3  *3 O u0 p2 {2,S} {5,S}
4  *4 O u0 p2 {2,S} {6,S}
5  *5 R!H u0 px cx {6,[S,D]} {3,S}
6  *6 R!H u0 px cx {5,[S,D]} {4,S} {7,S}
7  *7 F   u0 p3 c0 {6,S}
""",
    kinetics = None,
)

entry(
    index = 2,
    label = "SurfaceSite1",
    group =
"""
1  *8 Xv  u0 p0 c0
""",
    kinetics = None,
)

entry(
    index = 3,
    label = "SurfaceSite2",
    group =
"""
1  *9 Xv  u0 p0 c0
""",
    kinetics = None,
)


tree(
"""
L1: CarbonateRing
L1: SurfaceSite1
L1: SurfaceSite2
"""
)