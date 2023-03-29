#=
    problem2
    Copyright © 2023 junyi <junyi@jyxu@mail.ustc.edu.cn>

    Distributed under terms of the MIT license.
=#

using PyCall
using LaTeXStrings

@pyimport matplotlib.pyplot as plt


# %%

using Roots
using PyCall
using LaTeXStrings

@pyimport matplotlib.pyplot as plt

iszero(small) = small + one(small) ≈ one(small)
λ = 2
θ=π/4

for x=0.1:0.2:3
	f(y) = (tan(θ))^2 + (((y^2 - λ^2)*(-x^2*(-1 + y) + y*(-y + y^2 - λ^2))*(-x^2*(1 + y) + y*(y + y^2 - λ^2)))/(y^2*(-x^2 + y^2 - λ^2)*(y^4 + λ^4 + x^2*(1 - y^2 + λ^2) - y^2*(1 + 2*λ^2))))
	y = find_zeros(f, 0.1, 2.9)
	y = @. y[iszero(f(y))]
	plt.plot(repeat([x], length(y)),y, "ro")
end

plt.show()
