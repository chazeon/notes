---
title: Least square fitting
---

We want to find the best $x$ that minimizes the error $||Ax-b||^2$.

The bluteforce strategy is to find the solution for the equation $A^TA \hat x = A^Tb$. Multiplying by $A^T$ will remove the error part.

We also acknoledge that $||A \hat x - b||^2 = ||A \hat x - (b-e)||^2 + ||e||^2$.