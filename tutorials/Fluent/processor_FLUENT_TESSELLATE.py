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

f = open('logfile_tessellate.txt', 'w')
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
    
    exportParaview = 'x3d'
    export_format_paraview = '.' + exportParaview
    import_format_blender = export_format_paraview
    exportBlender = 'fbx'
    export_format_blender = '.' + exportBlender
    
    path_metadata = 'process/metadata/'
    os.makedirs(path_metadata, exist_ok=True)
    path_paraview = os.getcwd() + '/' + path_metadata
    path_blender = path_paraview
    path_unityfor = os.getcwd() + '/' + 'process/'
    # define total number of timesteps
    timestep_sim = 1;
        
    for x in range(0, timestep_sim):
        #paraview metadata export
        ExportView(path_paraview + str(x) + export_format_paraview, view=renderView1, ExportColorLegends=1)
        SaveScreenshot(path_paraview + str(x) + '.png', renderView1, ImageResolution=[1025, 782])
        #animationScene1 = GetAnimationScene() #added later to define animationScene1
        #animationScene1.GoToNext()
        #blender starts metadata import & export
        path_to_obj_dir = os.path.join(path_blender)
        # get list of all files in directory
        file_list = sorted(os.listdir(path_to_obj_dir))
        # get a list of files ending in 'obj'
        obj_list = [item for item in file_list if item.endswith(import_format_blender)]
        # loop through the strings in obj_list and add the files to the scene
        for item in obj_list:
            path_to_file = os.path.join(path_to_obj_dir, item)
            bpy.ops.import_scene.x3d(filepath = path_to_file)
            # if heavy importing is expected 
            # you may want use saving to main file after every import 
            # bpy.ops.wm.save_mainfile(filepath = "C:\\To\\Your\\File.blend")
        # get the current path and make a new folder for the exported meshes
        path_blender = bpy.path.abspath(path_blender)
        for object in bpy.context.selected_objects:
            # deselect all meshes
            bpy.ops.object.select_all(action='DESELECT')
            # select the object
            object.select = True
            # export object with its name as file name
            bpy.ops.export_scene.fbx(filepath=path_blender + object.name + str(statefile) + '_timestep' + str(i+1) +  '_' + export_format_blender,use_selection=True,)

stop2 = timeit.default_timer()   

"""
Data processing analytics for qualitative studies (3)
"""
        
b_x3d = os.path.getsize(path_blender + '0.x3d')
print('*****Data processing performance & analytics*****')
print('Time_ParaView: ', stop1 - start1)
print('X3D file size in bytes:',b_x3d)
print('Time_ParaView_Blender: ', stop2 - start2)
path_to_obj_dir = os.path.join(path_blender)
file_list = sorted(os.listdir(path_to_obj_dir))
obj_list = [item for item in file_list if item.endswith('.fbx')]
size_file_blender = []
for item in obj_list:
    path_to_file = os.path.join(path_to_obj_dir, item)
    size_processing_blender=os.path.getsize(path_to_file)
    print('FBX file sizes in bytes:',size_processing_blender)
    size_file_blender.append(size_processing_blender)
#print("The maximum is {:.1f}".format(max(size_file_blender)))
#print('Time_Unity (sec): ', stop3 - start3)
#print('Time_Integration (sec): ', stop3 - start3 + stop2 - start2 + stop1 - start1)
print('Time_Integration (sec): ', stop2 - start2 + stop1 - start1)
print('Data size compression ratio X3D/FBX:', b_x3d/max(size_file_blender))
print('Data processing has successfully been completed!')

#clean up metadata
metadata = input ('Clean all metadata? [y or n]: ')

mypath = path_paraview
if metadata == 'y':
    for mydata in glob.glob(mypath + "Shape*"):
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

