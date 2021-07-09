import subprocess
import sys
import os

# path to python.exe
python_exe = os.path.join(sys.prefix, 'bin', 'python.exe')

# upgrade pip
subprocess.call([python_exe, "-m", "ensurepip"])
subprocess.call([python_exe, "-m", "pip", "install", "--upgrade", "pip"])

# install required packages
subprocess.call([python_exe, "-m", "pip", "install", "pyproj"])
subprocess.call([python_exe, "-m", "pip", "install", "Shapely-1.7.1-cp37-cp37m-win_amd64.whl"])
subprocess.call([python_exe, "-m", "pip", "install", "Fiona-1.8.18-cp37-cp37m-win_amd64.whl"])
subprocess.call([python_exe, "-m", "pip", "install", "GDAL-3.2.2-cp37-cp37m-win_amd64.whl"])
subprocess.call([python_exe, "-m", "pip", "install", "geopandas-0.9.0-py2.py3-none-any.whl"])