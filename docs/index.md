---
template: profile.html
title: Welcome!
---

## Bio

I am currently a postdoctoral researcher at [Columbia University](https://www.columbia.edu/), following a [Hess Postdoctoral Fellowship](https://geosciences.princeton.edu/research/hessfellowship) at [Princeton University](https://www.princeton.edu/) from 2024–2025.

I received my PhD from Columbia University in 2024, where I worked with [Professor Renata Wentzcovitch](https://www.apam.columbia.edu/faculty/renata-wentzcovitch). I earned my bachelor's degree from [Nanjing University](http://www.nju.edu.cn/) in 2017.

## Research Focus

My research lies at the intersection of mineral physics, computational materials science, and geophysics. I combine *ab initio* calculations, deep-learning molecular dynamics, and thermodynamic modeling to study Earth-forming materials at high pressures and temperatures. I use these mineral-scale insights to understand how compositional and thermal heterogeneity shapes the thermochemical structure of the lower mantle.

###  Hydrogen-bond disordering in δ-AlOOH

δ-AlOOH is a high-pressure hydrous phase capable of transporting water to the lowermost mantle and a model system for hydrogen-bearing minerals at extreme conditions. Using first-principles calculations and machine-learning molecular dynamics, we connect its hydrogen-bond disordering, symmetrization, and proton diffusion with elasticity, acoustic velocities, and spectroscopic signatures. This work establishes a framework for investigating hydrogen behavior and its effects on the physical properties of other complex hydrous phases.

- C. Luo, K. Umemoto, and R. M. Wentzcovitch, [*Ab Initio Investigation of H-Bond Disordering in δ-AlOOH*](https://doi.org/10.1103/PhysRevResearch.4.023223), Phys. Rev. Research 4, 023223 (2022). [[preprint](https://arxiv.org/abs/2112.11369)]
- C. Luo, Y. Sun, and R. M. Wentzcovitch, [*Probing the state of hydrogen in δ-AlOOH at mantle conditions with machine learning potential*](https://doi.org/10.1103/PhysRevResearch.6.013292), Phys. Rev. Research 6, 013292 (2024). [[preprint](https://arxiv.org/abs/2309.06712)]
- C. Luo, Y. Sun, and R. M. Wentzcovitch, [*Elasticity and acoustic velocities of δ-AlOOH at extreme conditions: A methodology assessment*](https://doi.org/10.1103/PhysRevMaterials.8.103601), Phys. Rev. Materials 8, 103601 (2024). [[preprint](https://arxiv.org/abs/2406.13804)]
- C. Luo, S. Lee, H. Wang, Z. Zhang, and R. M. Wentzcovitch, [*Lattice dynamics and the spectroscopic signatures of H-bond disorder in δ-AlOOH*](https://arxiv.org/abs/2606.14590), arXiv:2606.14590 (2026).

### Deep-learning molecular dynamics of hydrous phases

Deep-learning potentials enable large-scale, GPU-accelerated molecular dynamics with *ab initio* accuracy for studying hydrous phases at mantle conditions.

- J. Zeng et al., [DeePMD-Kit v2: A Software Package for Deep Potential Models](https://doi.org/10.1063/5.0155600), The Journal of Chemical Physics (2023). [[preprint](https://arxiv.org/abs/2304.09409)]
- J. Zeng et al., [DeePMD-kit v3: A Multiple-Backend Framework for Machine Learning Potentials](https://doi.org/10.1021/acs.jctc.5c00340), Journal of Chemical Theory and Computation 21, 4375–4385 (2025). [[preprint](https://arxiv.org/abs/2502.19161)]
- J. Zeng et al., [dpdata: A Scalable Python Toolkit for Atomistic Machine Learning Data Sets](https://doi.org/10.1021/acs.jcim.5c01767), Journal of Chemical Information and Modeling 65, 11497–11504 (2025).

### Thermoelasticity

I develop first-principles, deep-learning, and thermodynamic methods to predict the elastic properties of mantle minerals at extreme pressures and temperatures.

- C. Luo, X. Deng, W. Wang, G. Shukla, Z. Wu, and R. M. Wentzcovitch, [*Cij: A Python Code for Quasiharmonic Thermoelasticity*](https://doi.org/10.1016/j.cpc.2021.108067), Computer Physics Communications (2021). [[preprint](https://arxiv.org/abs/2101.12596)]
- C. Luo, J. Tromp, and R. Wentzcovitch, [*Ab initio calculations of the third-order elastic coefficients*](https://doi.org/10.1103/PhysRevB.106.214104), Physical Review B (2022). [[preprint](https://arxiv.org/abs/2204.07608)]
- T. Wan, C. Luo, Y. Sun, and R. M. Wentzcovitch, [*Thermoelastic properties of bridgmanite using deep-potential molecular dynamics*](https://doi.org/10.1103/PhysRevB.109.094101), Phys. Rev. B 109, 094101 (2024). [[preprint](https://arxiv.org/abs/2307.07127)]
- T. Wan, C. Luo, Z. Zhang, Y. Sun, and R. M. Wentzcovitch, [*Ferroelastic hysteresis, shear modulus softening, and the tetragonal↔cubic transition in davemaoite*](https://doi.org/10.1126/sciadv.aed7601), Science Advances 12, eaed7601 (2026). [[preprint](https://arxiv.org/abs/2505.01529)]

### Physical properties of sheet-hydrous minerals

Using first-principles and machine-learning methods, we study how the stability, elasticity, and anisotropy of serpentines and brucite shape water transport and seismic signatures in subduction zones.

- X. Deng, C. Luo, R. Wentzcovitch, G.A. Abers, Z. Wu, *[Elastic anisotropy of lizardite at subduction zone conditions](https://doi.org/10.1029/2022GL099712)*, Geophysical Research Letters (2022) [[preprint](https://arxiv.org/abs/2209.09783)]
- H. Wang, C. Luo, and R. M. Wentzcovitch, [*Machine learning potential for serpentines*](https://doi.org/10.1029/2024JH000434), Journal of Geophysical Research: Machine Learning and Computation 1, e2024JH000434 (2024).
- H. Wang, C. Luo, and R. M. Wentzcovitch, [*Ab initio study of the stability and elasticity of brucite*](https://doi.org/10.1103/PhysRevB.109.214103), Phys. Rev. B 109, 214103 (2024). [[preprint](https://arxiv.org/abs/2311.17268)]

## Other work

<b class="header">VLab’s Rock property calculator</b> Frontend for [Abers & Hacker (2016)]( https://doi.org/10.1002/2015GC006171)’s MATLAB code, as part of [VLab’s website](http://www.mineralscloud.com/gridsphere/jsp/abershacker/index.jsp).

<b class="header">Phase diagram calculator</b> The [`phdg` Python code](https://github.com/MineralsCloud/phdg) computes phase diagram vs. pressure and temperature based on [`qha`](https://github.com/MineralsCloud/qha)’s Gibbs free enengy results.

<b class="header">The `qha` code</b> The [`qha` ](https://github.com/MineralsCloud/qha) Python package employs the quasi-harmonic approximation (QHA) to compute the thermodynamic properties of crystalline materials at finite pressure and temperature.
