# Modelling the COVID-19 epidemic in Croatia: a comparison of three analytic approaches

This repository holds the code for the paper *Modelling the COVID-19 epidemic in Croatia: a comparison of three analytic approaches*, published in Croat Med J.


## Abstract

### Aim
To facilitate the development of a COVID-19 predictive model in Croatia by analyzing three different methodological approaches.

### Method
We used the historical data to explore the fit of the extended SEIRD compartmental model, the Heidler function, an exponential approximation in analyzing electromagnetic phenomena related to lightning strikes, and the Holt-Winters smoothing (HWS) for short-term epidemic predictions. We also compared various methods for the estimation of R0.

### Results
The R0 estimates for Croatia varied from 2.09 (95% CI 1.77-2.40) obtained by using an empirical post-hoc method to 2.28 (95% CI 2.27-2.28) when we assumed an exponential outbreak at the very beginning of the COVID-19 epidemic in Croatia. Although the SEIRD model provided a good fit for the early epidemic stages, it was outperformed by the Heidler function fit. HWS achieved accurate short-term predictions and depended the least on model entry parameters. Neither model performed well across the entire observed period, which was characterized by multiple wave-form events, influenced by the re-opening for the tourist season during the summer, mandatory masks use in closed spaces, and numerous measures introduced in retail stores and public places. However, an extension of the Heidler function achieved the best overall fit.

### Conclusions
Predicting future epidemic events remains difficult because modeling relies on the accuracy of the information on population structure and micro-environmental exposures, constant changes of the input parameters, varying societal adherence to anti-epidemic measures, and changes in the biological interactions of the virus and hosts.

## Cite

Lojić Kapetanović A, Lukezić M, Pribisalić A, Poljak D, Polašek O. Modeling the COVID-19 epidemic in Croatia: a comparison of three analytic approaches. Croat Med J. 2022 Jun 22;63(3):295-298. doi: 10.3325/cmj.2022.63.295. PMID: 35722698; PMCID: PMC9284011.


## Reproduce the results

### Requirements
Clone the repo to your local machine
```shell
$ git clone https://github.com/antelk/covid-19-modelling-croatia.git
```
Install all required Python packages using `conda`
```shell
$ conda env create --name covid-19-modelling-croatia --file environment.yml 
```
In addition, install the latest version of `coropy` by cloning the repo to your local machine; details available at [antelk / coropy](https://github.com/antelk/coropy).

### Running the notebooks
Inside the `notebooks` sub-directory within `covid-19-modelling-croatia` start `jupyter` server by running
```shell
$ jupyter lab
```


## License
The code is under the [BSD 3-Clause](https://github.com/antelk/covid-19-modelling-croatia/blob/master/LICENSE) license.

Processed data are publicly available in `data` directory.
Raw medical records are not publicly available.