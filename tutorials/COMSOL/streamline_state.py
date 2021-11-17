# state file generated using paraview version 5.8.0

# ----------------------------------------------------------------
# setup views used in the visualization
# ----------------------------------------------------------------

# trace generated using paraview version 5.8.0
#
# To ensure correct image size when batch processing, please search 
# for and uncomment the line `# renderView*.ViewSize = [*,*]`

#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# get the material library
materialLibrary1 = GetMaterialLibrary()

# Create a new 'Render View'
renderView1 = CreateView('RenderView')
renderView1.ViewSize = [1176, 595]
renderView1.AxesGrid = 'GridAxes3DActor'
renderView1.CenterOfRotation = [-9.337710969048452e-05, 0.0009372758166429906, 0.35104447806384104]
renderView1.StereoType = 'Crystal Eyes'
renderView1.CameraPosition = [-2.156429868717939, -2.649560197761015, 2.2373060073917226]
renderView1.CameraFocalPoint = [-9.337710969043188e-05, 0.0009372758166430304, 0.351044478063841]
renderView1.CameraViewUp = [0.2712913224964147, 0.4017414962145148, 0.8746455216586142]
renderView1.CameraFocalDisk = 1.0
renderView1.CameraParallelScale = 1.0101540711151924
renderView1.BackEnd = 'OSPRay raycaster'
renderView1.OSPRayMaterialLibrary = materialLibrary1

SetActiveView(None)

# ----------------------------------------------------------------
# setup view layouts
# ----------------------------------------------------------------

# create new layout object 'Layout #1'
layout1 = CreateLayout(name='Layout #1')
layout1.AssignView(0, renderView1)

# ----------------------------------------------------------------
# restore active view
SetActiveView(renderView1)
# ----------------------------------------------------------------

# ----------------------------------------------------------------
# setup the data processing pipelines
# ----------------------------------------------------------------

# create a new 'XML Unstructured Grid Reader'
str1vtu = XMLUnstructuredGridReader(FileName=['C:/Users/u0127798/Desktop/tutorials/COMSOL/streamline_velocity/str1.vtu'])
str1vtu.PointArrayStatus = ['Streamline']

# ----------------------------------------------------------------
# setup the visualization in view 'renderView1'
# ----------------------------------------------------------------

# show data from str1vtu
str1vtuDisplay = Show(str1vtu, renderView1, 'UnstructuredGridRepresentation')

# trace defaults for the display properties.
str1vtuDisplay.Representation = 'Surface'
str1vtuDisplay.ColorArrayName = [None, '']
str1vtuDisplay.OSPRayScaleArray = 'Streamline'
str1vtuDisplay.OSPRayScaleFunction = 'PiecewiseFunction'
str1vtuDisplay.SelectOrientationVectors = 'None'
str1vtuDisplay.ScaleFactor = 0.1297911043872318
str1vtuDisplay.SelectScaleArray = 'None'
str1vtuDisplay.GlyphType = 'Arrow'
str1vtuDisplay.GlyphTableIndexArray = 'None'
str1vtuDisplay.GaussianRadius = 0.006489555219361589
str1vtuDisplay.SetScaleArray = ['POINTS', 'Streamline']
str1vtuDisplay.ScaleTransferFunction = 'PiecewiseFunction'
str1vtuDisplay.OpacityArray = ['POINTS', 'Streamline']
str1vtuDisplay.OpacityTransferFunction = 'PiecewiseFunction'
str1vtuDisplay.DataAxesGrid = 'GridAxesRepresentation'
str1vtuDisplay.PolarAxes = 'PolarAxesRepresentation'
str1vtuDisplay.ScalarOpacityUnitDistance = 0.03843105768110085

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
str1vtuDisplay.OSPRayScaleFunction.Points = [0.008018268893823101, 0.0, 0.5, 0.0, 2.3, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
str1vtuDisplay.ScaleTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 19.0, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
str1vtuDisplay.OpacityTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 19.0, 1.0, 0.5, 0.0]

# ----------------------------------------------------------------
# finally, restore active source
SetActiveSource(str1vtu)
# ----------------------------------------------------------------