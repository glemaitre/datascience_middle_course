# Introduction to data science

## Installing required packages

We choose to use `mamba` (a drop-in replacement of `conda` that is faster) to
manage and install packages. Be aware that you can use any other solution
if you are already used to manage your own environments.

### Installing `mambaforge`

Mambaforge is a minimalist distribution that contains `mamba` and where the
default channel used to install the packages is `conda-forge`. You can download
and install mambaforge from the following
[link](https://github.com/conda-forge/miniforge#mambaforge).

### Creating the environment via `mamba`

```bash
$ mamba create --name teaching python=3
$ conda activate teaching
$ mamba install scikit-learn imbalanced-learn jupyterlab pandas seaborn
```
