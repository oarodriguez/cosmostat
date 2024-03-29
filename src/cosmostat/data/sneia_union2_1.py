import os

import numpy as np

from cosmostat.cosmology import Dataset

cw_directory = os.path.dirname(os.path.abspath(__file__))
filename = os.path.join(cw_directory, "union2.txt")
sne_file = np.loadtxt(filename, usecols=(1, 2, 3))

REDSHIFTS_SNE = sne_file[:, 0]
OBS_SNE = sne_file[:, 1]
ERROR_SNE = sne_file[:, 2] * sne_file[:, 2]
# square root of the errors to standardize with JLa

DATA_SNE_SQR = np.stack((REDSHIFTS_SNE, OBS_SNE, ERROR_SNE), axis=1)
DATA_SNE = sne_file

dataset = Dataset(
    name="SNe",
    label="> SNe U2.1 (557)",
    data=DATA_SNE,
    cosmology_func="mu_sne",
)

## =====================================================================
# data downloaded from http://supernova.lbl.gov/Union/
# union2.txt file contains an ASCII table with tab-separated columns:
#   Supernova Name, Redshift, Distance Modulus, and Distance Modulus Error.
#   Last column: probability that the supernova was hosted by a low-mass galaxy.
# Covariance Matrix
# A 580 x 580 (Union2.1) tab-separated ASCII-format covariance matrix,
#  available with or without systematics.
#
## =====================================================================
