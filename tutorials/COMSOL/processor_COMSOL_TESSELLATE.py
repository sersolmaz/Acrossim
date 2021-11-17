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

f = open('logfile_tessellate.txt', 'w')
original = sys.stdout
sys.stdout = Tee(sys.stdout, f)
print ("Data processing is in progress...")  #This will go to stdout and the file out.txt

"""
ParaView state file operation (1)
"""

#COMSOL streamline data to construct geometry from VTU file
qStreamline = input ('Is the processed data streamline, glyph or point in VTU format [y or n]?: ')   

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
exportParaview = 'x3d'
export_format_paraview = '.' + exportParaview

import_format_blender = export_format_paraview
#data format to export visual CFD data from Blender: fbx, obj, 3ds, ply, stl and other supported formats
#(optional) exportBlender = input ('Enter the export format Blender: ')
exportBlender = 'fbx'
export_format_blender = '.' + exportBlender

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
    ExportView(path_paraview + str(x) + export_format_paraview, view=renderView1, ExportColorLegends=1)
    #check out the data processed 
    SaveScreenshot(path_paraview + str(x) + '.png', renderView1, ImageResolution=[1025, 782])
    #switch to the next timestep
    animationScene1 = GetAnimationScene() 
    animationScene1.GoToNext()
    #blender starts metadata import & export
    path_to_obj_dir = os.path.join(path_blender)
    #get list of all files in directory
    file_list = sorted(os.listdir(path_to_obj_dir))
    #get a list of files ending in 'obj' in Blender
    obj_list = [item for item in file_list if item.endswith(import_format_blender)]
    #loop through the strings in obj_list and add the files to the scene
    for item in obj_list:
        path_to_file = os.path.join(path_to_obj_dir, item)
        bpy.ops.import_scene.x3d(filepath = path_to_file)
        # data recuperation for COMSOL streamline files in VTU format
        if qStreamline == 'y':
            scene = bpy.context.scene
            scene.layers = [True] * 20 # Show all layers
            for obj in scene.objects:
                if obj.type == 'CURVE':
                    scene.objects.active = obj
                    bpy.ops.object.mode_set(mode='EDIT')
                    bpy.context.object.data.bevel_depth = 0.005
                    bpy.context.object.data.bevel_resolution = 1
                    bpy.context.object.data.fill_mode = 'FULL'
                    bpy.ops.object.mode_set(mode='OBJECT')
        else: 
            print('')
    #get the current path and make a new folder for the exported meshes
    path_blender = bpy.path.abspath(path_blender)
    for object in bpy.context.selected_objects:
        #deselect all meshes
        bpy.ops.object.select_all(action='DESELECT')
        #select the object
        object.select = True
        #export object with its name as file name
        if timestep_sim >1:
            bpy.ops.export_scene.fbx(filepath=path_blender + object.name + str(statefile) + '_timestep' + str(x+1) + '_time' + str(tsteps[x]) + '_' + export_format_blender,use_selection=True,)
        else:
            bpy.ops.export_scene.fbx(filepath=path_blender + object.name + str(statefile) + '_timestep1_' + export_format_blender,use_selection=True,)

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
