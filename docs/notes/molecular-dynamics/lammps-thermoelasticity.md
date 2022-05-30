---
title: Calculating thermoelasticity with LAMMPS
---

According to [LAMMPS's documentation](https://docs.lammps.org/Howto_elastic.html), there are three ways to compute the thermoelastic tensor in general:

1. The Born-matrix method
2. The stress-strain method
3. The triclinic cell fluctuations that occur in an NPT simulation (seems difficult to converge)

## The Born-matrix method

The elastic stiffness tensor $C_{\alpha\beta\mu\nu}$ is related to the Born matrix tensor $C^\mathrm{B}_{\alpha\beta\mu\nu}$ by (Clavier et al., 2017; Krief & Ashkenazy, 2021)

$$
C_{\alpha \beta \mu \nu}= \left\langle C_{\alpha \beta \mu \nu}^{\mathrm{B}}\right\rangle - \frac{V}{k_{\mathrm{B}} T}\left[\left\langle\sigma_{\alpha \beta}^{\mathrm{B}} \sigma_{\mu \nu}^{\mathrm{B}}\right\rangle-\left\langle\sigma_{\alpha \beta}^{\mathrm{B}}\right\rangle\left\langle\sigma_{\mu \nu}^{\mathrm{B}}\right\rangle\right] + \frac{N k_{\mathrm{B}} T}{V}\left(\delta_{\alpha \mu} \delta_{\beta \nu}+\delta_{\alpha \nu} \delta_{\beta \mu}\right) ,
$$

where $\sigma^\mathrm{B}_{\alpha\beta}$ and $C^\mathrm{B}_{\alpha\beta\gamma\mu}$ are given by

$$
\sigma^\mathrm{B}_{\alpha\beta} = \frac{1}{V}\frac{\partial U}{\partial\epsilon_{\alpha\beta}}
$$

$$
C^\mathrm{B}_{\alpha\beta\gamma\mu} = \frac{1}{V}\frac{\partial^2 U}{\partial\epsilon_{\alpha\beta} \partial\epsilon_{\gamma\mu}} .
$$

In LAMMPS, the Born matrix is calculated using the [`compute born/matrix` command](https://docs.lammps.org/compute_born_matrix.html).





## References

- Clavier, G., Desbiens, N., Bourasseau, E., Lachet, V., Brusselle-Dupend, N., & Rousseau, B. (2017). Computation of elastic constants of solids using molecular simulation: Comparison of constant volume and constant pressure ensemble methods. *Molecular Simulation*, *43*(17), 1413–1422. https://doi.org/10.1080/08927022.2017.1313418
- Krief, M., & Ashkenazy, Y. (2021). Calculation of elastic constants of embedded-atom-model potentials in the N V T ensemble. *Physical Review E*, *103*(6), 063307. https://doi.org/10.1103/PhysRevE.103.063307
- Lutsko, J. F. (1989). Generalized expressions for the calculation of elastic constants by computer simulation. *Journal of Applied Physics*, *65*(8), 2991–2997. https://doi.org/10.1063/1.342716
- Zhen, Y., & Chu, C. (2012). A deformation–fluctuation hybrid method for fast evaluation of elastic constants with many-body potentials. *Computer Physics Communications*, *183*(2), 261–265. https://doi.org/10.1016/j.cpc.2011.09.006
- [8.3.4. Calculate elastic constants — LAMMPS documentation](https://docs.lammps.org/Howto_elastic.html)
- [lammps/examples/ELASTIC_T/BORN_MATRIX/Silicon at develop · lammps/lammps (github.com)](https://github.com/lammps/lammps/tree/develop/examples/ELASTIC_T/BORN_MATRIX/Silicon)

