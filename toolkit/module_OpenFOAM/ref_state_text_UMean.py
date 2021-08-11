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

# Create a new 'Line Chart View'
lineChartView1 = CreateView('XYChartView')
lineChartView1.ViewSize = [666, 755]
lineChartView1.SortByXAxis = 1
lineChartView1.LegendPosition = [497, 709]
lineChartView1.LeftAxisTitle = 'y-axis'
lineChartView1.LeftAxisRangeMaximum = 6.5
lineChartView1.BottomAxisTitle = 'UMean_Magnitude'
lineChartView1.BottomAxisRangeMaximum = 0.045
lineChartView1.RightAxisRangeMaximum = 6.66
lineChartView1.TopAxisRangeMaximum = 6.66

# get the material library
materialLibrary1 = GetMaterialLibrary()

# Create a new 'Render View'
renderView1 = CreateView('RenderView')
renderView1.ViewSize = [450, 755]
renderView1.InteractionMode = '2D'
renderView1.AxesGrid = 'GridAxes3DActor'
renderView1.CenterOfRotation = [0.13469999562948942, 0.0, 0.0]
renderView1.StereoType = 'Crystal Eyes'
renderView1.CameraPosition = [0.15583577384552683, -0.007176173761044144, 0.6080086693737206]
renderView1.CameraFocalPoint = [0.15583577384552683, -0.007176173761044144, 0.0]
renderView1.CameraFocalDisk = 1.0
renderView1.CameraParallelScale = 0.23039695921839412
renderView1.BackEnd = 'OSPRay raycaster'
renderView1.OSPRayMaterialLibrary = materialLibrary1

SetActiveView(None)

# ----------------------------------------------------------------
# setup view layouts
# ----------------------------------------------------------------

# create new layout object 'Layout #1'
layout1 = CreateLayout(name='Layout #1')
layout1.SplitHorizontal(0, 0.403710)
layout1.AssignView(1, renderView1)
layout1.AssignView(2, lineChartView1)

# ----------------------------------------------------------------
# restore active view
SetActiveView(lineChartView1)
# ----------------------------------------------------------------

# ----------------------------------------------------------------
# setup the data processing pipelines
# ----------------------------------------------------------------

# create a new 'OpenFOAMReader'
pitzDaily_LESfoam = OpenFOAMReader(FileName='D:/Engineering/PhD/System_Architecture/5_software_development_one-way/6_SOFTWARE_Final/A_software_final/2_acrossim_toolkit_update2_11082021/module_OpenFOAM/pitzDaily_LES/pitzDaily_LES.foam')
pitzDaily_LESfoam.MeshRegions = ['internalMesh']
pitzDaily_LESfoam.CellArrays = ['U', 'UMean', 'UPrime2Mean', 'U_0', 'k', 'k_0', 'nut', 'p', 'pMean', 'pPrime2Mean', 's', 's_0']

# create a new 'Plot Over Line'
plotOverLine1 = PlotOverLine(Input=pitzDaily_LESfoam,
    Source='High Resolution Line Source')

# init the 'High Resolution Line Source' selected for 'Source'
plotOverLine1.Source.Point1 = [0.25, -0.022988419456487278, -0.0005000000237487465]
plotOverLine1.Source.Point2 = [0.25, 0.02126586214466692, 0.0005000000237487361]

# ----------------------------------------------------------------
# setup the visualization in view 'lineChartView1'
# ----------------------------------------------------------------

# show data from plotOverLine1
plotOverLine1Display = Show(plotOverLine1, lineChartView1, 'XYChartRepresentation')

