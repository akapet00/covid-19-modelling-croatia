# Modelling the SARS-CoV-2 epidemic in Croatia: a comparison of three analytic approaches
This repository serves as an official code base for the work-in-progress paper titled *Modelling the SARS-CoV-2 epidemic in Croatia: a comparison of three analytic approaches)*, to appear in [Croatian Medical Journal (CMJ)](http://www.cmj.hr/).


## Overview
Analysis, parameter identification and simulation of the first wave (mid Feb - Jun) of COVID-19 outbreak in Croatia using deterministic SEIR(D) and Heidler exponential functions.

### Cite
to-be-added

### DOI
to-be-added


## Reproduce the results
### The working environment
Clone the repo to your local machine:
```shell
$ git clone https://github.com/antelk/covid-19-modelling-croatia.git
```
Install all required Python packages using `conda`:
```shell
$ conda env create --name covid-19-modelling-croatia --file env.yml 
```
Install the latest version of `coropy` by cloning the repo to your local machine:
```shell
$ git clone https://github.com/antelk/coropy.git
```
Go to `covid-19` directory and run:
```shell
$ pip install .
```

### Running the examples
Go to `notebooks` directory and start `jupyter notebook` or `jupyter lab`. 


## License
The code is under the [BSD 3-Clause](https://github.com/antelk/covid-19-modelling-croatia/blob/master/LICENSE) license.

Processed data are publicly available in `data` directory.
Raw medical records data are not publicly available.