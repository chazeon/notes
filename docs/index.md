---
template: profile.html
title: Welcome!
---

## Bio

I am currently a PhD student (2019–) at the [Applied Physics & Applied Mathematics Department](https://www.apam.columbia.edu/) in [Columbia University](https://www.columbia.edu/). I work as a graduate research assistant with [Professor Renata Wentzcovitch](https://www.apam.columbia.edu/faculty/renata-wentzcovitch).

I got my bachelor degree from [Nanjing University](http://www.nju.edu.cn/) (2013–2017), and master degree from Columbia University (2017–2018).

## Research Focus

My research interests lie broadly around the intersection of physics and computer science. My current research focuses on investigating physical properties of Earth-forming materials under finite pressure and temperature with *ab initio* calculation and  deep-learning potential molecular dynamics.

###  Hydrogen-bond disordering in δ-AlOOH

δ-AlOOH is a high-pressure mineral with a wide stability field. This study investigate the effect of pressure on the hydrogen-bond disorder in δ-AlOOH. Our study suggests the disorder and tunneling of those hydrogen bonds are connected with observed anormalies in earlier experimental and computational studies.

- C. Luo, K. Umemoto, and R. M. Wentzcovitch, [*Ab Initio Investigation of H-Bond Disordering in δ-AlOOH*](https://doi.org/10.1103/PhysRevResearch.4.023223), Phys. Rev. Research 4, 023223 (2022). [[preprint](https://arxiv.org/abs/2112.11369)]
- C. Luo, Y. Sun, and R. M. Wentzcovitch, [*Probing the state of hydrogen in δ-AlOOH at mantle conditions with machine learning potential*](https://doi.org/10.1103/PhysRevResearch.6.013292), Phys. Rev. Research 6, 013292 (2024). [[preprint](https://arxiv.org/abs/2309.06712)]

###  Molecular-dynamics simulations of hydrous phases based on deep-learning potential

Deep-learning potentials enable us to perform large-scale molecular dynamics on GPU-accelerated machines with *ab initio* acuracy. Using these advanced technique, we study various properties that are unique to these hydrous phases (ongoing).

- J. Zeng et al., [DeePMD-Kit v2: A Software Package for Deep Potential Models](https://doi.org/10.1063/5.0155600), The Journal of Chemical Physics (2023). [[preprint](https://arxiv.org/abs/2304.09409)]

### Thermoelasticity

This study introduces the [`cij` Python package](https://github.com/MineralsCloud/cij). This package implements the [SAM-*C<sub>ij</sub>* formalism](https://doi.org/10.1103/PhysRevB.83.184115) that computes the elastic properties of solids under mantle pressure and temperature.

- C. Luo, X. Deng, W. Wang, G. Shukla, Z. Wu, and R. M. Wentzcovitch, [*Cij: A Python Code for Quasiharmonic Thermoelasticity*](https://doi.org/10.1016/j.cpc.2021.108067), Computer Physics Communications (2021). [[preprint](https://arxiv.org/abs/2101.12596)]

### Third-order elastic constants

This study investigates the change in second-order elastic constants under induced stress / strain. Our results show the changes in second-order elastic constants are connected with third-order elastic constants and pressure derivative of second-order elastic constants.

- C. Luo, J. Tromp, and R. Wentzcovitch, [*Ab initio calculations of the third-order elastic coefficients*](https://doi.org/10.1103/PhysRevB.106.214104), Physical Review B (2022). [[preprint](https://arxiv.org/abs/2204.07608)]

### Physical properties of sheet-hydrous minerals

Sheet hydrous minerals are abundant in subduction zones, they exhibit significant anisotropies.

- X. Deng, C. Luo, R. Wentzcovitch, G.A. Abers, Z. Wu, *[Elastic anisotropy of lizardite at subduction zone conditions](https://doi.org/10.1029/2022GL099712)*, Geophysical Research Letters (2022)
- H. Wang, C. Luo, R. Wentzcovitch, *[Ab initio study on the stability and elasticity of brucite]((https://arxiv.org/abs/2311.17268))*, [submitted] [[preprint](https://arxiv.org/abs/2311.17268)]

## Other work

<b class="header">VLab’s Rock property calculator</b> Frontend for [Abers & Hacker (2016)]( https://doi.org/10.1002/2015GC006171)’s MATLAB code, as part of [VLab’s website](http://www.mineralscloud.com/gridsphere/jsp/abershacker/index.jsp).

<b class="header">Phase diagram calculator</b> The [`phdg` Python code](https://github.com/MineralsCloud/phdg) computes phase diagram vs. pressure and temperature based on [`qha`](https://github.com/MineralsCloud/qha)’s Gibbs free enengy results.

<b class="header">The `qha` code</b> The [`qha` ](https://github.com/MineralsCloud/qha) Python package employs the quasi-harmonic approximation (QHA) to compute the thermodynamic properties of crystalline materials at finite pressure and temperature.

