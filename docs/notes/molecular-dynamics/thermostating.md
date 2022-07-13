---
title: Thermostating in VASP and LAMMPS
date: 2022-05-22
---

For Nose-Hoover thermostate with NVT simulation:

- In VASP use `fix nvt`.
- In LAMMPS set `MDALGO`, `ISIF`, and `SMASS`.

## References

- [Choice of SMASS for AIMD simulations (vasp.at)](https://www.vasp.at/forum/viewtopic.php?f=4&t=18412)
- [SMASS - Vaspwiki](https://www.vasp.at/wiki/index.php/SMASS)
- [Nose-Hoover thermostat - Vaspwiki](https://www.vasp.at/wiki/index.php/Nose-Hoover_thermostat)
- [Category:Thermostats - Vaspwiki](https://www.vasp.at/wiki/index.php/Category:Thermostats)
- [fix nvt command — LAMMPS documentation](https://docs.lammps.org/fix_nh.html)

