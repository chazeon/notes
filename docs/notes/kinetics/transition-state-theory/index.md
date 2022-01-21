---
title: Transition state theory
---

![Reaction coordinate, transition state. via [Wikipedia](https://en.wikipedia.org/wiki/Transition_state_theory)](p1.png)

## Target

For a reaction $\ce{A + B -> C}$, the reaction speed is given by

$$ \mathrm{d}[\ce{C}]/\mathrm{d}t = k[\ce{A}][\ce{B}] $$

we want to know the reaction speed constant $k$ as a function of $T$.

## Assumption

Transition state theory assumes at steady state, there is a complex $\ce{AB^\ddag}$ will reach equilibrium with reactant $\ce{A}$ and $\ce{B}$.

$$ \ce{A + B <=> AB^\ddag -> C} $$

## Derivation

From equilibrium condition

$$ K^\ddag = \frac{[\ce{AB^\ddag}]}{[\ce{A}][\ce{B}]} = \exp\left(-\frac{\Delta G^\ddag}{RT}\right) $$

And the rate for product $\ce{C}$ is generation is determined by the speed which $\ce{AB^\ddag}$ decomposes

$$ \mathrm{d}[\ce{C}]/\mathrm{d}t = \nu[\ce{AB^\ddag}] $$

And assume $h\nu = k_BT$.

Then we have the following derivation:

$$ \mathrm{d}[\ce{C}]/\mathrm{d}t = \nu[\ce{AB^\ddag}] = \nu K^\ddag[\ce{A}][\ce{B}] = \frac{k_BT}{h} \exp\left(-\frac{\Delta G^\ddag}{RT}\right)[\ce{A}][\ce{B}] $$

Then we have

$$ k = \frac{k_BT}{h} \exp\left(-\frac{\Delta G^\ddag}{RT}\right) $$
