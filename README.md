# covid-19-modelling-croatia

This repository serves as an official code base for the work-in-progress paper titled -- Modelling the SARS-CoV-2 epidemic in Croatia: a comparison of three analytic approaches), to appear in Croatian Medical Journal (CMJ).


## Overview

Analysis, parameter identification and simulation of the first wave (mid Feb - Jun) of COVID-19 outbreak in Croatia using deterministic SEIR(D) and Heidler exponential functions.


## Reproduce the results

### The working environment

Clone the repo to your local machine:
```shell
$ git clone https://github.com/antelk/cmj-covid-19-paper.git
```

Install all required Python packages using `conda`:
```shell
$ conda env create --name cmj-covid-19-paper --file env.yml 
```
or using `pip`.

Install the latest version of `coropy` by cloning the repo to your local machine:
```shell
$ git clone https://github.com/antelk/covid-19.git
```

Go to `covid-19` directory and run:
```shell
$ pip install .
```


### Running the examples

Go to `notebooks` directory and start `jupyter notebook` or `jupyter lab`. 


## Cite

to-be-added


## Authors

to-be-added

## License

The code is under the [BSD 3-Clause](https://github.com/antelk/cmj-covid-19-paper/blob/master/LICENSE) license. Processed data are publicaly available in the `data` directory, except the raw data which is properietary.