# Modelling the SARS-CoV-2 epidemic in Croatia: a comparison of three analytic approaches
This repository serves as an official code base for the work-in-progress paper titled *Modelling the SARS-CoV-2 epidemic in Croatia: a comparison of three analytic approaches)*, to appear in [Croatian Medical Journal (CMJ)](http://www.cmj.hr/).


## Overview
Analysis, parameter identification and simulation of COVID-19 outbreak (mid Feb - Jun) in Croatia by using stochastic-deterministic SEIR(D), and Heidler exponential functions.

## Cite
to-be-added


## Reproduce the results
### Requirements
Clone the repo to your local machine:
```shell
$ git clone https://github.com/antelk/covid-19-modelling-croatia.git
```
Install all required Python packages using `conda`:
```shell
$ conda env create --name covid-19-modelling-croatia --file environment.yml 
```
Install the latest version of `coropy` by cloning the repo to your local machine:
```shell
$ git clone https://github.com/antelk/coropy.git
```
Go to `coropy` directory and run:
```shell
$ pip install .
```

### Running the examples
Run:
```shell
$ jupyter notebook
```
or
```shell
$ jupyter lab
```

## License
The code is under the [BSD 3-Clause](https://github.com/antelk/covid-19-modelling-croatia/blob/master/LICENSE) license.

Processed data are publicly available in `data` directory.
Raw medical records data are not publicly available.