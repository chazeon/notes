---
title: The DP descriptor
date: 2022-04-28
---



## The vanilla non-smooth DP

### Overview

$$
\ce{
\underset{global coordinate}{$(x,y,z)$} ->[\mathcal{R}][rotation] \underset{local coordinate}{$(x',y',z')$} -> \underset{descriptor}{$\{\mathcal{D}_{ij}\}$}
}
$$

### The descriptor $\{\mathcal{D}_{ij}\}$

- Radial information: $1/r_{ij}$
- Distance info: $(x' / r_{ij}, y' / r_{ij}, z' / r_{ij})$.



![The rotation matrix $\mathcal{R}$ that transforms the global coordinate to the local coordinate in the vanilla non-smooth DP. (Wen et al., 2022)](vanilla-dp.png){ style='max-width: 300px' }

## The smooth DP (DP-SE)

### Overview

A simplified description of the process of constructing the energy is the following:

$$
\ce{\underset{atom environment}{$\mathcal{R}_i$} ->[embedding network] \underset{embeding matrix}{$\mathcal{G}_i$} ->[fitting network] \underset{energy}{$E_i$}}
$$

A more complete depiction can be seen in (Wen et al., 2022) as shown in the following figure:

![The construction of the network (Wen et al., 2022). ](descriptor.png){ style='max-width: 300px' }




## References

- [Atom Type Embedding — DeePMD-kit documentation](https://docs.deepmodeling.com/projects/deepmd/en/master/development/type-embedding.html)
- [DeePMD 描述符 se_a 前向和反向](https://bytedance.feishu.cn/wiki/wikcnfcYL9NA1L1XwnWUMZ0V9jf)
- [deepmd_on_pytorch/model.py at master · shishaochen/deepmd_on_pytorch (github.com)](https://github.com/shishaochen/deepmd_on_pytorch/blob/master/deepmd_pt/model.py)
- Wen, T., Zhang, L., Wang, H., E, W., & Srolovitz, D. J. (2022). Deep Potentials for Materials Science. *ArXiv:2203.00393 [Cond-Mat, Physics:Physics]*. http://arxiv.org/abs/2203.00393
- Zhang, L., Han, J., Wang, H., Saidi, W. A., Car, R., & Weinan, E. (2018). End-to-end symmetry preserving inter-atomic potential energy model for finite and extended systems. *Proceedings of the 32nd International Conference on Neural Information Processing Systems*, 4441–4451. https://arxiv.org/abs/1805.09003
