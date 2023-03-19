#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2023 junyi <junyi@ArchSurface>
#
# Distributed under terms of the MIT license.

import numpy as np
from numpy import arange, cos, sqrt
from numpy import pi as π
from matplotlib import pyplot as plt
"""

"""

k = 2
x = arange(0, 2, 0.01)
ym = x**2 - k**2 * x / (x - 1)
yp = x**2 - k**2 * x / (x + 1)
plt.plot(ym[ym > 0], x[ym > 0])
plt.plot(yp, x)
plt.xlim([0, 3])
# plt.axis("equal")
plt.show()
