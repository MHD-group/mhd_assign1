#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Created On  : 2023-03-23 06:27
# Last Modified : 2023-03-23 09:05
# Copyright © 2023 myron <yh131996@mail.ustc.edu.cn>
#
# Distributed under terms of the MIT license.

"""
problem3.py
"""

import numpy as np
from numpy import arange, cos, sqrt, sin
from numpy import pi as π
from matplotlib import pyplot as plt


fig, axs = plt.subplots(1,
                        3,
                        figsize=(16, 4))


for (θ, i) in zip([π/24, π/12, π/6], range(3)):
    γ = 5/3
    # s0 is the upstream H relative const
    s0 = 1 - (γ * sin(θ)**2)/(γ - 1)
    s1 = s0 / 2
    s2 = (s0 + 1) / 2
    print(s0, s1, s2)

    hf1 = (2*sin(θ) / (γ - 1))
    hf2 = (1 / (2*(γ - 1) - 0.5 * γ**2 * sin(θ)**2)) * \
            (sin(θ) * (2-γ) * (1 + s1) + \
            2*cos(θ) * sqrt((γ - 1) * (1 - s1)**2 + s1 * γ**2 * sin(θ)**2))
    print(hf1, hf2)

    hf = arange(0, hf1, 0.0001)

    B = (γ/2) * hf * sin(θ) - (1-s2)
    C = 2*sin(θ) - (γ - 1) * hf
    Rx = B**2 + C * (hf + 2*s2*sin(θ))
    # when C == 0
    # hf =
    Xf1 = (B + sqrt(Rx))/C
    axs[i].plot(hf, Xf1, label="Xf⁺/hf S>")

    B = (γ/2) * hf * sin(θ) - (1-s1)
    Rx = B**2 + C * (hf + 2*s1*sin(θ))
    Xf2 = (B + sqrt(Rx))/C
    axs[i].plot(hf, Xf2, label="Xf⁺/hf S<")

    hf = arange(hf1+0.001, hf2, 0.0001)
    B = (γ/2) * hf * sin(θ) - (1-s1)
    C = 2*sin(θ) - (γ - 1) * hf
    Rx = B**2 + C * (hf + 2*s1*sin(θ))
    # when C == 0
    # hf =
    Xf1 = (B + sqrt(Rx))/C
    Xf2 = (B - sqrt(Rx))/C
    axs[i].plot(hf, Xf1, label="Xf⁺/hf S<")
    axs[i].plot(hf, Xf2, label="Xf⁻/hf S<")

    axs[i].set_yscale("log", base=10)
    axs[i].set_ylim(0,1000)
    axs[i].set_title("θ = " + str(int(θ*180/π)) + "°")

plt.show()
axs[2].legend()
#plt.savefig('../figures/problem1.pdf', bbox_inches='tight')
