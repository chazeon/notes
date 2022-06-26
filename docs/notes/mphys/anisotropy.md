---
title: Christoffel’s equation and anisotropy
---

## Christoffel’s equation

Given a elastic coefficient matrix $C_{ijkl}$ ($i,j,k,l = 1\text{ to }3$), the velocity $V_P, V_{S1}, V_{S2}$  ($V_P > V_{S1} > V_{S2}$) along the propagation direction $\hat n = (n_1, n_2, n_3)$ is given by the solution of the Christoffer’s equation,

$$
\left| C_{ijkl} n_i n_k - \rho V^{2} \delta_{jl} \right|=0
$$

In other words, the three eigenvalues of the $C_{ijkl} n_i n_k$ matrices are $\rho V_P^2, \rho V_{S1}^2, \rho V_{S2}^2$, which gives the accoustic velocities. Eigenvectors indicate polarization direction.

> In the non-degenerate case, the Christoffel matrix $G$ has three distinct eigenvalues and three corresponding eigenvectors. The eigenvectors represent the polarization vectors of the three wave modes (P and two S) with the corresponding eigenvalues indicating the squared phase velocities v2 of the waves (Sripanich et al., 2017)

### Connections with experimental technique

To obtain full elastic tensor on single crystal samples, measure then fit velocities vs. direction with analytical solution to the Christoffel’s equation (Fan et al., 2015).

## Anisotropy

Azimuthal anisotropies $AV_\text{P}$ and $AV_\text{S}$ measure the variation of acoustic velocity vs. direction, polarization anisotropy $AV_\text{S}^\text{po}$ measures the variation of between shear velocity with different polarization.

They are given by (Karki et al., 2001)

$$ AV_\text{P} = \frac{V_\text{P}^\text{max} - V_\text{P}^\text{min}}{V_\text{P}} $$

$$ AV_\text{S} = \frac{V_\text{S}^\text{max} - V_\text{S}^\text{min}}{V_\text{S}} $$

$$ AV_\text{S}^\text{po} = \frac{V_\text{S1} - V_\text{S2}}{V_\text{S}} $$

## References

- Karki, B. B., Stixrude, L., & Wentzcovitch, R. M. (2001). High-pressure elastic properties of major materials of Earth’s mantle from first principles. *Reviews of Geophysics*, *39*(4), 507–534. https://doi.org/10.1029/2000RG000088
- Fan, D., Mao, Z., Yang, J., & Lin, J.-F. (2015). Determination of the full elastic tensor of single crystals using shear wave velocities by Brillouin spectroscopy. *American Mineralogist*, *100*(11–12), 2590–2601. https://doi.org/10.2138/am-2015-5311
- Sripanich, Y., Fomel, S., Sun, J., & Cheng, J. (2017). Elastic wave-vector decomposition in heterogeneous anisotropic media: Wave-vector decomposition in anisotropic media. *Geophysical Prospecting*, *65*(5), 1231–1245. https://doi.org/10.1111/1365-2478.12482