---
title: Canonical ensemble and partition function
---



## Assumption

- Microstate ID - $i$
- Occupancy - $a_i$
- Energy - $E_i$
- Total energy $E = \sum_i E_i$
- Total occupancy $A = \sum_i a_i$

## Target

We want to find $\{p_i\} = \{p_1,p_2,\dots, p_n\}$ for $i$-th microstates that maximizes maximize entropy $S / K_B = \ln W(a_1,a_2,\dots, a_n)$

$$ W(a_1,a_2,\dots, a_n) = \frac{A!}{\prod_i {a_i!}} $$

## Derivation

Use the [Lagrange multiplier](https://www.notion.so/Lagrange-multiplier-c1d8c2f2daa249a78b30f38a9ac4e56f) method, (note here we have $n$ equations...)

$$ \frac{\partial}{\partial a_i}\left[\ln W(a_1,a_2,\dots, a_n) - \alpha \sum_i a_i - \beta \sum_i a_i E_i)\right] = 0 $$

With Sterling’s approximation, we have

$$ \ln a^*_i - 1 -\alpha - \beta E_i = 0 $$

$$ a_i^* = e^{-(1+\alpha)}e^{-\beta E_i} $$

Then we will have $p_i$

$$ p_i = \frac{a^*_i}{A} = \frac{e^{-(1+\alpha)}e^{-\beta E_i}}{\sum_i  e^{-(1+\alpha)}e^{-\beta E_i}} = \frac{e^{-\beta E_i}}{\sum_i e^{-\beta E_i}} $$

This is also how we get the partition function $Z = e^{-\beta E_i}$.

We will realize that $\beta = 1/k_BT$.

## Other thermodynamic functions

$$ \begin{array}{l}\bar{E}=k T^{2}\left(\frac{\partial \ln Z}{\partial T}\right)*{V, N} \\\bar{P}=-k T\left(\frac{\partial \ln Z}{\partial V}\right)*{T, N} \\S=k T\left(\frac{\partial \ln Z}{\partial T}\right)_{V, N}+k \ln Z \\F=-k T \ln Z\end{array} $$