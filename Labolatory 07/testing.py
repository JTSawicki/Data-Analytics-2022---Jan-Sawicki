# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np
import arviz as az
from cmdstanpy import CmdStanModel

N = 100

model1 = CmdStanModel(stan_file='code_1.stan')
sample1 = model1.sample({'N': N})

model2 = CmdStanModel(stan_file='code_2.stan')
sample2 = model2.sample({'N': N})

y = sample1.stan_variable('y')
inputY = []
for i in range(y.shape[1]):
    OneY = []
    for j in range(y.shape[0]):
        OneY.append(y[j, i])
    inputY.append(np.mean(OneY))

model3 = CmdStanModel(stan_file='code_3.stan')
sample3 = model3.sample({'N': N, 'y':inputY })

model4 = CmdStanModel(stan_file='code_4.stan')
sample4 = model4.sample({'N': N, 'y': inputY})