# trace defaults for the display properties.
plotOverLine1Display.CompositeDataSetIndex = [0]
plotOverLine1Display.UseIndexForXAxis = 0
plotOverLine1Display.XArrayName = 'arc_length'
plotOverLine1Display.SeriesVisibility = ['UMean_Magnitude']
plotOverLine1Display.SeriesLabel = ['arc_length', 'arc_length', 'k', 'k', 'k_0', 'k_0', 'nut', 'nut', 'p', 'p', 'pMean', 'pMean', 'pPrime2Mean', 'pPrime2Mean', 's', 's', 's_0', 's_0', 'U_X', 'U_X', 'U_Y', 'U_Y', 'U_Z', 'U_Z', 'U_Magnitude', 'U_Magnitude', 'U_0_X', 'U_0_X', 'U_0_Y', 'U_0_Y', 'U_0_Z', 'U_0_Z', 'U_0_Magnitude', 'U_0_Magnitude', 'UMean_X', 'UMean_X', 'UMean_Y', 'UMean_Y', 'UMean_Z', 'UMean_Z', 'UMean_Magnitude', 'UMean_Magnitude', 'UPrime2Mean_XX', 'UPrime2Mean_XX', 'UPrime2Mean_YY', 'UPrime2Mean_YY', 'UPrime2Mean_ZZ', 'UPrime2Mean_ZZ', 'UPrime2Mean_XY', 'UPrime2Mean_XY', 'UPrime2Mean_YZ', 'UPrime2Mean_YZ', 'UPrime2Mean_XZ', 'UPrime2Mean_XZ', 'UPrime2Mean_Magnitude', 'UPrime2Mean_Magnitude', 'vtkValidPointMask', 'vtkValidPointMask', 'Points_X', 'Points_X', 'Points_Y', 'Points_Y', 'Points_Z', 'Points_Z', 'Points_Magnitude', 'Points_Magnitude']
plotOverLine1Display.SeriesColor = ['arc_length', '0', '0', '0', 'k', '0.889998', '0.100008', '0.110002', 'k_0', '0.220005', '0.489998', '0.719997', 'nut', '0.300008', '0.689998', '0.289998', 'p', '0.6', '0.310002', '0.639994', 'pMean', '1', '0.500008', '0', 'pPrime2Mean', '0.650004', '0.340002', '0.160006', 's', '0', '0', '0', 's_0', '0.889998', '0.100008', '0.110002', 'U_X', '0.220005', '0.489998', '0.719997', 'U_Y', '0.300008', '0.689998', '0.289998', 'U_Z', '0.6', '0.310002', '0.639994', 'U_Magnitude', '1', '0.500008', '0', 'U_0_X', '0.650004', '0.340002', '0.160006', 'U_0_Y', '0', '0', '0', 'U_0_Z', '0.889998', '0.100008', '0.110002', 'U_0_Magnitude', '0.220005', '0.489998', '0.719997', 'UMean_X', '0.300008', '0.689998', '0.289998', 'UMean_Y', '0.6', '0.310002', '0.639994', 'UMean_Z', '1', '0.500008', '0', 'UMean_Magnitude', '0.650004', '0.340002', '0.160006', 'UPrime2Mean_XX', '0', '0', '0', 'UPrime2Mean_YY', '0.889998', '0.100008', '0.110002', 'UPrime2Mean_ZZ', '0.220005', '0.489998', '0.719997', 'UPrime2Mean_XY', '0.300008', '0.689998', '0.289998', 'UPrime2Mean_YZ', '0.6', '0.310002', '0.639994', 'UPrime2Mean_XZ', '1', '0.500008', '0', 'UPrime2Mean_Magnitude', '0.650004', '0.340002', '0.160006', 'vtkValidPointMask', '0', '0', '0', 'Points_X', '0.889998', '0.100008', '0.110002', 'Points_Y', '0.220005', '0.489998', '0.719997', 'Points_Z', '0.300008', '0.689998', '0.289998', 'Points_Magnitude', '0.6', '0.310002', '0.639994']
plotOverLine1Display.SeriesPlotCorner = ['Points_Magnitude', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'UMean_Magnitude', '0', 'UMean_X', '0', 'UMean_Y', '0', 'UMean_Z', '0', 'UPrime2Mean_Magnitude', '0', 'UPrime2Mean_XX', '0', 'UPrime2Mean_XY', '0', 'UPrime2Mean_XZ', '0', 'UPrime2Mean_YY', '0', 'UPrime2Mean_YZ', '0', 'UPrime2Mean_ZZ', '0', 'U_0_Magnitude', '0', 'U_0_X', '0', 'U_0_Y', '0', 'U_0_Z', '0', 'U_Magnitude', '0', 'U_X', '0', 'U_Y', '0', 'U_Z', '0', 'arc_length', '0', 'k', '0', 'k_0', '0', 'nut', '0', 'p', '0', 'pMean', '0', 'pPrime2Mean', '0', 's', '0', 's_0', '0', 'vtkValidPointMask', '0']
plotOverLine1Display.SeriesLabelPrefix = ''
plotOverLine1Display.SeriesLineStyle = ['Points_Magnitude', '1', 'Points_X', '1', 'Points_Y', '1', 'Points_Z', '1', 'UMean_Magnitude', '1', 'UMean_X', '1', 'UMean_Y', '1', 'UMean_Z', '1', 'UPrime2Mean_Magnitude', '1', 'UPrime2Mean_XX', '1', 'UPrime2Mean_XY', '1', 'UPrime2Mean_XZ', '1', 'UPrime2Mean_YY', '1', 'UPrime2Mean_YZ', '1', 'UPrime2Mean_ZZ', '1', 'U_0_Magnitude', '1', 'U_0_X', '1', 'U_0_Y', '1', 'U_0_Z', '1', 'U_Magnitude', '1', 'U_X', '1', 'U_Y', '1', 'U_Z', '1', 'arc_length', '1', 'k', '1', 'k_0', '1', 'nut', '1', 'p', '1', 'pMean', '1', 'pPrime2Mean', '1', 's', '1', 's_0', '1', 'vtkValidPointMask', '1']
plotOverLine1Display.SeriesLineThickness = ['Points_Magnitude', '2', 'Points_X', '2', 'Points_Y', '2', 'Points_Z', '2', 'UMean_Magnitude', '2', 'UMean_X', '2', 'UMean_Y', '2', 'UMean_Z', '2', 'UPrime2Mean_Magnitude', '2', 'UPrime2Mean_XX', '2', 'UPrime2Mean_XY', '2', 'UPrime2Mean_XZ', '2', 'UPrime2Mean_YY', '2', 'UPrime2Mean_YZ', '2', 'UPrime2Mean_ZZ', '2', 'U_0_Magnitude', '2', 'U_0_X', '2', 'U_0_Y', '2', 'U_0_Z', '2', 'U_Magnitude', '2', 'U_X', '2', 'U_Y', '2', 'U_Z', '2', 'arc_length', '2', 'k', '2', 'k_0', '2', 'nut', '2', 'p', '2', 'pMean', '2', 'pPrime2Mean', '2', 's', '2', 's_0', '2', 'vtkValidPointMask', '2']
plotOverLine1Display.SeriesMarkerStyle = ['Points_Magnitude', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'UMean_Magnitude', '0', 'UMean_X', '0', 'UMean_Y', '0', 'UMean_Z', '0', 'UPrime2Mean_Magnitude', '0', 'UPrime2Mean_XX', '0', 'UPrime2Mean_XY', '0', 'UPrime2Mean_XZ', '0', 'UPrime2Mean_YY', '0', 'UPrime2Mean_YZ', '0', 'UPrime2Mean_ZZ', '0', 'U_0_Magnitude', '0', 'U_0_X', '0', 'U_0_Y', '0', 'U_0_Z', '0', 'U_Magnitude', '0', 'U_X', '0', 'U_Y', '0', 'U_Z', '0', 'arc_length', '0', 'k', '0', 'k_0', '0', 'nut', '0', 'p', '0', 'pMean', '0', 'pPrime2Mean', '0', 's', '0', 's_0', '0', 'vtkValidPointMask', '0']
plotOverLine1Display.SeriesMarkerSize = ['Points_Magnitude', '4', 'Points_X', '4', 'Points_Y', '4', 'Points_Z', '4', 'UMean_Magnitude', '4', 'UMean_X', '4', 'UMean_Y', '4', 'UMean_Z', '4', 'UPrime2Mean_Magnitude', '4', 'UPrime2Mean_XX', '4', 'UPrime2Mean_XY', '4', 'UPrime2Mean_XZ', '4', 'UPrime2Mean_YY', '4', 'UPrime2Mean_YZ', '4', 'UPrime2Mean_ZZ', '4', 'U_0_Magnitude', '4', 'U_0_X', '4', 'U_0_Y', '4', 'U_0_Z', '4', 'U_Magnitude', '4', 'U_X', '4', 'U_Y', '4', 'U_Z', '4', 'arc_length', '4', 'k', '4', 'k_0', '4', 'nut', '4', 'p', '4', 'pMean', '4', 'pPrime2Mean', '4', 's', '4', 's_0', '4', 'vtkValidPointMask', '4']

