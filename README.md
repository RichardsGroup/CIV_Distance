# CIV_Distance
Repo to compute CIV "distances" as advertised in Richards et al. papers.

The code you'll need is in ``CIVfunctions.py``.  To compute CIV distances for your dataset:

1) ``from CIVfunctions import project,CIV_distance``
2) Load your CIV bluehsift and EW data into an N-by-2 numpy array, ``data``.
3) Load in the line of best fit in ``data/RM_CIV_bestFitLine_noScale.npy`` as ``fit``.
4) Save them as ``civ_distances = CIV_distance(data, fit)``

See ``example.ipynb`` for a walkthrough.

After calling ``CIV_distance()`` the basic method for computing CIV distances for a given dataset is:

1) Convert your data from "raw" to "scaled" space.  Because the range of CIV blueshift (~ -1000-5000 km/s) is much greater than CIV EW (~ 5-110 Angstroms), scaling ensures that each parameter contributes equally to the CIV distance.
2) Project the scaled Blueshift+EW data onto the scaled best-fit curve.
3) For a given data point, 

For a visualization of how CIV "distance" changes throughout the EW-blueshift plane, hover over the points in this plot: http://physics.drexel.edu/~tmccafferey/CIV_distance_example.html
