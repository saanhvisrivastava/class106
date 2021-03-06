# -*- coding: utf-8 -*-
"""class106.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1iUNnQB1GrDXyXavWiuEviE8A4YBgaZMO
"""

import csv
import numpy as np

def getDataSource(data_path):
  size=[]
  timespent=[]
  with open(data_path)as csv_file:
    csv_reader=csv.DictReader(csv_file)
    for row in csv_reader:
      size.append(float(row["Size of TV"]))
      timespent.append(float(row[", Average time spent watching TV in a week (hours)"]))
  return{"x":size,"y":timespent}

def correlation(datasource):
  correlation=np.corrcoef(datasource["x"],datasource["y"])
  print("correlation is /n--->",correlation[0,1])

def setup():
  data_path="DataTv.csv"
  datasource=getDataSource(data_path)
  correlation(datasource)

setup()