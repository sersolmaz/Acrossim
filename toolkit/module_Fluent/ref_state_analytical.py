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
lineChartView1.ViewSize = [490, 755]
lineChartView1.SortByXAxis = 1
lineChartView1.LegendPosition = [454, 276]
lineChartView1.LeftAxisTitle = 'dd'
lineChartView1.LeftAxisRangeMinimum = 0.06
lineChartView1.LeftAxisRangeMaximum = 0.21
lineChartView1.BottomAxisTitle = 'dd'
lineChartView1.BottomAxisRangeMinimum = 0.05
lineChartView1.BottomAxisRangeMaximum = 0.30000000000000004
lineChartView1.RightAxisRangeMaximum = 6.66
lineChartView1.TopAxisRangeMaximum = 6.66

# get the material library
materialLibrary1 = GetMaterialLibrary()

# Create a new 'Render View'
renderView1 = CreateView('RenderView')
renderView1.ViewSize = [491, 755]
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
layout1.SplitHorizontal(0, 0.500000)
layout1.AssignView(1, renderView1)
layout1.AssignView(2, lineChartView1)

# ----------------------------------------------------------------
# restore active view
SetActiveView(lineChartView1)
# ----------------------------------------------------------------

# ----------------------------------------------------------------
# setup the data processing pipelines
# ----------------------------------------------------------------

# create a new 'Fluent Case Reader'
sYS100010datgzcas = FluentCaseReader(FileName=[casedics])
sYS100010datgzcas.CellArrayStatus = ['PRESSURE', 'X_VELOCITY', 'Y_VELOCITY', '', 'DENSITY', 'MU_LAM']

# create a new 'Plot Over Line'
plotOverLine1 = PlotOverLine(Input=sYS100010datgzcas,
    Source='High Resolution Line Source')

# init the 'High Resolution Line Source' selected for 'Source'
plotOverLine1.Source.Point1 = [0.12, -0.09717200264039398, 0.0]
plotOverLine1.Source.Point2 = [0.12, 0.3373811101614795, 0.0]

# ----------------------------------------------------------------
# setup the visualization in view 'lineChartView1'
# ----------------------------------------------------------------

# show data from plotOverLine1
plotOverLine1Display = Show(plotOverLine1, lineChartView1, 'XYChartRepresentation')

# trace defaults for the display properties.
plotOverLine1Display.CompositeDataSetIndex = [0]
plotOverLine1Display.UseIndexForXAxis = 0
plotOverLine1Display.XArrayName = 'arc_length'
plotOverLine1Display.SeriesVisibility = ['X_VELOCITY']
plotOverLine1Display.SeriesLabel = ['arc_length', 'arc_length', 'DENSITY', 'DENSITY', 'MU_LAM', 'MU_LAM', 'PRESSURE', 'PRESSURE', 'vtkValidPointMask', 'vtkValidPointMask', 'X_VELOCITY', 'X_VELOCITY', 'Y_VELOCITY', 'Y_VELOCITY', 'Points_X', 'Points_X', 'Points_Y', 'Points_Y', 'Points_Z', 'Points_Z', 'Points_Magnitude', 'Points_Magnitude']
plotOverLine1Display.SeriesColor = ['arc_length', '0', '0', '0', 'DENSITY', '0.889998', '0.100008', '0.110002', 'MU_LAM', '0.220005', '0.489998', '0.719997', 'PRESSURE', '0.300008', '0.689998', '0.289998', 'vtkValidPointMask', '0.6', '0.310002', '0.639994', 'X_VELOCITY', '1', '0.500008', '0', 'Y_VELOCITY', '0.650004', '0.340002', '0.160006', 'Points_X', '0', '0', '0', 'Points_Y', '0.889998', '0.100008', '0.110002', 'Points_Z', '0.220005', '0.489998', '0.719997', 'Points_Magnitude', '0.300008', '0.689998', '0.289998']
plotOverLine1Display.SeriesPlotCorner = ['DENSITY', '0', 'MU_LAM', '0', 'PRESSURE', '0', 'Points_Magnitude', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'X_VELOCITY', '0', 'Y_VELOCITY', '0', 'arc_length', '0', 'vtkValidPointMask', '0']
plotOverLine1Display.SeriesLabelPrefix = ''
plotOverLine1Display.SeriesLineStyle = ['DENSITY', '1', 'MU_LAM', '1', 'PRESSURE', '1', 'Points_Magnitude', '1', 'Points_X', '1', 'Points_Y', '1', 'Points_Z', '1', 'X_VELOCITY', '1', 'Y_VELOCITY', '1', 'arc_length', '1', 'vtkValidPointMask', '1']
plotOverLine1Display.SeriesLineThickness = ['DENSITY', '2', 'MU_LAM', '2', 'PRESSURE', '2', 'Points_Magnitude', '2', 'Points_X', '2', 'Points_Y', '2', 'Points_Z', '2', 'X_VELOCITY', '2', 'Y_VELOCITY', '2', 'arc_length', '2', 'vtkValidPointMask', '2']
plotOverLine1Display.SeriesMarkerStyle = ['DENSITY', '0', 'MU_LAM', '0', 'PRESSURE', '0', 'Points_Magnitude', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'X_VELOCITY', '0', 'Y_VELOCITY', '0', 'arc_length', '0', 'vtkValidPointMask', '0']
plotOverLine1Display.SeriesMarkerSize = ['DENSITY', '4', 'MU_LAM', '4', 'PRESSURE', '4', 'Points_Magnitude', '4', 'Points_X', '4', 'Points_Y', '4', 'Points_Z', '4', 'X_VELOCITY', '4', 'Y_VELOCITY', '4', 'arc_length', '4', 'vtkValidPointMask', '4']

