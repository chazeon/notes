---
title: Least-square fitting
---

We want to find the best $x$ that minimizes the error $||Ax-b||^2$.

The brute-force strategy is to find the solution for the equation $A^TA \hat x = A^Tb$. Because $A^TA$ as a [[projection operator]], keeps only the part of $x$ that is representable by the basis vectors from $A$, effectively removing the error $e$:

$$ ||A \hat x - b||^2 = ||A \hat x - (b-e)||^2 + ||e||^2. $$

In Python, least square fitting is done with `numpy.linalg.lstsq`, or `scipy.linalg.lstsq`.

Polynomial fitting (with `numpy.polyfit`) is a special case for least-square fitting, where $A$ is a Vandermonde matrix (`numpy.vander`).