---
title: Finite strain equation of states
---

## Finite strain vs. Birch-Murnaghan

### Explicit expression for Birch-Murnaghan equation of states

The explicit expressions for third-order Birch-Murnaghan equation of states are

$$ E(V)=E^{0}+\tfrac{9}{2} V^{0} \kappa^{0} f^{2}\left[1+f\left(\kappa^{\prime 0}-4\right)\right] $$

$$ P(V)=-\left(\frac{\partial E}{\partial V}\right)_{S}=3 \kappa^{0} f(1+2 f)^{\frac{5}{2}}\left[1+\tfrac{3}{2}\left(\kappa^{\prime 0}-4\right)\right] $$

where the Eulerian strain $f$ is given by

$$ f \equiv \tfrac{1}{2}\left[\left(V^{0} / V\right)^{\frac{2}{3}}-1\right] \,.$$

### The effect of using of an arbitrary $V_\mathrm{ref}$ instead of $V_0$

Since we have $f=\frac{1}{2}[(V_0/V)^{2/3}-1]$ and we assume $f' \equiv\frac{1}{2}[(V_\mathrm{ref}/V)^{2/3}-1]$, we have

$$ \frac{2f + 1}{2f'+1} = \frac{(V_0/V)^{2/3}}{(V_\mathrm{ref}/V)^{2/3}} = \left(\frac{V_0}{V_\mathrm{ref}}\right)^{2/3} $$

So we have

$$ f = \left[(2f'+1)\left(\frac{V_0}{V_\mathrm{ref}}\right)^{2/3} - 1\right] = pf' + q $$

Since $E(V) = a f^3 + bf^2 + d$, we can fit with $f'$

$$ E(V) = a(pf' + q)^3 + b(pf'+q)^2 + d = a'f'^3 + b'f'^2 + c'f' + d' $$

So with an arbitrary $V_\mathrm{ref}$, the fitting result is equivalent.

### Analytical derivatives to obtain $P(V)$

Not easy to do, because

$$ P = -\frac{\partial E}{\partial V} = -\frac{\partial E}{\partial f'} \frac{\partial f'}{\partial V} = -(3af'^2 + 2bf' + c)\frac{\partial f'}{\partial V} $$

where

$$ \frac{\partial f'}{\partial V}  =  \frac{\partial}{\partial V} \left[\left(\frac{V_\mathrm{ref}}{V}\right)^{2/3}-1\right] = -\frac{2}{3} \left(\frac{V_\text{ref}^{2/3}}{V^{5/3}}\right) =  -\frac{2}{3} \left(\frac{V_\mathrm{ref}}{V}\right)^{2/3} V^{-1} = -\tfrac{2}{3} (2f'+1)V^{-1} \,.$$

But the expression for $PV$ is a 3rd-order polynomial vs. $f'$,

$$ PV = \tfrac{2}{3} (2f' + 1) (3af'^2 + 2bf' + c) \,. $$

## References

- [Birch–Murnaghan equation of state - Wikipedia](https://en.wikipedia.org/wiki/Birch–Murnaghan_equation_of_state)

