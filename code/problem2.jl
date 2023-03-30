#=
    problem2
    Copyright © 2023 junyi <junyi@jyxu@mail.ustc.edu.cn>

    Distributed under terms of the MIT license.
=#

using PyCall
using LaTeXStrings

@pyimport matplotlib.pyplot as plt


# %%

λ = 2
# λ = 0.5

x = 0.1:0.01:6
x=x'
y = 0.1:0.01:3

# %%

z = @. -(((y^2 - λ^2)*(-x^2*(-1 + y) + y*(-y + y^2 - λ^2))*(-x^2*(1 + y) + y*(y + y^2 - λ^2)))/(y^2*(-x^2 + y^2 - λ^2)*(y^4 + λ^4 + x^2*(1 - y^2 + λ^2) - y^2*(1 + 2*λ^2))))

@. z[z <= 0] = NaN
Z=@. atan(sqrt(z))
Z*=180/π

# %%
cmap = "gist_rainbow"

img=plt.pcolormesh(x,y,Z, cmap=cmap)
plt.contour(x,y,Z, cmap=cmap)
plt.xlabel(L"$kc/\omega_c$")
plt.ylabel(L"$\omega/\omega_c$")                   
plt.title(L"$\omega_p/\omega_c = " * string(λ) * L"$")
plt.colorbar(img,label=L"$\theta(0°-90°)$")
plt.show()
