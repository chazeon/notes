---
title: Bootstrapping my conda environment on local computer
---

## Installing miniconda

### On macOS

Install miniconda using `brew` and deny its auto activation

```bash
brew install miniconda
conda init zsh
conda config --set auto_activate_base false
conda install mamba
```

### On Microsoft Windows

Use the official miniconda installer.

## Setting-up the working environments

### Installing the environments

Save one of the following environment file as `environment.yml` and create it by

```bash
mamba env create -f environments.yml
```

#### The `mphys` environment

```yaml
name: mphys
channels:
  - conda-forge
  - defaults
dependencies:
  - python=3.10
  - matplotlib
  - jupyter
  - ca-certificates
  - openssl
  - scipy
  - certifi
  - pandas
  - tqdm
  - pint
  - sympy
  - yaml
  - pyyaml
```

#### The QHA/Cij environment

The troubling issue with `qha` is its dependency `numba`. Its 1.53 version requires that `numpy<=1.21` and its dependency [`llvmlite` does not compiles on M1 Macs' `arm64` architecture](https://github.com/numba/llvmlite/issues/693). In addition, `scipy` requires OpenBLAS. The most convenient way to is to create a conda environment for it.

```yaml
name: qha
channels:
  - conda-forge
dependencies:
  - python=3.10
  - numba
  - numpy
  - scipy
  - matplotlib
  - pandas
  - pip:
    - qha
    - git+https://github.com/MineralsCloud/cij.git
```

### Exporting a environments

```bash
conda env export --from-history
```

## See also

- [[Install Quantum ESPRESSO via conda]]
- [[Install DeePMD-kit via conda]]