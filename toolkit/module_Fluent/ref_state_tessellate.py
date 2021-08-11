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
renderView1.ViewSize = [991, 755]
renderView1.InteractionMode = '2D'
renderView1.AxesGrid = 'GridAxes3DActor'
renderView1.CenterOfRotation = [0.6244999766349792, 0.10000000149011612, 0.0]
renderView1.StereoType = 'Crystal Eyes'
renderView1.CameraPosition = [0.6244999766349792, 0.10000000149011612, 10000.0]
renderView1.CameraFocalPoint = [0.6244999766349792, 0.10000000149011612, 0.0]
renderView1.CameraFocalDisk = 1.0
renderView1.CameraParallelScale = 0.6324557068404971
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

# create a new 'Fluent Case Reader'
sYS100010datgzcas = FluentCaseReader(FileName=[casedics])
sYS100010datgzcas.CellArrayStatus = ['PRESSURE', 'X_VELOCITY', 'Y_VELOCITY', '', 'DENSITY', 'MU_LAM']

# create a new 'Cell Data to Point Data'
cellDatatoPointData1 = CellDatatoPointData(Input=sYS100010datgzcas)
cellDatatoPointData1.CellDataArraytoprocess = ['', 'DENSITY', 'MU_LAM', 'PRESSURE', 'X_VELOCITY', 'Y_VELOCITY']

# ----------------------------------------------------------------
# setup the visualization in view 'renderView1'
# ----------------------------------------------------------------

# show data from cellDatatoPointData1
cellDatatoPointData1Display = Show(cellDatatoPointData1, renderView1, 'UnstructuredGridRepresentation')

# get color transfer function/color map for 'X_VELOCITY'
x_VELOCITYLUT = GetColorTransferFunction('X_VELOCITY')
x_VELOCITYLUT.RGBPoints = [-0.07610550576889022, 0.231373, 0.298039, 0.752941, 0.1182600609852921, 0.865003, 0.865003, 0.865003, 0.31262562773947444, 0.705882, 0.0156863, 0.14902]
x_VELOCITYLUT.ScalarRangeInitialized = 1.0

# get opacity transfer function/opacity map for 'X_VELOCITY'
x_VELOCITYPWF = GetOpacityTransferFunction('X_VELOCITY')
x_VELOCITYPWF.Points = [-0.07610550576889022, 0.0, 0.5, 0.0, 0.31262562773947444, 1.0, 0.5, 0.0]
x_VELOCITYPWF.ScalarRangeInitialized = 1

# trace defaults for the display properties.
cellDatatoPointData1Display.Representation = 'Surface'
cellDatatoPointData1Display.ColorArrayName = ['POINTS', 'X_VELOCITY']
cellDatatoPointData1Display.LookupTable = x_VELOCITYLUT
cellDatatoPointData1Display.OSPRayScaleArray = 'DENSITY'
cellDatatoPointData1Display.OSPRayScaleFunction = 'PiecewiseFunction'
cellDatatoPointData1Display.SelectOrientationVectors = 'DENSITY'
cellDatatoPointData1Display.ScaleFactor = 0.12489999532699586
cellDatatoPointData1Display.SelectScaleArray = 'DENSITY'
cellDatatoPointData1Display.GlyphType = 'Arrow'
cellDatatoPointData1Display.GlyphTableIndexArray = 'DENSITY'
cellDatatoPointData1Display.GaussianRadius = 0.006244999766349793
cellDatatoPointData1Display.SetScaleArray = ['POINTS', 'DENSITY']
cellDatatoPointData1Display.ScaleTransferFunction = 'PiecewiseFunction'
cellDatatoPointData1Display.OpacityArray = ['POINTS', 'DENSITY']
cellDatatoPointData1Display.OpacityTransferFunction = 'PiecewiseFunction'
cellDatatoPointData1Display.DataAxesGrid = 'GridAxesRepresentation'
cellDatatoPointData1Display.PolarAxes = 'PolarAxesRepresentation'
cellDatatoPointData1Display.ScalarOpacityFunction = x_VELOCITYPWF
cellDatatoPointData1Display.ScalarOpacityUnitDistance = 0.04180148576925318
cellDatatoPointData1Display.ExtractedBlockIndex = 1

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
cellDatatoPointData1Display.OSPRayScaleFunction.Points = [0.008018268893823101, 0.0, 0.5, 0.0, 2.3, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
cellDatatoPointData1Display.ScaleTransferFunction.Points = [1.225000023841858, 0.0, 0.5, 0.0, 1.225244164466858, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
cellDatatoPointData1Display.OpacityTransferFunction.Points = [1.225000023841858, 0.0, 0.5, 0.0, 1.225244164466858, 1.0, 0.5, 0.0]

# setup the color legend parameters for each legend in this view

# get color legend/bar for x_VELOCITYLUT in view renderView1
x_VELOCITYLUTColorBar = GetScalarBar(x_VELOCITYLUT, renderView1)
x_VELOCITYLUTColorBar.WindowLocation = 'AnyLocation'
x_VELOCITYLUTColorBar.Title = 'X_VELOCITY'
x_VELOCITYLUTColorBar.ComponentTitle = ''
x_VELOCITYLUTColorBar.ScalarBarLength = 0.7008439897698198

# set color bar visibility
x_VELOCITYLUTColorBar.Visibility = 1

# show color legend
cellDatatoPointData1Display.SetScalarBarVisibility(renderView1, True)

# ----------------------------------------------------------------
# setup color maps and opacity mapes used in the visualization
# note: the Get..() functions create a new object, if needed
# ----------------------------------------------------------------

# ----------------------------------------------------------------
# finally, restore active source
SetActiveSource(cellDatatoPointData1)
# ----------------------------------------------------------------