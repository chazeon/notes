---
title: Finite strain equation of states
---

## Finite strain vs. Birch-Murnaghan

### Explicit expression for Birch-Murnaghan equation of states

The explicit expressions for third-order Birch-Murnaghan (BM3) equation of states (EoS) are

$$ E(V)=E^{0}+\tfrac{9}{2} V^{0} \kappa^{0} f^{2}\left[1+f\left(\kappa^{\prime 0}-4\right)\right] $$

$$ P(V)=-\left(\frac{\partial E}{\partial V}\right)_{S}=3 \kappa^{0} f(1+2 f)^{\frac{5}{2}}\left[1+\tfrac{3}{2}\left(\kappa^{\prime 0}-4\right)f\right] $$

where the Eulerian strain $f$ is given by

$$ f \equiv \tfrac{1}{2}\left[\left(V^{0} / V\right)^{\frac{2}{3}}-1\right] \,.$$

### The effect of using of an arbitrary $V_\mathrm{ref}$ instead of $V_0$

Since we have $f=\frac{1}{2}[(V_0/V)^{2/3}-1]$ and we assume $f' \equiv\frac{1}{2}[(V_\mathrm{ref}/V)^{2/3}-1]$, we have

$$ \frac{2f + 1}{2f'+1} = \frac{(V_0/V)^{2/3}}{(V_\mathrm{ref}/V)^{2/3}} = \left(\frac{V_0}{V_\mathrm{ref}}\right)^{2/3} $$

So we have

$$ f = \tfrac{1}{2}\left[(2f'+1)\left(\frac{V_0}{V_\mathrm{ref}}\right)^{2/3} - 1\right] = pf' + q $$

Since $E(V) = a f^3 + bf^2 + d$, we can fit with $f'$

$$ E(V) = a(pf' + q)^3 + b(pf'+q)^2 + d = a'f'^3 + b'f'^2 + c'f' + d' $$

So with an arbitrary $V_\mathrm{ref}$, the fitting result is equivalent.

### Recovering $V_0$, $K_0$, and $K'_0$ from the polynomial coefficients

Suppose the fitted energy is

$$ E(f')=a{f'}^3+b{f'}^2+cf'+d $$

with $f'=\tfrac{1}{2}[(V_\mathrm{ref}/V)^{2/3}-1]$. Define

$$ \Delta\equiv\sqrt{b^2-3ac} \,.$$

For $a\ne0$, the strain at the energy minimum is

$$ f'_0=\frac{-b+\Delta}{3a} \,,$$

because it satisfies $\partial E/\partial f'=0$ and $\partial^2E/\partial {f'}^2=2\Delta>0$. The fit must also give $1+2f'_0>0$ so that the volume is positive. Define

$$ s_0\equiv1+2f'_0 \,.$$

Then the zero-pressure EoS parameters are

$$\boxed{V_0=V_\mathrm{ref}s_0^{-3/2}}$$

$$\boxed{K_0=\frac{2\Delta s_0^2}{9V_0}}$$

and

$$\boxed{K'_0=4+\frac{as_0}{\Delta}} \,.$$

Here $K=-V\,\partial P/\partial V$ and $K'_0=(\partial K/\partial P)_{P=0}$. The constant coefficient $d$ only fixes the energy zero and does not affect $V_0$, $K_0$, or $K'_0$.

If $a=0$, use $f'_0=-c/(2b)$, $K_0=2bs_0^2/(9V_0)$, and $K'_0=4$.

As a check, if $V_\mathrm{ref}=V_0$, then $f'_0=0$ and $c=0$, giving

$$ K_0=\frac{2b}{9V_0}, \qquad K'_0=4+\frac{a}{b} \,.$$

### Analytical derivatives to obtain $P(V)$

Not easy to do, because

$$ P = -\frac{\partial E}{\partial V} = -\frac{\partial E}{\partial f'} \frac{\partial f'}{\partial V} = -(3af'^2 + 2bf' + c)\frac{\partial f'}{\partial V} $$

where

$$ \frac{\partial f'}{\partial V} = -\frac{1}{3}\left(\frac{V_\mathrm{ref}}{V}\right)^{2/3}V^{-1} = -\tfrac{1}{3}(2f'+1)V^{-1} \,.$$

But the expression for $PV$ is a 3rd-order polynomial vs. $f'$,

$$ PV = \tfrac{1}{3} (2f' + 1) (3af'^2 + 2bf' + c) \,. $$

### Gibbs free energy or enthalpy

Usually, these equation of states are for internal energy ($U$), Helmholtz free energy ($F$) as a function of volume $V$. It is also possible to think about the form of enthalpy ($H$), Gibbs free energy ($G$) as a function of strain.

Because

$$\begin{split}
G &= F + PV \,,\\
H &= U + PV \,,
\end{split}$$

assuming $T = 0$, from the above statement, $PV$ is a 3rd-order polynomial of $f'$, it is obvious that $G$ and $H$ will be 3rd order polynomials of $f'$ too.

## References

- [Birch–Murnaghan equation of state - Wikipedia](https://en.wikipedia.org/wiki/Birch–Murnaghan_equation_of_state)
