# -*- coding: utf-8 -*-
"""
Created on Mon Mar  1 17:25:03 2021

@author: u0127798
"""

import os
import glob
import gzip
import shutil
from pathlib import Path

# Load paraview staff
from paraview.simple import *

"""
for casfile in glob.glob("*.cas.gz"):
    with gzip.open(casfile, 'rb') as f_in:
        with open(casfile + '.cas', 'wb') as f_out:
            shutil.copyfileobj(f_in, f_out)
        
for datfile in glob.glob("*.dat.gz"):
    with gzip.open(datfile, 'rb') as f_in:
        with open(datfile +'.dat', 'wb') as f_out:
            shutil.copyfileobj(f_in, f_out)     
"""

for casfile in glob.glob("*.cas.gz"):
    with gzip.open(casfile, 'rb') as f_in:
        with open(casfile + '.cas', 'wb') as f_out:
            shutil.copyfileobj(f_in, f_out)
        
for datfile in glob.glob("*.dat.gz"):
    with gzip.open(datfile, 'rb') as f_in:
        with open(datfile +'.dat', 'wb') as f_out:
            shutil.copyfileobj(f_in, f_out) 

for casfile1 in glob.glob("*.cas"):
    for datfile1 in glob.glob("*.dat"):
        with open(casfile1, 'rb') as f_in:
            datfile2 = Path(datfile1).stem + ""
            with open(datfile2 + '.cas', 'wb') as f_out:
                shutil.copyfileobj(f_in, f_out)

casedic=[]
for casfilename in glob.glob("*dat.gz.cas"):
    #casedic.append('C:/Users/u0127798/Desktop/trial_final/ansys/' + casfilename)
    casedic.append(os.getcwd() + '/' + casfilename)

print (casedic)
print (len(casedic))
number_casedic = len(casedic)


#casedic = 'C:/Users/u0127798/Desktop/trial/case_cfd/fluent/SYS-1-00010.dat.gz.cas'

#exec(open('fluent_state.py').read())
#from fluent_state import casedic
#fluent_state.casedic = 'C:/Users/u0127798/Desktop/trial/case_cfd/fluent/SYS-1-00010.dat.gz.cas'
#print (casedic)


