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
import os
import gzip
import shutil
from pathlib import Path
from distutils.dir_util import copy_tree
from paraview.simple import *
from paraview.simple import paraview
import vtk
import bpy
from fluenttoparaview import casedic, number_casedic

"""
logging of operations from terminal and save to a txt log file
"""

class Tee(object):
    def __init__(self, *files):
        self.files = files
    def write(self, obj):
        for f in self.files:
            f.write(obj)
            f.flush() # If you want the output to be visible immediately
    def flush(self) :
        for f in self.files:
            f.flush()

f = open('logfile_image.txt', 'w')
original = sys.stdout
sys.stdout = Tee(sys.stdout, f)
print ("Data processing is in progress...")  # This will go to stdout and the file out.txt

"""
Fluent data processing 
"""

#timer for each section - data processing speed
start1 = timeit.default_timer()

statefileprep = input ('Enter the state file: ')      

path = casedic[0]
pathCase = path.replace(os.sep, '/')

with open(statefileprep) as r:
  #text = r.read().replace("'flanders.dat.gz.cas'", 'casedics')
  #text = r.read().replace("FileName=['C:/Users/u0127798/Desktop/trial_final/ansys/SYS-1-00010.dat.gz.cas']", "FileName=[casedics]")
  text = r.read().replace("'" + pathCase + "'", "casedics")
with open(statefileprep, "w") as w:
  w.write(text)  

#import user-defined paraview_state
stop1 = timeit.default_timer()

"""
Data processing via ParaView and Blender pipeline (2)
"""

start2 = timeit.default_timer()

for i in range(number_casedic):

    casedics = casedic[i]

    #statefile = "fluent_state_final.py"
    statefile = statefileprep
    exec(open(statefile).read())
    
    # update the view to ensure updated data information
    renderView1.Update()
    # get color legend/bar for pLUT in view renderView1
    
    exportParaview = 'png'
    export_format_paraview = '.' + exportParaview
    import_format_blender = export_format_paraview
    
    path_metadata = 'process/metadata/'
    os.makedirs(path_metadata, exist_ok=True)
    path_paraview = os.getcwd() + '/' + path_metadata
    path_blender = path_paraview
    path_unityfor = os.getcwd() + '/' + 'process/'
    # define total number of timesteps
    timestep_sim = 1;
        
    for x in range(0, timestep_sim):
        #paraview metadata export
        #SaveScreenshot(path_paraview + str(statefile) + '_timestep' + str(i+1) +  '_' + export_format_paraview, renderView1, ImageResolution=[490, 755])
        SaveScreenshot(path_paraview + str(statefile) + '_timestep' + str(i+1) +  '_' + export_format_paraview)


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

