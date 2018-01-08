from zipfile import ZipFile
from shutil import make_archive
import os

DIRNAME = "C:\\Users\\Moritz\\Anaconda3\\envs\\aws_lambda\\Lib\\site-packages"
#make_archive("DeploymentPackage", 'zip', DIRNAME)
with ZipFile('DeploymentPackage.zip', 'a') as myzip:
    myzip.write('lambda_function.py')