# CIV_Distance
Repo to compute CIV "distances" as advertised in Richards et al. papers.

The code you'll need is in ``CIVfunctions.py``.  To compute CIV distances for your dataset:

1) ``from CIVfunctions import project,CIV_distance``
2) Load your CIV bluehsift and EW data into an N-by-2 numpy array, ``data``.
3) Load in the line of best fit in ``data/RM_CIV_bestFitLine_noScale.npy`` as ``fit``.
4) Save them as ``civ_distances = CIV_distance(data, fit)``

See ``example.ipynb`` for a walkthrough.

The basic method for computing CIV distances for a given dataset is:



For a visualization of how CIV "distance" changes throughout the EW-blueshift plane, hover over the points in this plot: http://physics.drexel.edu/~tmccafferey/CIV_distance_example.html
