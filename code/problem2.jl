#=
    problem2
    Copyright © 2023 junyi <junyi@ArchSurface>

    Distributed under terms of the MIT license.
=#

using PyCall
using LaTeXStrings

@pyimport matplotlib.pyplot as plt


# %%

λ = 2
x = 0.1:0.01:6
x=x'
y = 0.1:0.01:3
z = @. -(((y^2 - λ^2)*(-x^2*(-1 + y) + y*(-y + y^2 - λ^2))*(-x^2*(1 + y) + y*(y + y^2 - λ^2)))/(y^2*(-x^2 + y^2 - λ^2)*(y^4 + λ^4 + x^2*(1 - y^2 + λ^2) - y^2*(1 + 2*λ^2))))

@. z[z <= 0] = NaN
Z=@. atan(sqrt(z))

# plt.pcolormesh(x,y,Z)
plt.contour(x,y,Z)
plt.colorbar()
plt.show()

norm(-1e-13) <= atol
