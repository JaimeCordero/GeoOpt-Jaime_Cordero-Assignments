"""Provides a scripting component.
    Inputs:
        x: slider input
        y: slider input
    Output:
        sphere
        pt: point on sphere
        sun: sun vector
        """

import Rhino.Geometry as rg
import math

#----------------- 1. Create a sun vector -----------------#

"""create a Sphere at point (0,0,0) with radius 1 and output it to a. 
output the sphere to a"""

sph = rg.Sphere(rg.Point3d(0,0,0),1)

sphere = sph

#----------------- 2. Evaluate sphere -----------------#

"""evaluate a point in the sphere using rg.Sphere.PointAt() at coordintes x and y.
The point should only be on the upper half of the sphere (upper hemisphere)
the angles are in radians, so you might want to use math.pi for this
output the point to b"""

point = sph.PointAt(x*2*math.pi,y*math.pi)
#srf = sph.ToNurbsSurface()
#a = srf.SetDomain(0,rg.Interval(0,1))
#e = srf.SetDomain(1,rg.Interval(-math.pi,1))
#point = srf.PointAt(x,y)

print(a)
print(e)

pt = point
print(point)

#----------------- 3. Create sun vector -----------------#

"""create a vector from the origin and reverse the vector
keep in mind that Reverse affects the original vector
output the vector to c"""

vec = rg.Vector3d(point)
vec.Reverse()

#print vec
sun = vec

