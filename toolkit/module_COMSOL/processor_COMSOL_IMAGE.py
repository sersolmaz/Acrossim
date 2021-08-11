# -*- coding: utf-8 -*-
"""
Created on February 2021
@author: Serkan Solmaz
"""

import os, glob
import sys
import subprocess
import timeit
import shutil
from distutils.dir_util import copy_tree
from paraview.simple import *
from paraview.simple import paraview
import vtk
import bpy

"""
logging of operations from terminal and save in a text file
"""

class Tee(object):
    def __init__(self, *files):
        self.files = files
    def write(self, obj):
        for f in self.files:
            f.write(obj)
            f.flush() #If you want the output to be visible immediately
    def flush(self) :
        for f in self.files:
            f.flush()

f = open('logfile_image.txt', 'w')
original = sys.stdout
sys.stdout = Tee(sys.stdout, f)
print ("Data processing is in progress...")  #This will go to stdout and the file out.txt

"""
ParaView state file operation (1)
"""

#timer for each section - data processing speed
start1 = timeit.default_timer()
#input user-defined paraview_state (either name with extension or full directory)
statefile = input ('Enter the state file: ')        
#import user-defined paraview_state
exec(open(statefile).read())

#update the view to ensure updated data information
renderView1 = GetActiveViewOrCreate('RenderView')
renderView1.Update()
stop1 = timeit.default_timer()

"""
Data processing via ParaView and Blender pipeline (2)
"""

start2 = timeit.default_timer()
#data format to export visual CFD data from ParaView: x3d, vrml, svg and other supported formats
#(optional) exportParaview = input ('Enter the export format from ParaView: ')
exportParaview = 'png'
export_format_paraview = '.' + exportParaview

#create a directory to collect processed data and metadata
path_metadata = 'process/metadata/'
os.makedirs(path_metadata, exist_ok=True)
path_paraview = os.getcwd() + '/' + path_metadata
path_blender = path_paraview
path_unityfor = os.getcwd() + '/' + 'process/'

#define total number of timesteps (1 for steady-state solutions)
timestep_sim = int(input ('Total number of timesteps (1 for steady-state): '))

#obtain a list of timesteps with values
animationScene1 = GetAnimationScene() 
tsteps = animationScene1.TimeKeeper.TimestepValues

for x in range(0, timestep_sim):
    #paraview metadata export
    if timestep_sim >1:
        SaveScreenshot(path_paraview + str(statefile) + '_timestep' + str(x+1) + '_time' + str(tsteps[x]) + '_' + export_format_paraview, lineChartView1, ImageResolution=[490, 755])
    else:
        SaveScreenshot(path_paraview + str(statefile) + '_timestep1_' + export_format_paraview, lineChartView1, ImageResolution=[490, 755])
    #switch to the next timestep
    animationScene1 = GetAnimationScene() 
    animationScene1.GoToNext()
      
stop2 = timeit.default_timer()   

"""
Data processing analytics for qualitative studies (3)
"""

#clean up metadata
metadata = input ('Clean all metadata? [y or n]: ')

mypath = path_paraview
if metadata == 'y':
    for mydata in glob.glob(mypath + '*.png'):
        shutil.copy(mydata, os.getcwd() + '/' + 'process/')
    for mydata in glob.glob(mypath + '*.bmp'):
        shutil.copy(mydata, os.getcwd() + '/' + 'process/')
    for metadata in glob.glob(mypath + "*"):
        os.remove(metadata)
    print ('Metadata is cleaned.')
else:
    print ('Metadata is available under the process directory.')
#self.text_comments.insert('end', open(filename,'r').read())

"""
Categorize and store data for cross-platfrom applications (4)
"""

start3 = timeit.default_timer()

#saving, categorizing and updating processed CFD data in a dedicated directory
unitysave = input ('Save as extracts in the database directory: ')
path_unity= 'CFD_database/' + unitysave
copy_tree(path_unityfor, path_unity)
#dirs_exist_ok=False

stop3 = timeit.default_timer()

"""
The end
"""

#exit
input('Press ENTER to exit')
