---
title: OSZICAR
---

## Variables

The table below details the correspondence between `OSZICAR` and `OUTCAR`:

| `OSZICAR` | `OUTCAR`   | Explanation    | Details                                     |
| --------- | ---------- | -------------- | ------------------------------------------- |
| `T`       |            | temperature    | current temperature                         |
| `E`       | `ETOTAL`   | total energy   |                                             |
| `F`       |            |                | total free energy                           |
| `E0`      |            |                | the energy for $\sigma \to 0$               |
| `EK`      | `EKIN`     | kinetic energy |                                             |
| `SP`      | `EPS`      | nose potential | the potential energy of the Nosé thermostat |
| `SK`      | `ES`       | nose kinetic   | the corresponding kinetic energy            |
|           | `EKIN_LAT` | kin. lattice   |                                             |
|           | `TOTEN`    | ion-electron   |                                             |

## Parsing

Use [johnkerl/miller (`mlr`)](https://github.com/johnkerl/miller) to parse the [`DKVP`-like](https://miller.readthedocs.io/en/latest/file-formats/#dkvp-key-value-pairs) format and convert it to `CSV`:

```bash
cat OSZICAR | grep T= | awk '{$1= ""; print $0}' | sed -e "s/= /=/g" | sed -e "s/ /,/g" | mlr --ocsv cat > out.csv 
```



## References

- [OSZICAR - Vaspwiki](https://www.vasp.at/wiki/index.php/OSZICAR)