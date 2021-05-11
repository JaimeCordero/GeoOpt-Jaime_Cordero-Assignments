"""Provides a scripting component.
    Inputs:
        m: a mesh
        s: sun vector
    Output:
        a: List of Vectors - normals
        b: List of Points - 
        c: list of angles
        d: exploded mesh
        """
        
import Rhino.Geometry as rg
import ghpythonlib.treehelpers as th

#----------------- 1. Compute Face Normals -----------------#

"""compute face normals using rg.Mesh.FaceNormals.ComputeFaceNormals()
Output the vectors to a"""

m.FaceNormals.ComputeFaceNormals
a = m.FaceNormals

#----------------- 2. Get Face centers -----------------#

"""get the centers of each faces using rg.Mesh.Faces.GetFaceCenter()
Store the centers into a list called centers 
Output that list to b"""

centers = []

for i in range(m.Faces.Count):
    cntr = m.Faces.GetFaceCenter(i)
    centers.append(cntr)

b = centers

#----------------- 3. Angle between sun and FaceNormal -----------------#

"""calculate the angle between the sun and each FaceNormal using rg.Vector3d.VectorAngle()
Store the angles in a list called angleList and output it to c"""

anglesList = []
for i in range(m.Faces.Count):
    angles = rg.Vector3d.VectorAngle(s, a[i])
    anglesList.append(angles)

c = anglesList

#----------------- 4. Angle between sun and faceNormal -----------------#

"""explode the mesh - convert each face of the mesh into a mesh
For this, you have to first copy the mesh using rg.Mesh.Duplicate()
Then iterate through each face of the copy, extract it using rg.Mesh.ExtractFaces
And store the result into a list called exploded in output d"""

mesh2 = rg.Mesh.Duplicate(m)
print(m)
print(mesh2)

meshList = []

for i in range(m.Faces.Count):
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

#Rotating panels according to angle between sun and normals

for i in range(len(meshList)):
    vertices = meshList[i].Vertices
    #print(type(edges[0]))
    vA = rg.Vector3d(vertices[0])
    vB = rg.Vector3d(vertices[1])
    rotAxis = rg.Vector3d(vB-vA)
    transMesh = meshList[i].Rotate(anglesList[i], rotAxis, vertices[0])

#Frame in the edge

"""for i in range(len(meshList)):
    vertices = meshList[i].Vertices
    points = vertices.ToPoint3dArray
    curve = rg.Curve.CreateInterpolatedCurve(points[0], 1)"""

edg = []
movedEdg = []
extrusion

for i in range(len(meshList)):
    edges = meshList[i].GetNakedEdges()
    listEdge = []
    for j in range(len(edges)):
        edge = edges[j]
        listEdge.append(edge.ToNurbsCurve())
    curve = rg.Curve.JoinCurves(listEdge)[0]
    curve2 = curve.Duplicate()
    edg.append(curve2)
    vector = rg.Vector3d.Multiply(-a[i], 0.1)
    curve.Translate(vector)
    movedEdg.append(curve)
    ext = rg.Brep.CreateFromTaperedExtrude(curve2, 0.1, -a[i], b[i], 0, 0)
    extrusion.append(ext)
    #loft = rg.Brep.CreateFromLoft(curve, curve2, rg.Point3d.Unset, rg.Point3d.Unset, rg.LoftType.Normal, False)

print(type(movedEdg[0]))
e = th.list_to_tree(edg)
f = th.list_to_tree(movedEdg)
#I'm getting 2000 items
#getting Goo instead of Brep in here, tried [0] when creating the extrusion but didn't work
g = extrusion

