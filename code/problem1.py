#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2023 junyi <jyxu@mail.ustc.edu.cn>
#
# Distributed under terms of the MIT license.
"""
problem1.py
"""

import numpy as np
from numpy import arange, cos, sqrt
from numpy import pi as π
from matplotlib import pyplot as plt

θ = arange(0, 2 * π, 0.01)

fig, axs = plt.subplots(1,
                        3,
                        figsize=(16, 4),
                        subplot_kw={'projection': 'polar'})
for (s, i) in zip([0.5, 1, 2], range(3)):
    s_Δ = sqrt((s**2 + 1)**2 - 4 * s**2 * cos(θ)**2)
    bn = np.abs(cos(θ))
    cf = sqrt(0.5 * (s**2 + 1 + s_Δ))
    cs = sqrt(0.5 * (s**2 + 1 - s_Δ))
    axs[i].plot(θ, cf, label="cf/b")
    axs[i].plot(θ, cs, label="cs/b")
    axs[i].plot(θ, bn, label="bn/b")
    axs[i].set_title("s =" + str(s))
# plt.show()
axs[2].legend()
plt.savefig('../figures/problem1.pdf', bbox_inches='tight')