# ----------------------------------------------------------------
# setup the visualization in view 'renderView1'
# ----------------------------------------------------------------

# show data from pitzDaily_LESfoam
pitzDaily_LESfoamDisplay = Show(pitzDaily_LESfoam, renderView1, 'UnstructuredGridRepresentation')

# get color transfer function/color map for 'U'
uLUT = GetColorTransferFunction('U')
uLUT.RGBPoints = [0.021387763448225697, 0.231373, 0.298039, 0.752941, 9.390945915204915, 0.865003, 0.865003, 0.865003, 18.7605040669616, 0.705882, 0.0156863, 0.14902]
uLUT.ScalarRangeInitialized = 1.0

# get opacity transfer function/opacity map for 'U'
uPWF = GetOpacityTransferFunction('U')
uPWF.Points = [0.021387763448225697, 0.0, 0.5, 0.0, 18.7605040669616, 1.0, 0.5, 0.0]
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

# show data from plotOverLine1
plotOverLine1Display_1 = Show(plotOverLine1, renderView1, 'GeometryRepresentation')

# get color transfer function/color map for 'p'
pLUT = GetColorTransferFunction('p')
pLUT.RGBPoints = [0.0, 0.231373, 0.298039, 0.752941, 113.1917495727539, 0.865003, 0.865003, 0.865003, 226.3834991455078, 0.705882, 0.0156863, 0.14902]
pLUT.ScalarRangeInitialized = 1.0

