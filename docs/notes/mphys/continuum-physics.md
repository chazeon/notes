---
title: Stress, strain, and energy in continuum physics
---

## Deformation in continuum physics

### The deformation of coordinates

$x^I$ gives the referential coordinates, $r^i$ gives the deformed coordinates

$$ x^I \xrightarrow{\text{deform}~F} r^i $$

The deformed coordinates $r^i$ is related to the undeformed coordinates $x^I$ by the deformation matrix $\mathbf{F}$. The components of $\mathbf{F}$ are given by

$$ F_I^i = \frac{\partial r^i}{\partial x^I}. $$

### The deformation of volume

The Jacobian $J$, or what actually more commonly referred to as (volumic) “strain”, $\alpha$, is the determinant of the deformation matrix

$$ J = \det \mathbf{F}. $$

### The deformation of surface

$$ \mathbf{n}^0\,\mathrm{d}\Sigma^0 \xrightarrow{\text{deform } F} \mathbf{n}^t\,\mathrm{d}\Sigma^t $$

### Notations

The uppercase subscripts $\square_{IJKL}$ denote quantities in referential coordinates, whereas the lowercase subscripts $\square_{ijkl}$ denote quantities in the deformed coordinates.

## Stress

### Three definitions of stress

- Lagrangian description of the Cauchy stress $\mathbf{T}^\mathrm{L}$

  $$\mathrm{d}\mathbf{f}^\mathrm{L} = \hat{\mathbf{n}}^t \mathrm{d}\Sigma^t \, \mathbf{T}^\mathrm{L} \quad \text{ or } \quad \mathrm{d}f^\mathrm{L}_I = n^t_j \, \mathrm{d}\Sigma^t \, T^\mathrm{L}_{jI}$$

- Eulerian description of the Cauchy stress $\mathbf{T}^\mathrm{E}$

  $$ \mathrm{d}\mathbf{f}^\mathrm{E} = \hat{\mathbf{n}}^t \mathrm{d}\Sigma^t \, \mathbf{T}^\mathrm{E} \quad \text{ or } \quad \mathrm{d}f^\mathrm{E}_i = n^t_j \, \mathrm{d}\Sigma^t \, T^\mathrm{E}_{ji} $$

- First Piola-Kirchhoff stress $\mathbf{T}^\mathrm{PK}$

  $$ \mathrm{d}\mathbf{f}^\mathrm{E} = \hat{\mathbf{n}}^0 \mathrm{d}\Sigma^0 \, \mathbf{T}^\mathrm{PK} \quad \text{ or } \quad \mathrm{d}f^\mathrm{E}_i = n^0_J \, \mathrm{d}\Sigma^0 \, T^\mathrm{PK}_{Ji} $$

- Second Piola-Kirchhoff stress  $\mathbf{T}^\mathrm{SK}$

  $$ \mathrm{d}\mathbf{f}^\mathrm{L} = \hat{\mathbf{n}}^0 \mathrm{d}\Sigma^0 \, \mathbf{T}^\mathrm{SK} \quad \text{ or } \quad \mathrm{d}f^\mathrm{L}_I = n^0_J \, \mathrm{d}\Sigma^0 \, T^\mathrm{SK}_{JI} $$

### Relations between the three definitions of stress

Because of the [deformation relations](https://www.notion.so/Stress-strain-and-energy-in-continuum-physics-7d00bc0733274a3ab758b3cb88b05aa2), the relations between these definitions can be given.

### Comparison with Birch (1947)

In Birch (1947), Eq. (10) is actually Cauchy stress with this respect, because $\rho = J^{-1}\rho_0$, $\partial a_p / \partial x_r = F_{iI}$

$$T_{rs} = \rho\frac{\partial\phi}{\partial \eta_{pq}} \frac{\partial a_p}{\partial x_r} \frac{\partial a_q}{\partial x_s} \quad \to \quad T_{ij}^\mathrm{L} = J^{-1} \rho_0\frac{\partial\phi}{\partial E_{IJ}} F^I_i F^J_j \quad \text{or} \quad \mathbf{T}^\mathrm{L} = J^{-1} \mathbf{F}\mathbf{T}^\mathrm{SK}\mathbf{F}^\mathrm{T} $$

And Dahlen & Tromp (1998) usually focuses on $\mathbf{T}^\mathrm{SK}$ and $\rho_0\partial\phi/\partial E_{IJ}$.

## Reference

- Birch, F., 1947. Finite Elastic Strain of Cubic Crystals. Phys. Rev. 71, 809–824. https://doi.org/10.1103/PhysRev.71.809
- Dahlen, F.A., Tromp, J., 1998. Theoretical Global Seismology. Princeton University Press.