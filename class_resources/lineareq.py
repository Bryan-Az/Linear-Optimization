# -*- coding: utf-8 -*-
"""
Created on Tue May 12 16:46:29 2020

@author: CHVUPPAL
"""

from pyomo.environ import *
model = ConcreteModel()
model.x = Var( initialize=-1.2, bounds=(-2, 2) )
model.y = Var( initialize= 1.0, bounds=(-2, 2) )


model.limits = ConstraintList()
model.limits.add(model.x + 7 * model.y <= 17.5)
model.limits.add(model.x <= 3.5) 

model.obj = Objective(
expr= model.x + 10 * model.y,
sense= maximize )

SolverFactory('glpk').solve(model, tee=True) and model.display()




