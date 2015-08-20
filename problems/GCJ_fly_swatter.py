from __future__ import division
import sys
import numpy as np

def circular_segment_area(rad, theta):
    return pow(rad, 2) * (theta - np.sin(theta)) / 2.0
    
def get_area_exact(x1, y1, g, t):
    #Given the position of the lower left corner of a square
    #in the upper right quadrant of the racquet, find the 
    #area of the unobstructed region (which will be a square
    #potentially occluded by a circular arc)
    
    #The occluding circle has radius 1 - t (we've normalized):
    R_adj = 1.0 - t
    
    #Check if the lower left corner is occluded (and we return 0)
    if pow(x1, 2) + pow(y1, 2) >= pow(R_adj, 2):
        return 0.0
        
    #Check if the upper right corner isn't occluded (and we
    #return the full area, g^2)
    x2 = x1 + g
    y2 = y1 + g
    if pow(x2, 2) + pow(y2, 2) <= pow(R_adj, 2):
        return pow(g, 2)
        
    #Otherwise we have some occlusion to worry about, and there
    #are four different options:
    # 1) only the upper right (UR) corner is occluded
    # 2) both the UR and UL corners are occluded
    # 3) both the UR and LR corners are occluded
    # 4) all of the UR, UL, and LR corners are occluded
    # Any other options are excluded by the checks we've already done.
    ul_occ = pow(x1, 2) + pow(y2, 2) >= pow(R_adj, 2)
    lr_occ = pow(x2, 2) + pow(y1, 2) >= pow(R_adj, 2)
    
    #Now the unoccluded area in the square is the sum of a single
    #circular segment and rectangular or right triangular regions.
    if not lr_occ:
        if not ul_occ:
            #Case 1, intersecting the upper and right edges
            segment = circular_segment_area(R_adj,
                np.arcsin(y2 / R_adj) - np.arccos(x2 / R_adj))
            #print segment, pow(g, 2)
            dx = x2 - np.sqrt(pow(R_adj, 2) - pow(y2, 2))
            dy = y2 - np.sqrt(pow(R_adj, 2) - pow(x2, 2))
            num = pow(g, 2) - dx * dy / 2 + segment
        else:
            #Case 2, intersecting the left and right edges
            segment = circular_segment_area(R_adj,
                np.arccos(x1 / R_adj) - np.arccos(x2 / R_adj))
            #print segment, pow(g, 2)
            y_left = np.sqrt(pow(R_adj, 2) - pow(x1, 2)) - y1
            y_right = np.sqrt(pow(R_adj, 2) - pow(x2, 2)) - y1
            num = g * (y_left + y_right) / 2 + segment
    else:
        if not ul_occ:
            #Case 3, intersecting the upper and lower edges
            segment = circular_segment_area(R_adj,
                np.arcsin(y2 / R_adj) - np.arcsin(y1 / R_adj))
            #print segment, pow(g, 2)
            x_upper = np.sqrt(pow(R_adj, 2) - pow(y2, 2)) - x1
            x_lower = np.sqrt(pow(R_adj, 2) - pow(y1, 2)) - x1
            num = g * (x_lower + x_upper) / 2 + segment
        else:
            #Case 4, intersecting the left and lower edges
            segment = circular_segment_area(R_adj,
                np.arccos(x1 / R_adj) - np.arcsin(y1 / R_adj))
            #print segment, pow(g, 2)
            dx = np.sqrt(pow(R_adj, 2) - pow(y1, 2)) - x1
            dy = np.sqrt(pow(R_adj, 2) - pow(x1, 2)) - y1
            num = dx * dy / 2 + segment
    if num > pow(g, 2):
        raise ValueError('Problem: %s %s' % (lr_occ, ul_occ))
    return num

def get_area_recursive(x1, y1, g, t, epsilon=1e-9):
    #Here we'll use a recursive approach
    R_adj = 1 - t
    
    if pow(x1, 2) + pow(y1, 2) >= pow(R_adj, 2):
        return 0.0
    
    x2 = x1 + g
    y2 = y1 + g
    if pow(x2, 2) + pow(y2, 2) <= pow(R_adj, 2):
        return pow(g, 2)
        
    if pow(g, 2) <= epsilon:
        return pow(g, 2) / 2.0
    
    midx = x1 + g / 2.0
    midy = y1 + g / 2.0
    
    return get_area_recursive(x1, y1, g / 2.0, t) + \
           get_area_recursive(midx, y1, g / 2.0, t) + \
           get_area_recursive(x1, midy, g / 2.0, t) + \
           get_area_recursive(midx, midy, g / 2.0, t)
    
def solve_prob(f, R, t, r, g):
    #First adjust t (rim thickness), r (string radius), 
    #and g (string gap) for the fly's radius f, so that we
    #can treat the fly as a point and divide value by R,
    #the outer radius of the raquet, so we're working on the
    #unit circle.
    #So, f=0 and R=1 after these adjustments.
    t = (t + f) / R
    r = (r + f) / R
    g = (g - 2 * f) / R
    
    #The gap might be negative now, and if it is, the fly will
    #always be hit!
    if g <= 0:
        return 1.0
        
    #Now we need to add up the areas of all the squares.  We'll
    #loop through the squares in the upper right quadrant (the 
    #system is symmetric), indexed by their lower left corners.
    #
    #These values will range from r (the smallest) up to (1-t)
    #in steps of 2r+g
    free_area = 0.0
    for x1 in np.arange(r, 1-t, g + 2 * r):
        for y1 in np.arange(r, 1-t, g + 2 * r):
            free_area += get_area_exact(x1, y1, g, t)
            
    #Calculate the area of the full quadrant of the racquet
    #and return 1 minus the fraction of free area.
    return 1.0 - 4 * free_area / np.pi
    
infile = open("%s" % sys.argv[1], 'r')
outfile = open("%s.out" % sys.argv[1][:-3], 'w')
cases = int(infile.readline().strip())
for i in range(cases):
    #Read in the raw parameters
    f, R, t, r, g = [float(num) for num in infile.readline().split()]
    output = solve_prob(f, R, t, r, g)
    outfile.write("Case #%i: %.6f\n" % (i+1, output))
    print "Case #%i: %.6f" % (i+1, output)
infile.close()
outfile.close()