# trace defaults for the display properties.
plotOverLine1Display_1.Representation = 'Surface'
plotOverLine1Display_1.ColorArrayName = ['POINTS', 'p']
plotOverLine1Display_1.LookupTable = pLUT
plotOverLine1Display_1.OSPRayScaleArray = 'p'
plotOverLine1Display_1.OSPRayScaleFunction = 'PiecewiseFunction'
plotOverLine1Display_1.SelectOrientationVectors = 'U'
plotOverLine1Display_1.ScaleFactor = 0.004425428248941899
plotOverLine1Display_1.SelectScaleArray = 'p'
plotOverLine1Display_1.GlyphType = 'Arrow'
plotOverLine1Display_1.GlyphTableIndexArray = 'p'
plotOverLine1Display_1.GaussianRadius = 0.0002212714124470949
plotOverLine1Display_1.SetScaleArray = ['POINTS', 'p']
plotOverLine1Display_1.ScaleTransferFunction = 'PiecewiseFunction'
plotOverLine1Display_1.OpacityArray = ['POINTS', 'p']
plotOverLine1Display_1.OpacityTransferFunction = 'PiecewiseFunction'
plotOverLine1Display_1.DataAxesGrid = 'GridAxesRepresentation'
plotOverLine1Display_1.PolarAxes = 'PolarAxesRepresentation'

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
plotOverLine1Display_1.OSPRayScaleFunction.Points = [0.008018268893823101, 0.0, 0.5, 0.0, 2.3, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
plotOverLine1Display_1.ScaleTransferFunction.Points = [41.47943878173828, 0.0, 0.5, 0.0, 42.6285285949707, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
plotOverLine1Display_1.OpacityTransferFunction.Points = [41.47943878173828, 0.0, 0.5, 0.0, 42.6285285949707, 1.0, 0.5, 0.0]

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

# get opacity transfer function/opacity map for 'p'
pPWF = GetOpacityTransferFunction('p')
pPWF.Points = [0.0, 0.0, 0.5, 0.0, 226.3834991455078, 1.0, 0.5, 0.0]
pPWF.ScalarRangeInitialized = 1

# ----------------------------------------------------------------
# finally, restore active source
SetActiveSource(plotOverLine1)
# ----------------------------------------------------------------