# Analysis of the first wave COVID-19 pandemic in Croatia

This repo serves as an official code base for the paper titled `Analysis of the first wave COVID-19 pandemic in Croatia` published in Croatian Medical Journal.

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
In `cmj-covid-19-paper` go to `notebooks` directory and start `jupyter notebook` or `jupyter lab`. 

## Cite

`tba`

## Authors
* Ozren Polašek, the first author of the paper
* Ante Lojić Kapetanović, the main developer and the second author
* Dragan Poljak, the third author

## License
The code is under the [BSD 3-Clause](https://github.com/antelk/cmj-covid-19-paper/blob/master/LICENSE) license. Processed data are publicaly available in the `data` directory, except the raw data which is properietary.