---
title: OSZICAR
---

## Variable explaination

| Variable | Explaination                                |
| -------- | ------------------------------------------- |
| `T`      | current temperature                         |
| `E`      | total free energy                           |
| `F`      |                                             |
| `E0`     |                                             |
| `EK`     | the kinetic energy                          |
| `SP`     | the potential energy of the Nosé thermostat |
| `SK`     | the corresponding kinetic energy            |

## Parsing

Use [johnkerl/miller (`mlr`)](https://github.com/johnkerl/miller) to parse the [`DKVP`-like](https://miller.readthedocs.io/en/latest/file-formats/#dkvp-key-value-pairs) format and convert it to `CSV`:

```bash
cat OSZICAR | grep T= | awk '{$1= ""; print $0}' | sed -e "s/= /=/g" | sed -e "s/ /,/g" | mlr --ocsv cat > out.csv 
```



## References

- [OSZICAR - Vaspwiki](https://www.vasp.at/wiki/index.php/OSZICAR)