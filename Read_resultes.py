# 2023-03-20
# Code to read composite ply stress state
# By MingM.xu

from abaqus import *
from abaqusConstants import *
from driverUtils import executeOnCaeStartup
import math
import os
import odbAccess
import odbMaterial
import odbSection
import numpy as np
# import pandas as pd

jobName = 'CFRP05_STATIC'
Model_name = 'PART-1-1'
Step_name = 'Step-1'

#:    Number of nodes: 3317
#:    Number of elements: 2432
#:    Element types: C3D8IC3 

Open3 = session.openOdb(jobName+'.odb')
session.viewports['Viewport: 1'].setValues(displayedObject=Open3)
Mat_all = {'BX610LASHEN':[630, 502, 618, 515, 83.7, 41],'WS3000ALASHEN':[1410, 925, 65.6, 161, 75.4, 69.6]}
Allsets = ['GROUP01_BT01','GROUP01_BT02','GROUP01_BT03','GROUP01_BT04']



def Read_Date(jobName,Model_name,Step_name,Mat_all,SetName):
	rODB = session.openOdb(jobName+'.odb')
	# ('11', '22', '33', '12', '13', '23').
	# ( 11, -11, 22, -22, 12, 23).

	# print rODB.sections
	# print rODB.sections['Section-GROUP01_BT01']
	# print rODB.sections['Section-GROUP01_BT01'].layup[16]
	# print len(rODB.sections['Section-GROUP01_BT01'].layup) # 17
	# print rODB.sections['Section-GROUP01_BT01'].layup[10].material #
	# print rODB.sections['Section-GROUP01_BT01'].layup[10].angle #
	# print rODB.materials['WS3000ALASHEN']
	# print Mat_all['BX610LASHEN']
	# return()
	# Group 1
	secMaterial = rODB.sections['Section-'+SetName]
	Group1 = rODB.rootAssembly.instances[Model_name].elementSets[SetName]
	# print 'Elements number:', len(eles)
	StreeField = rODB.steps[Step_name].frames[-1].fieldOutputs['S']
	dict_Group = []
	for ele in Group1.elements:
		data_Ele = StreeField.getSubset(region=ele)
		for i in data_Ele.values:
			# if i==2:
				# print '25%'
			# elif i==5:
				# print '50%'
			# elif i==7:
				# print '75%'
			# print i.sectionPoint.number
			Tag1 = i.elementLabel             # 
			Tag2 = int((i.sectionPoint.number-1)//3) # layer number
			# print Tag2
			Tag3 = i.integrationPoint
			if (secMaterial.layup[Tag2].material == 'BX610LASHEN'):
				Tag4 = 1
			elif (secMaterial.layup[Tag2].material == 'WS3000ALASHEN'):
				Tag4 = 2
			Tag5 = list(i.data)
			new_Ddict = [Tag1,Tag2+1,Tag3,Tag4]+Tag5
			
			# Failure state 1- Max stress
			km = Mat_all[secMaterial.layup[Tag2].material]
			if (Tag5[0]>=0):
				f1 = abs(Tag5[0]/km[0])
				X = 1/km[0]**2
			else:
				f1 = abs(Tag5[0]/km[1])
				X = 1/km[1]**2
			if (Tag5[1]>=0):
				f2 = abs(Tag5[1]/km[2])
				Y = 1/km[2]**2
			else:
				f2 = abs(Tag5[1]/km[3])
				Y = 1/km[3]**2
			if (Tag5[2]>=0):
				f3 = abs(Tag5[2]/km[2])
				Z = 1/km[2]**2
			else:
				f3 = abs(Tag5[2]/km[3])
				Z = 1/km[3]**2
			f4 = abs(Tag5[3]/km[4])
			f5 = abs(Tag5[4]/km[4])
			f6 = abs(Tag5[5]/km[5])
			MAXF = max(f1,f2,f3,f4,f5,f6)
			Tag6 = 1.0 - 1.0/MAXF
			# Failure state 2- Tasi-Wu
			F11=1.0/km[0]/km[1]
			F22=1.0/km[2]/km[3]
			F33=F22
			F44=1.0/km[4]/km[4]
			F55=F44
			F66=1.0/km[5]/km[5]  
			F12=-0.5*sqrt(F11*F22)
			F13=F12    
			F23=F22-0.5*F44    
			F1=1.0/km[0]-1.0/km[1]
			F2=1.0/km[2]-1.0/km[3]
			F3=F2
			TsaiWu = (F11*Tag5[0]**2 + F22*Tag5[1]**2 + F33*Tag5[2]**2
				+ F44*Tag5[3]**2 + F55*Tag5[4]**2 + F66*Tag5[5]**2 
				+ 2.0*F12*Tag5[0]*Tag5[1]+2.0*F13*Tag5[0]*Tag5[2] + 2.0*F23*Tag5[1]*Tag5[2]
				+ F1*Tag5[0]+F2*Tag5[1]+F3*Tag5[2] ) 
			Tag7 = 1.0 - 1.0/TsaiWu
			# Failure state 3- Tsai-Hill 
			Q = 1/km[4]**2
			R = 1/km[4]**2
			S = 1/km[5]**2
			TsaiHILL=(X*Tag5[0]**2+Y*Tag5[1]**2+Z*Tag5[2]**2
				+ Q*Tag5[3]**2+R*Tag5[4]**2+S*Tag5[5]**2   
				- (X+Y-Z)*Tag5[0]*Tag5[1]
				- (X-Y+Z)*F13*Tag5[0]*Tag5[2]
				- (-X+Y+Z)*F23*Tag5[1]*Tag5[2] )
			Tag8 = 1.0 - 1.0/TsaiHILL
			# Failure state 4- Yamada-Sun 
			Q = 1/km[4]**2
			YamadaSun =sqrt(X*Tag5[0]**2+Q*Tag5[3]**2)    
			Tag9 = 1.0 - 1.0/YamadaSun
			# print Tag6,Tag7,Tag8,Tag9
			new_Ddict = new_Ddict + [Tag6,Tag7,Tag8,Tag9]
			dict_Group.append(new_Ddict)
			# print i.sectionPoint.description # {'description': 'fraction = -0.647059, Layer = 3'}
			# print i.sectionPoint.number # {'number': 9}, 1-3->layer_1, 4-6->Layer2
			# print secMaterial.layup[i.sectionPoint.number//3-1].material
			# print secMaterial.layup[i.sectionPoint.number//3-1].angle
			# print dict
		# ('11', '22', '33', '12', '13', '23').
	All = np.array(dict_Group)
	# np.savetxt('Group1_Resultes.txt',All,fmt='%0.8f')
	fmtall = ('%d','%d','%d','%d','%0.8f','%0.8f','%0.8f','%0.8f','%0.8f','%0.8f','%0.8f','%0.8f','%0.8f','%0.8f')
	header1 = 'Element,Layer,IntegrationPoint,Material,S11,S22,S33,S12,S13,S23,MaxStress,Tsai-Wu,Tsai-Hill,Yamada-Sun'
	np.savetxt(SetName+'_Resultes.csv', All, fmt=fmtall, delimiter=',',encoding='utf-8',header=header1,comments='')

	# key1 = np.array(dict_S.keys())
	# values1 = np.array(dict_S.values())
	# dict1 = np.column_stack((key1.transpose(),values1))
	# np.savetxt('name.txt',dict1,fmt='%0.8f')
		
		
		
		
		
# print rODB.rootAssembly.instances[Model_name].elements[i].sectionCategory
# ({'baseElementType': 'C3D8IC3', 'data': array([-7.28764533996582, -0.0291101112961769, 0.0420856773853302, -26.1914100646973, -0.823677361011505, 0.324239939451218], 'f'),
# 'elementLabel': 11010001, 'instance': 'OdbInstance object', 'integrationPoint': 1, 
# 'inv3': -28.463586807251, 'localCoordSystem': ((1.0, 0.0, 0.0), (0.0, 1.0, 0.0), (0.0, 0.0, 1.0)), 
# 'localCoordSystemDouble': 'unknown', 'magnitude': None, 'maxInPlanePrincipal': 0.0, 
# 'maxPrincipal': 22.8103866577148, 'midPrincipal': 0.0205115433782339, 'minInPlanePrincipal': 0.0, 'minPrincipal': -30.1055679321289, 'tresca': 52.9159545898438, 'mises': 45.9731330871582, 'outOfPlanePrincipal': 0.0, 
# 'position': INTEGRATION_POINT, 'precision': SINGLE_PRECISION, 
# 'press': 2.42489004135132, 
# 'sectionPoint': 'SectionPoint object',  'type': TENSOR_3D_FULL})
#
 # 'sectionPoint': 'SectionPoint object' ->({'description': 'SNEG, (fraction = -1.0), Layer = 1', 'number': 1})


for set in Allsets:
	Read_Date(jobName,Model_name,Step_name,Mat_all,set)
	
	