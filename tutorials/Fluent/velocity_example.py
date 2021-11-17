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
renderView1.ViewSize = [854, 435]
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

# ----------------------------------------------------------------
# setup the visualization in view 'renderView1'
# ----------------------------------------------------------------

# show data from sYS100010datgzcas
sYS100010datgzcasDisplay = Show(sYS100010datgzcas, renderView1, 'UnstructuredGridRepresentation')

# get color transfer function/color map for 'PRESSURE'
pRESSURELUT = GetColorTransferFunction('PRESSURE')
pRESSURELUT.RGBPoints = [-0.03669620447521329, 0.231373, 0.298039, 0.752941, 0.002807382133212695, 0.865003, 0.865003, 0.865003, 0.04231096874163868, 0.705882, 0.0156863, 0.14902]
pRESSURELUT.ScalarRangeInitialized = 1.0

# get opacity transfer function/opacity map for 'PRESSURE'
pRESSUREPWF = GetOpacityTransferFunction('PRESSURE')
pRESSUREPWF.Points = [-0.03669620447521329, 0.0, 0.5, 0.0, 0.04231096874163868, 1.0, 0.5, 0.0]
pRESSUREPWF.ScalarRangeInitialized = 1

# trace defaults for the display properties.
sYS100010datgzcasDisplay.Representation = 'Surface'
sYS100010datgzcasDisplay.ColorArrayName = ['CELLS', 'PRESSURE']
sYS100010datgzcasDisplay.LookupTable = pRESSURELUT
sYS100010datgzcasDisplay.OSPRayScaleFunction = 'PiecewiseFunction'
sYS100010datgzcasDisplay.ScaleFactor = 0.12489999532699586
sYS100010datgzcasDisplay.GlyphType = 'Arrow'
sYS100010datgzcasDisplay.GaussianRadius = 0.006244999766349793
sYS100010datgzcasDisplay.SetScaleArray = [None, '']
sYS100010datgzcasDisplay.ScaleTransferFunction = 'PiecewiseFunction'
sYS100010datgzcasDisplay.OpacityArray = [None, '']
sYS100010datgzcasDisplay.OpacityTransferFunction = 'PiecewiseFunction'
sYS100010datgzcasDisplay.DataAxesGrid = 'GridAxesRepresentation'
sYS100010datgzcasDisplay.PolarAxes = 'PolarAxesRepresentation'
sYS100010datgzcasDisplay.ScalarOpacityFunction = pRESSUREPWF
sYS100010datgzcasDisplay.ScalarOpacityUnitDistance = 0.04180148576925318
sYS100010datgzcasDisplay.ExtractedBlockIndex = 1

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
sYS100010datgzcasDisplay.OSPRayScaleFunction.Points = [0.008018268893823101, 0.0, 0.5, 0.0, 2.3, 1.0, 0.5, 0.0]

# setup the color legend parameters for each legend in this view

# get color legend/bar for pRESSURELUT in view renderView1
pRESSURELUTColorBar = GetScalarBar(pRESSURELUT, renderView1)
pRESSURELUTColorBar.WindowLocation = 'AnyLocation'
pRESSURELUTColorBar.Title = 'PRESSURE'
pRESSURELUTColorBar.ComponentTitle = ''
pRESSURELUTColorBar.ScalarBarLength = 0.7008439897698198

# set color bar visibility
pRESSURELUTColorBar.Visibility = 1

# show color legend
sYS100010datgzcasDisplay.SetScalarBarVisibility(renderView1, True)

# ----------------------------------------------------------------
# setup color maps and opacity mapes used in the visualization
# note: the Get..() functions create a new object, if needed
# ----------------------------------------------------------------

# ----------------------------------------------------------------
# finally, restore active source
SetActiveSource(sYS100010datgzcas)
# ----------------------------------------------------------------