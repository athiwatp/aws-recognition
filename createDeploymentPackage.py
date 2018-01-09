from zipfile import ZipFile
from shutil import make_archive
import os

DIRNAME = "$VIRTUAL_ENV/lib/python3.6/site-packages"
#make_archive("DeploymentPackage", 'zip', DIRNAME)
with ZipFile('DeploymentPackage.zip', 'a') as myzip:
    myzip.write('lambda_function.py')