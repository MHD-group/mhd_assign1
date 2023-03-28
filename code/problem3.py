#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Created On  : 2023-03-23 06:27
# Last Modified : 2023-03-29 01:56
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

    # hf1 and hf2 is the plot range of hf
    hf1 = (2*sin(θ) / (γ - 1))
    hf2 = (1 / (2*(γ - 1) - 0.5 * γ**2 * sin(θ)**2)) * \
            (sin(θ) * (2-γ) * (1 + s1) + \
            2*cos(θ) * sqrt((γ - 1) * (1 - s1)**2 + s1 * γ**2 * sin(θ)**2))
    print(hf1, hf2)

    # plot the left part of hf
    hf = arange(0, hf1, 0.00001)

    B = (γ/2) * hf * sin(θ) - (1-s2)
    C = 2*sin(θ) - (γ - 1) * hf
    Rx = B**2 + C * (hf + 2*s2*sin(θ))

    Xf1 = (B + sqrt(Rx))/C
    axs[i].plot(hf, Xf1, label="Xf⁺/hf S>")

    B = (γ/2) * hf * sin(θ) - (1-s1)
    Rx = B**2 + C * (hf + 2*s1*sin(θ))
    Xf2 = (B + sqrt(Rx))/C
    axs[i].plot(hf, Xf2, label="Xf⁺/hf S<")

    # plot the right part of hf
    hf = arange(hf1+0.0001, hf2, 0.0001)
    B = (γ/2) * hf * sin(θ) - (1-s1)
    C = 2*sin(θ) - (γ - 1) * hf
    Rx = B**2 + C * (hf + 2*s1*sin(θ))
    Xf1 = (B + sqrt(Rx))/C
    Xf2 = (B - sqrt(Rx))/C
    axs[i].plot(hf, Xf1, label="$Xf⁺/h_f S<$")
    axs[i].plot(hf, Xf2, label="$Xf⁻/h_f S<$")

    axs[i].set_ylabel("$X^±_f/h_f$  - $log$")
    axs[i].set_xlabel("$h_f$")
    y_max = 1000
    axs[i].set_yscale("log", base=10)
    axs[i].set_ylim(0.1,1000)
#    y_max = 30
#    axs[i].set_ylim(0.1,30)
    axs[i].vlines(hf1, ls = ':', linewidth=1, color='r', label='$\^\^h_f$',alpha=0.8, ymin = 0, ymax = y_max)
    axs[i].vlines(hf2, ls = ':', linewidth=1, label='$\^h_f$',alpha=0.8, ymin = 0, ymax = y_max)
    axs[i].set_title("$θ = " + str(int(θ*180/π)) + "°$")
    axs[i].annotate('$\^h_f$', (hf1, 0.1),
                    fontsize=10,
                    horizontalalignment='center', verticalalignment='bottom')
    axs[i].annotate('$\^\^h_f$', (hf2, 0.1),
                    fontsize=10,
                    horizontalalignment='left', verticalalignment='bottom')

plt.show()
plt.savefig('../figures/problem3_log.pdf', bbox_inches='tight')
