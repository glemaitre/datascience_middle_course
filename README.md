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

### Creating the environment from the `environment.yml`

We provide an `environment.yml` file that contains the packages to be
installed. You can use the following command that will create an `teaching`
environment where the required package will be installed.

```bash
$ mamba create --file environment.yml
```

Then, you can activate the environment via:

```bash
conda activate teaching
```
