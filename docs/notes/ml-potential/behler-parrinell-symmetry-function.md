---
title: Behler–Michele Parrinell symmetry functions
---

## Formulation

Behler & Parrinello (2007):

$$
f_\mathrm{c}(R_{ij}) = \left\{
\begin{aligned}
& \tfrac{1}{2} \, \big[ \cos \big(\tfrac{\pi R_{ij}}{R_\mathrm{c}}\big) + 1 \big] & (R_{ij} \le R_\mathrm{c}) \\
& 0 & (R_{ij} > R_\mathrm{c})
\end{aligned}
\right.
$$


## Applications

- **ANI** (e.g., [TorchANI](https://github.com/aiqm/torchani), [Neurochem](https://github.com/atomistic-ml/neurochem)) uses a heavily modified version of the Behler and Parrinello symmetry functions (Smith et al., 2017).
- [**ænet**](https://github.com/atomisticnet/aenet) use the BP's symmetry functions + smooth overlap of atomic positions (SOAP) approach (Artrith et al., 2017).

## References

- Artrith, N., Urban, A., & Ceder, G. (2017). Efficient and accurate machine-learning interpolation of atomic energies in compositions with many species. *Physical Review B*, *96*(1), 014112. https://doi.org/10.1103/PhysRevB.96.014112
- Behler, J., & Parrinello, M. (2007). Generalized Neural-Network Representation of High-Dimensional Potential-Energy Surfaces. *Physical Review Letters*, *98*(14), 146401. https://doi.org/10.1103/PhysRevLett.98.146401
- Smith, J. S., Isayev, O., & Roitberg, A. E. (2017). ANI-1: An extensible neural network potential with DFT accuracy at force field computational cost. *Chemical Science*, *8*(4), 3192–3203. https://doi.org/10.1039/C6SC05720A