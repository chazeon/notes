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

- C. Luo, K. Umemoto, and R. M. Wentzcovitch, [*Ab Initio Investigation of H-Bond Disordering in δ-AlOOH*](https://doi.org/10.1103/PhysRevResearch.4.023223), Phys. Rev. Research 4, 023223 (2022). [[preprint](https://arxiv.org/abs/2112.11369), [poster1](files/agu19-alooh.pdf), [poster2](files/esw21-alooh.pdf)]

###  Molecular-dynamics simulations of hydrous phases based on deep-learning potential

Deep-learning potentials enable us to perform large-scale molecular dynamics on GPU-accelerated machines with *ab initio* acuracy. Using these advanced technique, we study various properties that are unique to these hydrous phases (ongoing).

### Thermoelasticity

This study introduces the [`cij`  Python package](https://github.com/MineralsCloud/cij). This package implements the [SAM-*C<sub>ij</sub>* formalism](https://doi.org/10.1103/PhysRevB.83.184115) that computes the elastic properties of solids under mantle pressure and temperature.

- C. Luo, X. Deng, W. Wang, G. Shukla, Z. Wu, and R. M. Wentzcovitch, [*Cij: A Python Code for Quasiharmonic Thermoelasticity*](https://doi.org/10.1016/j.cpc.2021.108067), Computer Physics Communications 108067 (2021). [[preprint](https://arxiv.org/abs/2101.12596)]

### Third-order elastic constants

This study investigates the change in second-order elastic constants under induced stress / strain. Our results show the changes in second-order elastic constants are connected with third-order elastic constants and pressure derivative of second-order elastic constants.

- C. Luo, J. Tromp, and R. Wentzcovitch, [*Ab initio calculations of the third-order elastic coefficients*](https://arxiv.org/abs/2204.07608), (2022). [submitted] [[preprint](https://arxiv.org/abs/2204.07608), [poster](files/agu21-toec.pdf)]

### Physical properties of serpentine minerals

Serpentine is the most abundant water carrier in the Earth’s subducted slab. Lizardite, is a low-temperature variant of serpentine. The large anisotropy in lizardite, as shown in our study, could account for the observed SKS splitting in the trench.

- X. Deng, C. Luo, R. Wentzcovitch, G.A. Abers, Z. Wu, *Elastic anisotropy of lizardite at subduction zone conditions*, (2022). [[poster](https://agu.confex.com/agu/fm21/meetingapp.cgi/Paper/934164), submitted]

## Other work

<b class="header">VLab’s Rock property calculator</b> Frontend for [Abers & Hacker (2016)]( https://doi.org/10.1002/2015GC006171)’s MATLAB code, as part of [VLab’s website](http://www.mineralscloud.com/gridsphere/jsp/abershacker/index.jsp).

<b class="header">Phase diagram calculator</b> The [`phdg` Python code](https://github.com/MineralsCloud/phdg) computes phase diagram vs. pressure and temperature based on [`qha`](https://github.com/MineralsCloud/qha)’s Gibbs free enengy results.

<b class="header">The `qha` code</b> The [`qha` ](https://github.com/MineralsCloud/qha) Python package employs the quasi-harmonic approximation (QHA) to compute the thermodynamic properties of crystalline materials at finite pressure and temperature.

