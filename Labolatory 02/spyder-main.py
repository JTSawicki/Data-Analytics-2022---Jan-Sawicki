# -*- coding: utf-8 -*-
"""
Created on Mon Mar 14 20:08:52 2022

@author: Jasio
"""

from cmdstanpy import CmdStanModel
import pandas as pd
import arviz as az 
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats

bern1 = CmdStanModel(stan_file='code_2.stan')
samp_bern1 = bern1.sample(data={'N':2, 'y':[0,1]}) # Orginalnie 'y':[0,2]