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
renderView1.InteractionMode = '2D'
renderView1.AxesGrid = 'GridAxes3DActor'
renderView1.CenterOfRotation = [0.13469999562948942, 0.0, 0.0]
renderView1.StereoType = 'Crystal Eyes'
renderView1.CameraPosition = [0.14860103313588072, -0.007520685223408244, 0.6080086693737206]
renderView1.CameraFocalPoint = [0.14860103313588072, -0.007520685223408244, 0.0]
renderView1.CameraFocalDisk = 1.0
renderView1.CameraParallelScale = 0.13005307704244665
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
openFOAMReader1 = OpenFOAMReader(FileName='D:/Engineering/PhD/System_Architecture/5_software_development_one-way/6_SOFTWARE_Final/A_software_final/2_acrossim_toolkit_update2_11082021/module_OpenFOAM/pitzDaily_LES/pitzDaily_LES.foam')

openFOAMReader1.MeshRegions = ['internalMesh']
openFOAMReader1.CellArrays = ['U', 'UMean', 'UPrime2Mean', 'U_0', 'k', 'k_0', 'nut', 'p', 'pMean', 'pPrime2Mean', 's', 's_0']

# create a new 'Glyph'
glyph1 = Glyph(Input=openFOAMReader1,
    GlyphType='Arrow')
glyph1.OrientationArray = ['POINTS', 'U']
glyph1.ScaleArray = ['POINTS', 'U']
glyph1.ScaleFactor = 0.001
glyph1.GlyphTransform = 'Transform2'

# ----------------------------------------------------------------
# setup the visualization in view 'renderView1'
# ----------------------------------------------------------------

# show data from glyph1
glyph1Display = Show(glyph1, renderView1, 'GeometryRepresentation')

# get color transfer function/color map for 'U_0'
u_0LUT = GetColorTransferFunction('U_0')
u_0LUT.RGBPoints = [0.08958900416556008, 0.231373, 0.298039, 0.752941, 10.339581050069693, 0.865003, 0.865003, 0.865003, 20.589573095973826, 0.705882, 0.0156863, 0.14902]
u_0LUT.ScalarRangeInitialized = 1.0

# trace defaults for the display properties.
glyph1Display.Representation = 'Surface'
glyph1Display.ColorArrayName = ['POINTS', 'U_0']
glyph1Display.LookupTable = u_0LUT
glyph1Display.OSPRayScaleArray = 'p'
glyph1Display.OSPRayScaleFunction = 'PiecewiseFunction'
glyph1Display.SelectOrientationVectors = 'None'
glyph1Display.ScaleFactor = 1.206897258758545
glyph1Display.SelectScaleArray = 'p'
glyph1Display.GlyphType = 'Arrow'
glyph1Display.GlyphTableIndexArray = 'p'
glyph1Display.GaussianRadius = 0.06034486293792725
glyph1Display.SetScaleArray = ['POINTS', 'p']
glyph1Display.ScaleTransferFunction = 'PiecewiseFunction'
glyph1Display.OpacityArray = ['POINTS', 'p']
glyph1Display.OpacityTransferFunction = 'PiecewiseFunction'
glyph1Display.DataAxesGrid = 'GridAxesRepresentation'
glyph1Display.PolarAxes = 'PolarAxesRepresentation'

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
glyph1Display.OSPRayScaleFunction.Points = [0.008018268893823101, 0.0, 0.5, 0.0, 2.3, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
glyph1Display.ScaleTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 222.43824768066406, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
glyph1Display.OpacityTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 222.43824768066406, 1.0, 0.5, 0.0]

# setup the color legend parameters for each legend in this view

# get color legend/bar for u_0LUT in view renderView1
u_0LUTColorBar = GetScalarBar(u_0LUT, renderView1)
u_0LUTColorBar.Orientation = 'Horizontal'
u_0LUTColorBar.WindowLocation = 'AnyLocation'
u_0LUTColorBar.Position = [0.12109665520389984, 0.7620529801324504]
u_0LUTColorBar.Title = 'U_0'
u_0LUTColorBar.ComponentTitle = 'Magnitude'
u_0LUTColorBar.ScalarBarLength = 0.70084398976982

# set color bar visibility
u_0LUTColorBar.Visibility = 1

# show color legend
glyph1Display.SetScalarBarVisibility(renderView1, True)

# ----------------------------------------------------------------
# setup color maps and opacity mapes used in the visualization
# note: the Get..() functions create a new object, if needed
# ----------------------------------------------------------------

# get opacity transfer function/opacity map for 'U_0'
u_0PWF = GetOpacityTransferFunction('U_0')
u_0PWF.Points = [0.08958900416556008, 0.0, 0.5, 0.0, 20.589573095973826, 1.0, 0.5, 0.0]
u_0PWF.ScalarRangeInitialized = 1

# ----------------------------------------------------------------
# finally, restore active source
SetActiveSource(glyph1)
# ----------------------------------------------------------------