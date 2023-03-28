#=
    problem2
    Copyright © 2023 junyi <junyi@ArchSurface>

    Distributed under terms of the MIT license.
=#

using Roots
using PyCall
using LaTeXStrings

@pyimport matplotlib.pyplot as plt

iszero(small) = small + one(small) ≈ one(small)
λ = 2
θ=π/4

for x=0.1:0.2:3
	f(y) = tan(θ) + (1 - λ^2/y^2)*( (x/y)^2 - 1 + (λ/y)^2/(1+1/y) )*( (x/y)^2 -1 + (λ/y)^2/(1-1/y) ) / ( ((1 - 1/(1-1/y^2))*(x/y)^2 - (1 - (λ/y)^2/(1+1/y))*(1 - (λ/y)^2/(1-1/y) ))*( (x/y)^2 - (1-(λ/y)^2) ) )
	y = find_zeros(f, 0.1, 2.9)
	y = @. y[iszero(f(y))]
	plt.plot(repeat([x], length(y)),y, "ro")
end

plt.show()
