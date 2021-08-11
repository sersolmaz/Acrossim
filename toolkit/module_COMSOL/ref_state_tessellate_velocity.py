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
renderView1.StereoType = 'Crystal Eyes'
renderView1.CameraPosition = [0.0, 0.0, 10000.0]
renderView1.CameraFocalDisk = 1.0
renderView1.CameraParallelScale = 0.14142135623730953
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
mergedpvd = PVDReader(FileName='D:/Engineering/PhD/System_Architecture/5_software_development_one-way/6_SOFTWARE_Final/A_software_final/2_acrossim_toolkit_update2_11082021/module_COMSOL/velocity_isothermal/merged.pvd')
mergedpvd.PointArrays = ['Color']

# ----------------------------------------------------------------
# setup the visualization in view 'renderView1'
# ----------------------------------------------------------------

# show data from mergedpvd
mergedpvdDisplay = Show(mergedpvd, renderView1, 'UnstructuredGridRepresentation')

# get color transfer function/color map for 'Color'
colorLUT = GetColorTransferFunction('Color')
colorLUT.RGBPoints = [0.0, 0.231373, 0.298039, 0.752941, 0.040883908185664036, 0.865003, 0.865003, 0.865003, 0.08176781637132807, 0.705882, 0.0156863, 0.14902]
colorLUT.ScalarRangeInitialized = 1.0

# get opacity transfer function/opacity map for 'Color'
colorPWF = GetOpacityTransferFunction('Color')
colorPWF.Points = [0.0, 0.0, 0.5, 0.0, 0.08176781637132807, 1.0, 0.5, 0.0]
colorPWF.ScalarRangeInitialized = 1

# trace defaults for the display properties.
mergedpvdDisplay.Representation = 'Surface'
mergedpvdDisplay.ColorArrayName = ['POINTS', 'Color']
mergedpvdDisplay.LookupTable = colorLUT
mergedpvdDisplay.OSPRayScaleArray = 'Color'
mergedpvdDisplay.OSPRayScaleFunction = 'PiecewiseFunction'
mergedpvdDisplay.SelectOrientationVectors = 'Color'
mergedpvdDisplay.ScaleFactor = 0.020000000000000004
mergedpvdDisplay.SelectScaleArray = 'Color'
mergedpvdDisplay.GlyphType = 'Arrow'
mergedpvdDisplay.GlyphTableIndexArray = 'Color'
mergedpvdDisplay.GaussianRadius = 0.001
mergedpvdDisplay.SetScaleArray = ['POINTS', 'Color']
mergedpvdDisplay.ScaleTransferFunction = 'PiecewiseFunction'
mergedpvdDisplay.OpacityArray = ['POINTS', 'Color']
mergedpvdDisplay.OpacityTransferFunction = 'PiecewiseFunction'
mergedpvdDisplay.DataAxesGrid = 'GridAxesRepresentation'
mergedpvdDisplay.PolarAxes = 'PolarAxesRepresentation'
mergedpvdDisplay.ScalarOpacityFunction = colorPWF
mergedpvdDisplay.ScalarOpacityUnitDistance = 0.016767355837079674

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
mergedpvdDisplay.OSPRayScaleFunction.Points = [0.008018268893823101, 0.0, 0.5, 0.0, 2.3, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
mergedpvdDisplay.ScaleTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 0.08176781637132807, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
mergedpvdDisplay.OpacityTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 0.08176781637132807, 1.0, 0.5, 0.0]

# setup the color legend parameters for each legend in this view

# get color legend/bar for colorLUT in view renderView1
colorLUTColorBar = GetScalarBar(colorLUT, renderView1)
colorLUTColorBar.WindowLocation = 'AnyLocation'
colorLUTColorBar.Title = 'Color'
colorLUTColorBar.ComponentTitle = ''
colorLUTColorBar.ScalarBarLength = 0.7008439897698198

# set color bar visibility
colorLUTColorBar.Visibility = 1

# show color legend
mergedpvdDisplay.SetScalarBarVisibility(renderView1, True)

# ----------------------------------------------------------------
# setup color maps and opacity mapes used in the visualization
# note: the Get..() functions create a new object, if needed
# ----------------------------------------------------------------

# ----------------------------------------------------------------
# finally, restore active source
SetActiveSource(mergedpvd)
# ----------------------------------------------------------------