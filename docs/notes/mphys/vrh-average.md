---
title: Average moduli and velocity of minerals
---



## Mineral aggregate averages

### VRH Bounds

- Voigt bound (upper): $K_\text{Voigt} = \sum n_i K_i$
- Reuss bound (lower): $K_\text{Reuss}^{-1} = \sum n_i K_i^{-1}$
- Voigt-Reuss-Hill Average: $K_\text{Voigt-Reuss-Hill} =  K_\text{Voigt} + K_\text{Reuss}$

### Hashin-Shtrikman (HS) Bounds

## Polycrystalline averages

Bulk / shear moduli from elastic constants ($C_{ij}$) based on polycrystalline averages (Hill, 1952; Watt, 1987).

- $K_\text{V} = [(c_{11}+c_{22}+c_{33}) + 2(c_{12}+c_{23}+c_{31})]/9$
- $K_\text{R} = [(s_{11}+s_{22}+s_{33})+2(s_{12}+s_{23}+s_{31})]^{-1}$
- $K_\text{VRH} = (K_\text{V} + K_\text{R}) / 2$
- $G_\text{V} = [ (c_{11} + c_{22} + c_{33})  -   (c_{12} + c_{23} + c_{31}) + 3 (c_{44} + c_{55} + c_{66}) ] / 15$
- $G_\text{R} = 15 / [4 (s_{11} + s_{22} + s_{33}) - 4 (s_{12} + s_{23} + s_{31}) + 3 (s_{44} + s_{55} + s_{66})]$
- $G_\text{VRH} = (G_\text{V} + G_\text{R}) / 2$

## Acoustic velocity

- Compressional velocity: $V_\mathrm{P} = \sqrt{(K + \frac{3}{4} G)/ \rho}$
- Shear velocity: $V_\mathrm{S} = \sqrt{G / \rho}$
- $V_\phi = \sqrt{K / \rho}$
- $V_\mathrm{P}^2 = V_\mathrm{S}^2 + \frac{3}{4} V_\phi^2$

## References

- Hill, R. (1952). The Elastic Behaviour of a Crystalline Aggregate. *Proceedings of the Physical Society. Section A*, *65*(5), 349–354. https://doi.org/10.1088/0370-1298/65/5/307
- Watt, P. J. (1987). POLYXSTAL: A FORTRAN program to calculate average elastic properties of minerals from single-crystal elasticity data. *Computers & Geosciences*, *13*(5), 441–462. https://doi.org/10.1016/0098-3004(87)90050-1
- Watt, P. J. (1979). Hashin‐Shtrikman bounds on the effective elastic moduli of polycrystals with orthorhombic symmetry. *Journal of Applied Physics*, *50*(10), 6290–6295. https://doi.org/10.1063/1.325768
- [MPtutorial2 (berkeley.edu)](https://seismo.berkeley.edu/wiki_cider/images/8/85/MP2.pdf)
- [Rock physics - SEG Wiki](https://wiki.seg.org/wiki/Rock_physics)
- [Microsoft Word - CijExercise.docx (colorado.edu)](http://ruby.colorado.edu/~smyth/G5700/CijExercise.pdf)
- [The cij calculator cij.core.calculator module — Cij documentation (mineralscloud.github.io)](https://mineralscloud.github.io/cij/api/core/calculator.html)

