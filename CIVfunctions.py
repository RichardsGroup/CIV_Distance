def trevorFit(data, fit):
    #Use: Project scattered data (data) onto a line of best fit (fit)
    #Returns: 2-D array of (x,y) locations on the line of your orthogonal projection
    
    #data: 2-D (N by 2) array of your data in some x-y space
    #fit: 2-D (N by 2) array of coordinates along your line of best fit
    
    trevorFit = np.array([]).reshape(0, 2) 
    
    for scat in data: 
        r = np.sqrt((scat[0]-fit[:,0])**2 + (scat[1]-fit[:,1])**2) #dist of data point from each point along fit
        delta = np.array([fit[np.argmin(r), 0], fit[np.argmin(r), 1]]) #we want to take the index of fit where
        trevorFit = np.concatenate((trevorFit, np.atleast_2d(delta)))  #the displacement was minimum (min r)
        
    return trevorFit


def sudo_pca(fit, data, step=1): #add step to decrease runtime for large, finely spaced array
    #fit: 2-D array containing coordinates of points along best fit line
    #data: 2-D [x,y] array of data (N by 2 shape)
    #NOTE: This really just caters to this situation (assumes monotonically decreasing function)
    
    data = trevorFit(data, fit) #project data onto fit
    
    #
    if fit[0,1] < fit[-1,1]: #Compare EQW at endpoints [Blueshift, EQW] - want fit[0,1] to be top left of plot
        fit  = np.flip(fit, axis=0)
    
    darr = [] #list to fill with distances for each point

    #Since in this case, the points of the fit (by definition) are already ordered by increasing CIV,
    #can save a whole lot of time by setting d=0 prior to entering the following loop
    for scat in data:
        d = 0 #start at beginning of the line
        for i in range(0, fit.shape[0]-2, step):
            xp, x = fit[i,0], fit[i+step-1,0]
            yp, y = fit[i,1], fit[i+step-1,1] 
            dp = d
            d += np.sqrt((x-xp)**2 + (y-yp)**2)
            if yp >= scat[1] >= y: #if we pass the projected y-coord, save the distance traveled
                darr.append(d)
                break
    
    return np.array(darr).reshape(len(darr),1)


