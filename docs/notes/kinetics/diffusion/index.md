---
title: Diffusion
---

## Basics of Diffusion

### Fick’s Law

- Diffusion flux $J = m / (tS)$ (unit: atoms cm<sup>-2</sup> s<sup>-1</sup>)
  - Mass diffusivity, or diffusion coefficient $D$ (unit: cm<sup>2</sup> s<sup>-1</sup>)

#### First law

Also compare electricity: $I = -R dU / dx$

$$J = - D \frac{dC}{dx}$$

#### Second law

Because $dC / dt = - [J(x+dx) - J(x)] / dx = - dJ / dx$, we have

$$ \frac{dC}{dt} = \frac{dD}{dC} \left(\frac{dC}{dx}\right)^2 + D \frac{d^2 C}{dx^2} $$

and when $D \neq D(c)$

$$ \frac{dC}{dt} = D \frac{d^2 C}{dx^2} $$

which means

[...]

## Diffusion and thermodynamics

### Diffusion & chemical potential

The thermodynamic correction term: $1 - M_i RT \frac{\partial \ln \gamma_i}{\partial \ln x_i}$.

Proof: [...]

## Mechanisms

### Atomic mechanisms

#### The random walk derivation of Fick’s first law

[...]

Therefore we have the atomic diffusion factor

$$ D = \frac{1}{6}\,\Gamma\lambda^2 $$

And the following discussions of mechanisms will focus on the expression of jump frequency $\Gamma$.

## Examples: diffusion in different systems

### Diffusion in elemental crystals

Also see the [[point defect]] chapter. The interstitial and vacancy are two main defects in elemental crystals (especially pure metal).

#### Interstitial mechanism

This could also be, carbon particles move in iron.

- Jump frequency $\Gamma = Z f_0 \exp\left(-\Delta G^{\#} / RT\right)$
  - $Z$: jumpable sites
  - $f_0$: intrinsic frequency
- Diffusivity $D = D_0 \exp (-Q / RT)$

#### Vacancy mechanism

- The vacancy mechanism is also called **self-diffusion** in pure metal.
- Jump frequency $\Gamma = ZX_v^ef_0\exp(-\Delta G / RT)$.
  - $X_\text{v}^e$ - equilibrium vacancy concentration
- Diffusivity $D = \frac{1}{6} Z X_\text{v} f_0 \lambda^2 \exp{-\frac{\Delta G}{RT}}$
- For the equilibrium concentration of vacancies $X_{\mathrm{v}}=e^{\bar S_\mathrm{v}^{\mathrm{xs}} / k} e^{-\bar{H}_\mathrm{v} / k T}$ , derivation see the [point defect](https://www.notion.so/Point-defects-1D-defects-5a303859cfdd427dbc3a89eff490b5e4) chapter. Also can be derived from configruational entropy.
- The self-diffusion can be see as the reverse process of vacancy diffusion $D_\text{self} = X_\text{v} D_\text{v}$

#### Biased-random walk, drift velocity: Fick's first law with chemical potential

### Diffusion in substitution alloys

#### Kirkendall effect

The move of boundaries (marked by Mo markers) is the result of the creation and destruction of atomic planes due to inequalities in diffusivities ($D_\ce{Cu} \neq D_\ce{Ni}$).

[...]

#### Darken analysis

**Interdiffusion** coefficient $\tilde D$

$$ \tilde D = X_BD_A + X_AD_B $$

[...]

#### Extended darken analysis

Include thermodynamic correction into the darken analysis.

$$ \tilde D = (X_AD^*_B + X_BD^*_A) \frac{X_AX_B}{RT}\frac{d^2 G}{dX_B^2} $$

This is also the source of up-hill diffusion, which causes [spinodal decomposition](https://www.notion.so/50f1569038604e93b7b8884c24befca7) (automatic separation of phases).

Proof: [...]

### Diffusion in polycrystalline materials: short circuit diffusion

Grain boundary and dislocations have a lower activation energy.

## Temperature effect

Easy to see that jump frequency $\Gamma \propto \exp(-Q/K_BT)$, and $D = \frac{1}{6}\Gamma\lambda^2$, $\ln D = -Q(1/K_BT)$

## Other process Relates to Diffusion

- Nucleation