import numpy as np
from sklearn.preprocessing import scale

def project(data, fit):
    #Use: Project scattered data (data) onto a line of best fit (fit)
    #Returns: 2-D array of (x,y) locations on the line of your orthogonal projection
    
    #data: 2-D (N by 2) array of your data in some x-y space
    #fit: 2-D (N by 2) array of coordinates along your line of best fit
    
    locs = [] #this will contain xy locations along the best-fit curve corresponding to each data point's orthogonal projection onto said curve - python list faster than numpy array
    
    #Loop through each data point and compare with locations along fit
    for scat in data: 
        r2 = (scat[0]-fit[:,0])**2 + (scat[1]-fit[:,1])**2      #dist^2 of scat from each point along fit
        delta = [fit[np.argmin(r2), 0], fit[np.argmin(r2), 1]]  #save point along fit where dist^2 was minimum
        locs.append(delta)  
        
    return np.array(locs)


def CIV_distance(data_original, fit_original, step=1):
    #fit: N-by-2 array containing coordinates of points along best fit line 
    #data: N-by-2 [[x,y]] array of data 
    #NOTE: This really just caters to this situation (assumes monotonically decreasing fit_original)
    
    #1) Scale all the data equally
    xscale = scale(np.concatenate((fit_original[:,0], data_original[:,0]))) #add ``good`` mask to lofar to remove "bad" reconstructions
    yscale = scale(np.concatenate((fit_original[:,1], data_original[:,1])))
    fit = np.array([xscale[0:len(fit_original)], yscale[0:len(fit_original)]]).T
    data = np.array([xscale[len(fit_original):len(fit_original)+len(data_original)], yscale[len(fit_original):len(fit_original)+len(data_original)]]).T
    
    #2) data is now each point's orthogonal projection onto fit
    ind_projcut = -((fit.shape[0]-1)%step)
    data = project(data, fit[:ind_projcut]) 
        
    darr = [] #list to fill with distances along best-fit line for each point

    #3) Loop through each data point- start at tip of line and sum dist traveled until passing data point
    for scat in data:
        d = 0 #start at beginning of the line
        for i in range(0, fit.shape[0]-step, step):
            xp, x = fit[i,0], fit[i+step,0]
            yp, y = fit[i,1], fit[i+step,1] 
            dp = d
            d += np.sqrt((x-xp)**2 + (y-yp)**2)
            if yp >= scat[1] >= y: #if we pass the projected y-coord, save the distance traveled
                darr.append((d+dp)/2) #save the average between dprevious and d
                break
                
    return np.array(darr)
