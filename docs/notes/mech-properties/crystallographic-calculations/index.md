---
title: Crystallographic calculations
---



## Vectors & metric tensors

### Vectors

Direct space vectors or directions are denoted by square brackets, e.g., "$[abc]$"; reciprocal space vectors or planes, are denoted by round brackets, e.g., "$(hkl)$".

### Metric tensors

Metric tensor is a symmetric tensor. The direct space metric tensor is given by

$$
g = \begin{bmatrix}
\mathbf{a}\cdot\mathbf{a} & \mathbf{a}\cdot\mathbf{b} & \mathbf{a}\cdot\mathbf{c} \\
\mathbf{b}\cdot\mathbf{a} & \mathbf{b}\cdot\mathbf{b} & \mathbf{b}\cdot\mathbf{c} \\
\mathbf{c}\cdot\mathbf{a} & \mathbf{c}\cdot\mathbf{b} & \mathbf{c}\cdot\mathbf{c} \\
\end{bmatrix}
$$




## Vector operations

### Dot product

For two direct space vectors $\mathbf{r}$, dot-producting itself is

$$
\mathbf{r} \cdot \mathbf{r} = r_i \, g_{ij} \, r_j
$$

and, for two reciprocal vectors $\mathbf{g}^*$, dot-producting itself is

$$
\mathbf{g}^* \cdot \mathbf{g}^* = g_i \, g^*_{ij} \, g_j
$$

where $g$ and $g^*$ are the direct-space and reciprocal space metric tensors, respectively.

Using dot product, we can calculate:

- The length of the vector: $||\mathbf{r}|| = \sqrt{\mathbf{r} \cdot \mathbf{r}}$
- The angle of the vector
- Distance between the planes

### Cross product

$$
\mathbf{g}^* \times \mathbf{h}^* = \mathbf{t}
$$

The cross product of two direct space vectors is a reciprocal space vector; and the dot product of two reciprocal space vectors is a direct space vector.