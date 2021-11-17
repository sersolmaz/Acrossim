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
renderView1.ViewSize = [779, 595]
renderView1.AxesGrid = 'GridAxes3DActor'
renderView1.CenterOfRotation = [0.13469999562948942, 0.0, 0.0]
renderView1.StereoType = 'Crystal Eyes'
renderView1.CameraPosition = [0.13469999562948942, 0.0, 0.8728879109919444]
renderView1.CameraFocalPoint = [0.13469999562948942, 0.0, 0.0]
renderView1.CameraFocalDisk = 1.0
renderView1.CameraParallelScale = 0.23005740770156918
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

# create a new 'OpenFOAMReader'
pitzDaily_LESfoam = OpenFOAMReader(FileName='C:/Users/u0127798/Desktop/tutorials/OpenFOAM/pitzDaily_LES/pitzDaily_LES.foam')
pitzDaily_LESfoam.MeshRegions = ['internalMesh']
pitzDaily_LESfoam.CellArrays = ['U', 'UMean', 'UPrime2Mean', 'U_0', 'k', 'k_0', 'nut', 'p', 'pMean', 'pPrime2Mean', 's', 's_0']

# ----------------------------------------------------------------
# setup the visualization in view 'renderView1'
# ----------------------------------------------------------------

# show data from pitzDaily_LESfoam
pitzDaily_LESfoamDisplay = Show(pitzDaily_LESfoam, renderView1, 'UnstructuredGridRepresentation')

# get color transfer function/color map for 'U'
uLUT = GetColorTransferFunction('U')
uLUT.RGBPoints = [0.02264286621144795, 0.231373, 0.298039, 0.752941, 7.7170077878956675, 0.865003, 0.865003, 0.865003, 15.411372709579888, 0.705882, 0.0156863, 0.14902]
uLUT.ScalarRangeInitialized = 1.0

# get opacity transfer function/opacity map for 'U'
uPWF = GetOpacityTransferFunction('U')
uPWF.Points = [0.02264286621144795, 0.0, 0.5, 0.0, 15.411372709579888, 1.0, 0.5, 0.0]
uPWF.ScalarRangeInitialized = 1

# trace defaults for the display properties.
pitzDaily_LESfoamDisplay.Representation = 'Surface'
pitzDaily_LESfoamDisplay.ColorArrayName = ['POINTS', 'U']
pitzDaily_LESfoamDisplay.LookupTable = uLUT
pitzDaily_LESfoamDisplay.OSPRayScaleArray = 'p'
pitzDaily_LESfoamDisplay.OSPRayScaleFunction = 'PiecewiseFunction'
pitzDaily_LESfoamDisplay.SelectOrientationVectors = 'U'
pitzDaily_LESfoamDisplay.ScaleFactor = 0.031059999205172065
pitzDaily_LESfoamDisplay.SelectScaleArray = 'p'
pitzDaily_LESfoamDisplay.GlyphType = 'Arrow'
pitzDaily_LESfoamDisplay.GlyphTableIndexArray = 'p'
pitzDaily_LESfoamDisplay.GaussianRadius = 0.001552999960258603
pitzDaily_LESfoamDisplay.SetScaleArray = ['POINTS', 'p']
pitzDaily_LESfoamDisplay.ScaleTransferFunction = 'PiecewiseFunction'
pitzDaily_LESfoamDisplay.OpacityArray = ['POINTS', 'p']
pitzDaily_LESfoamDisplay.OpacityTransferFunction = 'PiecewiseFunction'
pitzDaily_LESfoamDisplay.DataAxesGrid = 'GridAxesRepresentation'
pitzDaily_LESfoamDisplay.PolarAxes = 'PolarAxesRepresentation'
pitzDaily_LESfoamDisplay.ScalarOpacityFunction = uPWF
pitzDaily_LESfoamDisplay.ScalarOpacityUnitDistance = 0.013662170746235222
pitzDaily_LESfoamDisplay.ExtractedBlockIndex = 1

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
pitzDaily_LESfoamDisplay.OSPRayScaleFunction.Points = [0.008018268893823101, 0.0, 0.5, 0.0, 2.3, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
pitzDaily_LESfoamDisplay.ScaleTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 226.3834991455078, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
pitzDaily_LESfoamDisplay.OpacityTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 226.3834991455078, 1.0, 0.5, 0.0]

# setup the color legend parameters for each legend in this view

# get color legend/bar for uLUT in view renderView1
uLUTColorBar = GetScalarBar(uLUT, renderView1)
uLUTColorBar.WindowLocation = 'AnyLocation'
uLUTColorBar.Title = 'U'
uLUTColorBar.ComponentTitle = 'Magnitude'
uLUTColorBar.ScalarBarLength = 0.7008439897698198

# set color bar visibility
uLUTColorBar.Visibility = 1

# show color legend
pitzDaily_LESfoamDisplay.SetScalarBarVisibility(renderView1, True)

# ----------------------------------------------------------------
# setup color maps and opacity mapes used in the visualization
# note: the Get..() functions create a new object, if needed
# ----------------------------------------------------------------

# ----------------------------------------------------------------
# finally, restore active source
SetActiveSource(pitzDaily_LESfoam)
# ----------------------------------------------------------------