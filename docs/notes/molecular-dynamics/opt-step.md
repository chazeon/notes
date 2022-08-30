---
title: VASP’s optimization timestep
---

[Vaspwiki](https://www.vasp.at/wiki/index.php/IBRION) describes the effect of `POTIM` in ionic optimization with the RMM-DIIS method (`IBRION=1`):

> The choice of a reasonable [`POTIM`](https://www.vasp.at/wiki/index.php/POTIM) is also important and can speed up calculations significantly, we recommend to find an optimal [`POTIM`](https://www.vasp.at/wiki/index.php/POTIM) using `IBRION=2` or performing a few test calculations. 

In ionic relaxation with the conjugate gradient algorithm (`IBRION=2`), the stride of optimization step is output as `opt step` in the `OUTCAR`. For example,

```
opt step  =   0.27850  (harmonic =   0.27850) maximal distance =0.00000028
```

## References

- [IBRION - Vaspwiki](https://www.vasp.at/wiki/index.php/IBRION)