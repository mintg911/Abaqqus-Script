# python:language_level=3
#-*- coding:utf-8 -*-
from abaqus import *
from abaqusConstants import *
from caeModules import *
from WovenFabric_CoreD import *
from driverUtils import executeOnCaeStartup
import math
import os


## 模型定义
# inp 文件名
inpfile = 'Plain_90.inp'
# Abaqus 模型名称(不同job使用不同名字，避免覆盖)
modelName = 'Fabric-Plain'
# Weft 和 Warp 纱线数量
Warp, Weft, = 2 , 2
# 模型的长和高 mm
Wx, Wy = 2.0, 2.0
# 加载类型：X, Y, XY
load_Type = 'X'
# 加载等效应变
load_Dis = 0.02

# 开始运行模型

Import_TexGen(modelName,inpfile)
Material_Orientation(modelName, Warp, Weft )
Face_Sets(modelName)
Insert_Equations_2D_Fabric(modelName,Wx, Wy)
Loading(modelName,load_Type, load_Dis)

# 在job管理提交
