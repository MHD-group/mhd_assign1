#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Created On  : 2023-03-28 23:50
# Last Modified : 2023-03-29 01:06
# Copyright © 2023 myron <yh131996@mail.ustc.edu.cn>
#
# Distributed under terms of the MIT license.

import numpy as np
from numpy import arange, cos, sqrt, sin, maximum, clip, arctan
from numpy import pi as π
from matplotlib import pyplot as plt

fig, axs = plt.subplots(1,
                        2,
                        figsize=(10, 5))
step = 0.005
x = np.arange(0.1, 6, step)
y = np.arange(0.1, 3, step)

X,Y = np.meshgrid(x, y)

for (λ, i) in zip([0.5, 2], range(2)):
    Z = -(((Y**2 - λ**2)*(-X**2*(-1 + Y) + Y*(-Y + Y**2 - λ**2))*\
            (-X**2*(1 + Y) + Y*(Y + Y**2 - λ**2)))/\
            (Y**2*(-X**2 + Y**2 - λ**2)*(Y**4 + λ**4 + \
            X**2*(1 - Y**2 + λ**2) - Y**2*(1 + 2*λ**2))))

    Z = arctan(sqrt(maximum(0, Z)))
    Z = np.where(Z, Z, np.nan)
    axi = axs[i].contour(X, Y, Z*180/π, linewidth=0.01)
    axi = axs[i].pcolormesh(X, Y, Z*180/π, alpha=0.7)
    axs[i].set_xlabel("$kc/\omega_c$")
    axs[i].set_ylabel("$\omega/\omega_c$")
    axs[i].set_title("$\omega_p/\omega_c = "+str(λ)+"$")
    fig.colorbar(axi, ax = axs[i], label="$\\theta(0°-90°)$")

plt.show()
plt.savefig('../figures/problem2b.pdf', bbox_inches='tight')
