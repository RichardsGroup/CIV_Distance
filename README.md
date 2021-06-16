# CIV_Distance
Repo to compute CIV "distances" as advertised in Richards et al. papers.

The code you'll need is in ``CIVfunctions.py``.  To compute CIV distances for your dataset:

1) ``from CIVfunctions import project,CIV_distance``
2) Load your CIV bluehsift and EW data into an N-by-2 numpy array, ``data``.
3) Load in the line of best fit in ``data/RM_CIV_bestFitLine_noScale.npy`` as ``fit``.
4) Save them as ``civ_distances = CIV_distance(data, fit)``

See ``example.ipynb`` for a walkthrough.

After calling ``CIV_distance()`` the basic method for computing CIV distances for a given dataset is:

1) Convert the data from "raw" to "scaled" space.  Because the range of CIV blueshift (~ -1000-5000 km/s) is much greater than CIV EW (~ 5-110 Angstroms), scaling ensures that each parameter contributes equally to the CIV distance.
2) Project the scaled Blueshift+EW data onto the scaled best-fit curve.
3) To compute a distance for a given data point, start at the upper left the curve, and travel along each point in the 
```
#Loop through each data point- start at tip of line and sum dist traveled until passing data point
darr = [] #list to fill with distances along best-fit line for each point
for scat in data:
    d = 0 #start at beginning of the line
    for i in range(fit.shape[0]-1):
        xp, x = fit[i,0], fit[i+1,0]
        yp, y = fit[i,1], fit[i+1,1] 
        d += np.sqrt((x-xp)**2 + (y-yp)**2)
        if yp >= scat[1] > y: #if we pass the projected y-coord, save the distance traveled
            darr.append(d)
            break
```

For a visualization of how CIV "distance" changes throughout the EW-blueshift plane, hover over the points in this plot: http://physics.drexel.edu/~tmccafferey/CIV_distance_example.html
