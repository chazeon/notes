---
title: Phonon non-analytical term correction
tags: [phonon]
---

The **non-analytical term correction** (NAC) corrects the *dynamical matrices* using (Baroni, 2001, p527; Zhang et al., 2022),

$$
\tilde{D}_{\kappa \alpha, \kappa^{\prime} \beta}^{\mathrm{NA}}(\boldsymbol{q})=\frac{4 \pi}{\Omega \sqrt{M_{\kappa} M_{\kappa^{\prime}}}} \frac{\left(\sum_{\gamma} q_{\gamma} Z_{\kappa, \gamma \alpha}^{*}\right)\left(\sum_{\gamma^{\prime}} q_{\gamma^{\prime}} Z_{\kappa^{\prime}, \gamma^{\prime} \beta}^{*}\right)}{\sum_{\alpha \beta} q_{\alpha} \epsilon_{\alpha \beta}^{\infty} q_{\beta}}
$$

where the $Z^*$ denotes the *Born effective charge* and $\epsilon^\infty$ denotes the *dielectric constant*.

In phonopy, this is achieved by performing [a separate VASP run](https://phonopy.github.io/phonopy/vasp.html#non-analytical-term-correction-optional) with [`LEPSILON = .TRUE.`](https://www.vasp.at/wiki/index.php/LEPSILON) and a denser $k$-mesh to calculate the $Z^*$ and $\epsilon^\infty$, then use [`phonopy-vasp-born`](https://phonopy.github.io/phonopy/auxiliary-tools.html#phonopy-vasp-born) to post-process and create a [`BORN`](https://phonopy.github.io/phonopy/input-files.html#born-file) file.

## References

- [Formulations — Phonopy v.2.15.0](https://phonopy.github.io/phonopy/formulation.html#non-analytical-term-correction)
- [Setting tags — Phonopy v.2.15.0](https://phonopy.github.io/phonopy/setting-tags.html#non-analytical-term-correction)
- [Auxiliary tools — Phonopy v.2.15.0](https://phonopy.github.io/phonopy/auxiliary-tools.html#phonopy-vasp-born)
- [VASP & phonopy calculation — Phonopy v.2.15.0](https://phonopy.github.io/phonopy/vasp.html#non-analytical-term-correction-optional)
- [LEPSILON - Vaspwiki](https://www.vasp.at/wiki/index.php/LEPSILON)
- [Ionic contributions to the frequency dependent dielectric function of NaCl - Vaspwiki](https://www.vasp.at/wiki/index.php/Ionic_contributions_to_the_frequency_dependent_dielectric_function_of_NaCl)
- [Phonons & Phonopy: Pro Tips - J. M. Skelton](https://www.researchgate.net/profile/Fatih-Ersan/post/How_can_I_calculate_lattice_thermal_conductivity_using_phonopy_code/attachment/59d6262479197b80779846e1/AS%3A320702106800128%401453472748696/download/phonopy_tips_2014.pdf)
- Baroni, S., de Gironcoli, S., Dal Corso, A., & Giannozzi, P. (2001). Phonons and related crystal properties from density-functional perturbation theory. *Reviews of Modern Physics*, *73*(2), 515–562. https://doi.org/10.1103/RevModPhys.73.515
- Zhang, L., Wang, H., Muniz, M. C., Panagiotopoulos, A. Z., Car, R., & E, W. (2022). A deep potential model with long-range electrostatic interactions. *The Journal of Chemical Physics*, *156*(12), 124107. https://doi.org/10.1063/5.0083669