# ----------------------------------------------------------------
# setup the visualization in view 'renderView1'
# ----------------------------------------------------------------

# show data from sYS100010datgzcas
sYS100010datgzcasDisplay = Show(sYS100010datgzcas, renderView1, 'UnstructuredGridRepresentation')

# get color transfer function/color map for 'X_VELOCITY'
x_VELOCITYLUT = GetColorTransferFunction('X_VELOCITY')
x_VELOCITYLUT.RGBPoints = [-0.07732146559926571, 0.231373, 0.298039, 0.752941, 0.11875680739494239, 0.865003, 0.865003, 0.865003, 0.3148350803891505, 0.705882, 0.0156863, 0.14902]
x_VELOCITYLUT.ScalarRangeInitialized = 1.0

# get opacity transfer function/opacity map for 'X_VELOCITY'
x_VELOCITYPWF = GetOpacityTransferFunction('X_VELOCITY')
x_VELOCITYPWF.Points = [-0.07732146559926571, 0.0, 0.5, 0.0, 0.3148350803891505, 1.0, 0.5, 0.0]
x_VELOCITYPWF.ScalarRangeInitialized = 1

# trace defaults for the display properties.
sYS100010datgzcasDisplay.Representation = 'Surface'
sYS100010datgzcasDisplay.ColorArrayName = ['CELLS', 'X_VELOCITY']
sYS100010datgzcasDisplay.LookupTable = x_VELOCITYLUT
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
sYS100010datgzcasDisplay.ScalarOpacityFunction = x_VELOCITYPWF
sYS100010datgzcasDisplay.ScalarOpacityUnitDistance = 0.04180148576925318
sYS100010datgzcasDisplay.ExtractedBlockIndex = 1

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
sYS100010datgzcasDisplay.OSPRayScaleFunction.Points = [0.008018268893823101, 0.0, 0.5, 0.0, 2.3, 1.0, 0.5, 0.0]

# show data from plotOverLine1
plotOverLine1Display_1 = Show(plotOverLine1, renderView1, 'GeometryRepresentation')

# trace defaults for the display properties.
plotOverLine1Display_1.Representation = 'Surface'
plotOverLine1Display_1.ColorArrayName = [None, '']
plotOverLine1Display_1.OSPRayScaleArray = 'DENSITY'
plotOverLine1Display_1.OSPRayScaleFunction = 'PiecewiseFunction'
plotOverLine1Display_1.SelectOrientationVectors = 'DENSITY'
plotOverLine1Display_1.ScaleFactor = 0.043455312401056295
plotOverLine1Display_1.SelectScaleArray = 'DENSITY'
plotOverLine1Display_1.GlyphType = 'Arrow'
plotOverLine1Display_1.GlyphTableIndexArray = 'DENSITY'
plotOverLine1Display_1.GaussianRadius = 0.0021727656200528143
plotOverLine1Display_1.SetScaleArray = ['POINTS', 'DENSITY']
plotOverLine1Display_1.ScaleTransferFunction = 'PiecewiseFunction'
plotOverLine1Display_1.OpacityArray = ['POINTS', 'DENSITY']
plotOverLine1Display_1.OpacityTransferFunction = 'PiecewiseFunction'
plotOverLine1Display_1.DataAxesGrid = 'GridAxesRepresentation'
plotOverLine1Display_1.PolarAxes = 'PolarAxesRepresentation'

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
plotOverLine1Display_1.OSPRayScaleFunction.Points = [0.008018268893823101, 0.0, 0.5, 0.0, 2.3, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
plotOverLine1Display_1.ScaleTransferFunction.Points = [1.225000023841858, 0.0, 0.5, 0.0, 1.225244164466858, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
plotOverLine1Display_1.OpacityTransferFunction.Points = [1.225000023841858, 0.0, 0.5, 0.0, 1.225244164466858, 1.0, 0.5, 0.0]

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
sYS100010datgzcasDisplay.SetScalarBarVisibility(renderView1, True)

# ----------------------------------------------------------------
# setup color maps and opacity mapes used in the visualization
# note: the Get..() functions create a new object, if needed
# ----------------------------------------------------------------

# ----------------------------------------------------------------
# finally, restore active source
SetActiveSource(plotOverLine1)
# ----------------------------------------------------------------