---
title: Install DeePMD-kit via conda
---

## Building the conda environment

To install the GPU-enabled version, prepare the following `environment.yml` file:

```yaml
name: dpmd

channels:
  - deepmodeling
  - nvidia
  - conda-forge

dependencies:

  - python=3.9

  - cudatoolkit=11.3
  - deepmd-kit=*[build=*gpu]
  - libdeepmd=*[build=*gpu]
  - lammps-dp
  - horovod
```

And construct the environment at `./env` from the `environment.yml` by

```bash
conda env create \
    -f environment.yml \    # Name of the environment YAML spec
    -p $(pwd)/env           # Location for the environment to be created
```

After the environment construction is finished, you can enter the conda environment by

```bash
conda activate $(pwd)/env
```

## Additional notes

### GPU dependency

To install the GPU-enabled version, one need to have the GPUs and CUDA library available at the time the environment is being built because of the `__cuda`  virtual package dependency. This can be avoided by [specifying `CONDA_OVERRIDE_CUDA=""` environment](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-virtual.html#overriding-detected-packages) at install time, but CUDA is still required upon running the program. (See also [\[BUG\] Conda (CUDA) & TF 2.7 · Issue #1362 · deepmodeling/deepmd-kit (github.com)](https://github.com/deepmodeling/deepmd-kit/issues/1362)).

You can chcek the output of `conda info` for whether the virtual dependency `__cuda` is present to see if CUDA is properly installed and recognized, e.g.,

```
(base) [chazeon@exp-7-60 test-dpmd]$ conda info

     active environment : base
    active env location : /cm/shared/apps/spack/cpu/opt/spack/linux-centos8-zen2/gcc-10.2.0/anaconda3-2020.11-weucuj4yrdybcuqro5v3mvuq3po7rhjt
            shell level : 1
       user config file : /home/chazeon/.condarc
 populated config files :
          conda version : 4.9.2
    conda-build version : 3.20.5
         python version : 3.8.5.final.0
       virtual packages : __cuda=11.2=0
                          __glibc=2.28=0
                          __unix=0=0
                          __archspec=1=x86_64
       base environment : /cm/shared/apps/spack/cpu/opt/spack/linux-centos8-zen2/gcc-10.2.0/anaconda3-2020.11-weucuj4yrdybcuqro5v3mvuq3po7rhjt  (read only)
           channel URLs : https://repo.anaconda.com/pkgs/main/linux-64
                          https://repo.anaconda.com/pkgs/main/noarch
                          https://repo.anaconda.com/pkgs/r/linux-64
                          https://repo.anaconda.com/pkgs/r/noarch
          package cache : /cm/shared/apps/spack/cpu/opt/spack/linux-centos8-zen2/gcc-10.2.0/anaconda3-2020.11-weucuj4yrdybcuqro5v3mvuq3po7rhjt/pkgs
                          /home/chazeon/.conda/pkgs
       envs directories : /home/chazeon/.conda/envs
                          /cm/shared/apps/spack/cpu/opt/spack/linux-centos8-zen2/gcc-10.2.0/anaconda3-2020.11-weucuj4yrdybcuqro5v3mvuq3po7rhjt/envs
               platform : linux-64
             user-agent : conda/4.9.2 requests/2.24.0 CPython/3.8.5 Linux/4.18.0-147.el8.x86_64 centos/8.1.1911 glibc/2.28
                UID:GID : 520832:10478
             netrc file : None
           offline mode : False
```

### `conda` vs. `mamba`

[`mamba`](<https://github.com/mamba-org/mamba>) is a drop-in replacement of `conda` written in C with compatible CLI interface, only faster

- “parallel downloading of repository data and package files using multi-threading”
- “libsolv for much faster dependency solving”
- “implemented in C++ for maximum efficiency”

### `conda env build` vs. `conda build`

`conda build` is a CLI-focused tool whereas `conda env` focus on using a YAML description file. Both resolves dependencies on installation.

[`conda env`](https://github.com/conda/conda/tree/master/conda_env) is now [a part of](https://github.com/conda-archive/conda-env) `conda`.

This is similar to the docker’s situation if you are familiar with it.

### Anaconda vs. miniconda

From [Anaconda vs. miniconda](https://stackoverflow.com/questions/45421163/anaconda-vs-miniconda) via StackOverflow:

- Miniconda installer = Python + `conda`
- Anaconda installer = Python + `conda` + *meta package* `anaconda`

Now we also have the option to use [miniforge](https://github.com/conda-forge/miniforge).

## See also

- [[Install Quantum ESPRESSO via conda]]
