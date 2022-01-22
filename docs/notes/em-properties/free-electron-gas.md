---
title: Free electron-gas model
---

## 1D model and density of states

Assume an electron is confined in a infinite square wall, the electron wave function will be

$$ \psi(x) = A_n \sin k_n x $$

where $k_n = n\pi / L$.

density of states is by definition "state per $\Delta k$", and in 1D case it is

$$ D(k) = \frac{\text{number of states per~} \Delta k}{\Delta k} = \frac{2\text{~(spin)}}{\pi / L} $$

### 3D case

$$ D(k) = \frac{2}{(\pi / L)^3} $$

### F-D distribution

Because $E_\text{f} \gg k_\text{B}T$, $f(E) = \mathrm{H}(E-E_\text{f})$ ($H(x)$  is the Heaviside function).

### Number of electrons

1D: $N = k_\text{f} \, D(k)$

3D: $N = D_{k_\text{F}^3} \frac{1}{8} \frac{4}{3}\pi k_\text{F}^3$

### Fermi energy

### Fermi surface

$E(k_\text{f})$

### "*Energy*" density of states

The energy density of states is $D(E)$, $D(E) \propto \sqrt E$

Because $k_n \propto E$, density of states gives $D(E)$ or $D(k)$,

## Electronic energy and electronic specific heat

See also [[lattice specific heat]].

Sommerfeld expansion...?

$$E = \int_0^{\infty} f(\epsilon) D(\epsilon) \,\epsilon \, \mathrm{d}\epsilon \approx \int_0^{E_\mathrm{f}} D(\epsilon) \,\epsilon \, \mathrm{d}\epsilon$$

$$C_V = \frac{\partial E}{\partial T}$$

## References

- Wikipedia contributors. (2021, February 12). Electronic specific heat. In Wikipedia, The Free Encyclopedia. Retrieved 20:09, February 17, 2021, from https://en.wikipedia.org/w/index.php?title=Electronic_specific_heat&oldid=1006278621