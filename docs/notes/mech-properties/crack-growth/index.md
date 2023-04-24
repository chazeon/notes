---
title: Crack growth
---

The Paris equation is given by

$$
\frac{da}{dN} = A \, (\Delta K)^m
$$


where $a(N)$ is the crack length at load $N$. Plug in $\Delta K  = Y\,\Delta\sigma \sqrt{a}$, we have

$$
da = A \, Y^m \Delta\sigma^m \sqrt{a^m} \, dN
$$

integrate this general form, we have:

$$
\begin{split}
N_f = & \int dN = \int^{a_f}_{a_0} (A \, Y^m \Delta\sigma^m \sqrt{a^m})^{-1} \, da \\ 
= & \frac{1}{A \, Y^m \Delta\sigma^m}\left[\bigg(\frac{1}{a_0}\bigg)^\frac{m-2}{2} - \bigg(\frac{1}{a_f}\bigg)^\frac{m-2}{2}\right]
\end{split}
$$

## References

- [Paris' law - Wikipedia](https://en.wikipedia.org/wiki/Paris'_law)