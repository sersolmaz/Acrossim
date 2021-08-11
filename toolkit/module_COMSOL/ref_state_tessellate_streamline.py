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
renderView1.ViewSize = [1126, 755]
renderView1.AxesGrid = 'GridAxes3DActor'
renderView1.CenterOfRotation = [-9.337710969048452e-05, 0.0009372758166429906, 0.35104447806384104]
renderView1.StereoType = 'Crystal Eyes'
renderView1.CameraPosition = [-2.250011410798908, -1.7085351290168493, 3.0433445018908265]
renderView1.CameraFocalPoint = [-9.337710969047147e-05, 0.0009372758166430117, 0.35104447806384104]
renderView1.CameraViewUp = [0.5250548224857883, 0.4482975914469092, 0.7234270542959516]
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

# create a new 'PVD Reader'
merged_strpvd = PVDReader(FileName='D:/Engineering/PhD/System_Architecture/5_software_development_one-way/6_SOFTWARE_Final/A_software_final/2_acrossim_toolkit_update2_11082021/module_COMSOL/streamline_mixing/merged_str.pvd')
merged_strpvd.PointArrays = ['Streamline']

# ----------------------------------------------------------------
# setup the visualization in view 'renderView1'
# ----------------------------------------------------------------

# show data from merged_strpvd
merged_strpvdDisplay = Show(merged_strpvd, renderView1, 'UnstructuredGridRepresentation')

# trace defaults for the display properties.
merged_strpvdDisplay.Representation = 'Surface'
merged_strpvdDisplay.ColorArrayName = [None, '']
merged_strpvdDisplay.OSPRayScaleArray = 'Streamline'
merged_strpvdDisplay.OSPRayScaleFunction = 'PiecewiseFunction'
merged_strpvdDisplay.SelectOrientationVectors = 'None'
merged_strpvdDisplay.ScaleFactor = 0.1297911043872318
merged_strpvdDisplay.SelectScaleArray = 'None'
merged_strpvdDisplay.GlyphType = 'Arrow'
merged_strpvdDisplay.GlyphTableIndexArray = 'None'
merged_strpvdDisplay.GaussianRadius = 0.006489555219361589
merged_strpvdDisplay.SetScaleArray = ['POINTS', 'Streamline']
merged_strpvdDisplay.ScaleTransferFunction = 'PiecewiseFunction'
merged_strpvdDisplay.OpacityArray = ['POINTS', 'Streamline']
merged_strpvdDisplay.OpacityTransferFunction = 'PiecewiseFunction'
merged_strpvdDisplay.DataAxesGrid = 'GridAxesRepresentation'
merged_strpvdDisplay.PolarAxes = 'PolarAxesRepresentation'
merged_strpvdDisplay.ScalarOpacityUnitDistance = 0.03843105768110085

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
merged_strpvdDisplay.OSPRayScaleFunction.Points = [0.008018268893823101, 0.0, 0.5, 0.0, 2.3, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
merged_strpvdDisplay.ScaleTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 19.0, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
merged_strpvdDisplay.OpacityTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 19.0, 1.0, 0.5, 0.0]

# ----------------------------------------------------------------
# finally, restore active source
SetActiveSource(merged_strpvd)
# ----------------------------------------------------------------