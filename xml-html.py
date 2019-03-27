# !/usr/bin/python
import subprocess
import os
import re

pattern = "\d+"
path ="./"
files = os.listdir(path)

for file in files:
    pattern = re.compile(pattern)
    x=re.findall(pattern,file)
    if x :
        xml=file
        html=x[0]+".html"

	subprocess.call(['xsltproc',xml,'-o',html])
        
print("------------------------------SUCESSSSS----------------------------------------------------")









