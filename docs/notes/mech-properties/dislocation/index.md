---
title: Dislocation (1D defects)
---

## Dislocation basics

### Burgers vector, tangent vector, and slip plane

- Burgers vector $\vec b$
- Unit tangent vector $\vec t$
- Edge dislocation $\vec b \perp \vec t$
- Edge dislocation symbol $\perp$
    - Vertical line: half plane, broken bonds
    - Horizontal line: slip plane
- Screw dislocation $\vec b \parallel \vec t$
- The same dislocation shares the same $\vec b$
- Slip plane $\vec b \times \vec t$

![Different types of dislocation. via *Science and Design of Engineering Materials* (p.157)](p1.png)

### Slip system

Usually the highest density plane.

![Slip planes for different crystal systems. via *Science and Design of Engineering Materials* (p.162)](p2.png)

## Force on dislocation: Peach-Koehler formula

Peach-Koehler formula gives us the force on a dislocation line $\vec f_\text{d}$ under a stress field $[\sigma]$.

$$
\frac{\vec f_\text{d}}{\delta l} = (\sigma \cdot \vec b) \times \hat l
$$

### Properties

The shear stress need to have a component in the $\vec b$ direction; then consider the plane, assume pure shear, then $\sigma \, \vec b$ is perpendicular to $\vec b$ because, assume pure shear with a magnitude of $\tau$, we have
$$
\sigma_{ij} \, b_j =  \begin{bmatrix}
0 & \tau \\
\tau & 0 \\
\end{bmatrix} \begin{bmatrix}
b_x \\
b_y \\
\end{bmatrix} = \begin{bmatrix}
\tau\,b_y \\
\tau\,b_x \\
\end{bmatrix}
$$


## Strain, stress, and self-energy of dislocation

With the Peach-Koehler formula, we are able to obtain the force on a dislocation line under a stress field. If we have the stress field of another dislocation, we can calculate the force “between” the two dislocations.

## Strain field, stress field of a dislocation

###  Results

|             | Screw dislocation                                            | Edge dislocation                                             |
| ----------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| Strain      | $\epsilon_{z\theta} = \frac{b}{4\pi}\left(\frac{1}{r}\right)$ |                                                              |
| Stress      | $\sigma_{z\theta} = \frac{Gb}{2\pi}\left(\frac{1}{r}\right)\sigma_{z\theta} = \frac{Gb}{2\pi}\left(\frac{1}{r}\right)\sigma_{z\theta} = \frac{Gb}{2\pi}\left(\frac{1}{r}\right)$ | $\sigma_{z\theta} = \frac{Gb}{2\pi(1-\nu)}\left(\frac{1}{r}\right)$ |
| Self energy | $\frac{Gb^2}{4\pi} \ln\frac{R_\text{max}}{R_\text{c}}$       | $\frac{Gb^2}{4\pi(1-\nu)} \ln\frac{R_\text{max}}{R_\text{c}}$ |

Important points:

1. Stiffer materials have higher dislocation energy, $U_e \propto G$.
2. Comparatively, edge dislocation will have higher energy because of the $\frac{1}{1-\nu}$ term.
3. Strain falls off as $1/r$.

![Elastic energy of a screw dislocation (via Bailey)](p3.jpeg)

## See also

- [[Point defects (0D defects)]], which has more of a thermodynamic aspect.
- *Science and Design of Engineering Materials* has a really good chapter on this topic.
