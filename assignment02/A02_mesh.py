"""Provides a scripting component.
    Inputs:
        mesh: a mesh
        sun: sun vector
    Output:
        a: List of Vectors - normals
        b: List of Points - 
        c: list of angles
        d: exploded mesh
        """
        
import Rhino.Geometry as rg

#----------------- 1. Compute Face Normals -----------------#

"""compute face normals using rg.Mesh.FaceNormals.ComputeFaceNormals()
Output the vectors to a"""

mesh.FaceNormals.ComputeFaceNormals
a = mesh.FaceNormals

#----------------- 2. Get Face centers -----------------#

"""get the centers of each faces using rg.Mesh.Faces.GetFaceCenter()
Store the centers into a list called centers 
Output that list to b"""

centers = []

for i in range(mesh.Faces.Count):
    cntr = mesh.Faces.GetFaceCenter(i)
    centers.append(cntr)

b = centers

#----------------- 3. Angle between sun and FaceNormal -----------------#

"""calculate the angle between the sun and each FaceNormal using rg.Vector3d.VectorAngle()
Store the angles in a list called angleList and output it to c"""

anglesList = []
for i in range(mesh.Faces.Count):
    angles = rg.Vector3d.VectorAngle(sun, a[i])
    anglesList.append(angles)

c = anglesList

#----------------- 4. Angle between sun and faceNormal -----------------#

"""explode the mesh - convert each face of the mesh into a mesh
For this, you have to first copy the mesh using rg.Mesh.Duplicate()
Then iterate through each face of the copy, extract it using rg.Mesh.ExtractFaces
And store the result into a list called exploded in output d"""

mesh2 = rg.Mesh.Duplicate(mesh)
print(mesh)
print(mesh2)

meshList = []

for i in range(mesh.Faces.Count):
    meshes = mesh2.Faces.ExtractFaces([0])
    meshList.append(meshes)
    
print(type(meshList[0]))
d = meshList

#----------------- 5. Faces transformation -----------------#

"""after here, your task is to apply a transformation to each face of the mesh
the transformation should correspond to the angle value that corresponds that face to it... 
the result should be a mesh that responds to the sun position... its up to you!

Bonus tasks:
- Propose a different mesh to analyse
- Provide a frame for the resulting mesh by moving edges according to the rg.Mesh.VertexNormals"""

srpt = []
for i in range(len(meshList)):
    v = []
    v1 =  meshList[i].Vertices
    v.append(v1[0])
    v.append(v1[3])

##moving diagonal points based on vector angle difference
    mvdpoints = []
    for pt in v:
        vec = rg.Vector3d(pt)
        mag = anglesList[i]*-0.8
        zvec = rg.Vector3d(0,0,mag)
        mvdp = rg.Point3d(vec - zvec)
        mvdpoints.append(mvdp)
    srpt.append(mvdpoints)