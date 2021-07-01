# CIV Distance
Repo to compute CIV "distances" as advertised in Richards et al. papers.

Dependencies
```
pip install numpy
pip install joblib
pip install -U scikit-learn
```

The code you'll need is in ``CIVfunctions.py``.  To compute CIV distances for your dataset:

1) ``from CIVfunctions import project,CIV_distance``
2) Load your CIV blueshift and log10(EW)<sup>1</sup> data into an N-by-2 numpy array, ``data``.
3) Load in the line of best fit in ``data/bestfit.npy`` as ``fit``.
4) Save them as ``civ_distances = CIV_distance(data, fit)``

See ``example.ipynb`` for a walkthrough.

<sup>1</sup>If you wish to work with linearly scaled EWs instead, simply set the parameter ``logEW=False``.  However, we advise against this as the CIV distance metric is much more meaningful at low EWs when using the default logarithmic scale.

----

After calling ``CIV_distance(data, fit)`` the basic method for computing CIV distances for a given dataset is:

1) Convert the data from "raw" to "scaled" space.  Because the range of CIV blueshift (~ -1000-5000 km/s) is much greater than CIV EW (~ 5-110 Angstroms), scaling ensures that each parameter contributes equally to the CIV distance.  Scaling models are saved in ``scalers/`` and ensure that CIV distance calculations will be the same no matter the input dataset.  Note that ``CIV_distance()`` assumes ``scalers/`` is in your current working directory.
![alt text](https://github.com/RichardsGroup/CIV_Distance/blob/main/imgs/scale_data.png)
2) Project the scaled Blueshift+EW data onto the scaled best-fit curve.  (Note that points beyond either endpoint of the curve will get projected onto the respective endpoint.)
```
data = project(data, fit) 
```
![alt text](https://github.com/RichardsGroup/CIV_Distance/blob/main/imgs/project_scaled.png)

3) To compute a distance for a given data point, start at the upper left the curve, and travel from point-to-point<sup>2</sup> along the best-fit curve--summing your distance traveled as you go--until you pass the data point you're looking for.  Since the curve is monotonically decreasing, once your y-location on the curve falls below the projection of data point's y-location, save the total distance traveled.   
```
#Start at tip of line and sum distance traveled until passing data point
darr = [] #list to fill with distances along best-fit line for each point
for scat in data: #scat is [x,y] location of a given data point (projected onto the curve)
    d = 0 #start at beginning of the line
    for i in range(fit.shape[0]-1):
        xp, x = fit[i,0], fit[i+1,0]
        yp, y = fit[i,1], fit[i+1,1] 
        dp = d
        d += np.sqrt((x-xp)**2 + (y-yp)**2)
        if yp >= scat[1] >= y: #if we pass the projected y-coord, save the distance traveled
            darr.append((d+dp)/2)
            break
```
![alt text](https://github.com/RichardsGroup/CIV_Distance/blob/main/imgs/distance_path.png)

<sup>2</sup>You don't actually have to travel from point-to-point -- the ``step`` parameter sets the increment between points and can save a lot of time; see ``example.ipynb``. 

----

For another visualization of how CIV "distance" changes throughout the EW-blueshift plane, hover over the points in this plot: http://physics.drexel.edu/~tmccafferey/CIV_distance_example.html
