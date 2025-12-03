# Updates
# 2021-03-30
# 1. Using TexGen to create warp and weft tows
# 2. The orientation of the weft tows is constructed by the surface orientation
# 3. The height and rotation of the warp tow
# 4. The cross-section of the weft tow
from abaqus import *
from abaqusConstants import *
from caeModules import *
from driverUtils import executeOnCaeStartup
import math
import os
import numpy as np

# mdb.models['Model-1'].featureOptions.setValues(checkSelfIntersection=ON)
# print '#  _   _       _ _    ____     _ _         _____    #'
# print '# | | | |_ __ (_) |_ / ___|___| | |___    / ___ \   #'
# print '# | | | | `_ \| | __| |   / _ \ | / __|  / | _ \ \  #'
# print '# | |_| | | | | | |_| |___  __/ | \__ \ |  |   /  | #'
# print '#  \___/|_| |_|_|\__|\____\___|_|_|___/  \ |_|_\ /  #'
# print '#                                         \_____/   #'
def Input_Geometry_data():
	# Input some parameters.
	# getInputs returns strings.
	str_ModelName = '3D_Woven_S1-G1-D2-1'
	# str_ModelName = '3D_Woven_S1-G1-D2'
	str_offset = '0'
	str_Straight = '0'
	str_Step = '1'
	str_Skip = '2'
	str_Deep = '2'
	str_Steep = '2'
	# Weft Tow / axial Tow
	str_W_a = '2'
	str_H_a = '0.4'
	# Weft Tow spacing
	str_D_a = '2.5'
	# Warp Tow / binder Tow
	str_w_b = '2'
	str_h_b = '0.4'
	# weft Tow spacing
	str_d_b = '0.06'
	# Tow section
	str_SectionA = '0.5'
	str_SectionB = '0.5'
	# 0=rectangle, [0-1]=ellipetical round; 2=lenticular
	# mesh Size
	str_meshSize = '0.1'
	# read input file 
	file=open('Input_Geometric_Parameters.txt','a+')
	file.close
	file=open('Input_Geometric_Parameters.txt','r')
	s=file.readline()
	if(s!=''):
		str_offset = s
		str_Straight = file.readline()
		str_Step = file.readline()
		str_Skip = file.readline()
		str_Deep = file.readline()
		str_Steep = file.readline()
		str_W_a= file.readline()
		str_H_a= file.readline()
		str_D_a= file.readline()
		str_w_b= file.readline()
		str_h_b= file.readline()
		str_d_b= file.readline()
		str_SectionA= file.readline()
		str_SectionB= file.readline()
		str_meshSize= file.readline()
	file.close
	#
	offset = int(str_offset)
	Straight = int(str_Straight)
	Step = int(str_Step)
	Skip = int(str_Skip)
	Deep = int(str_Deep)
	Steep = int(str_Steep)
	W_a = float(str_W_a)
	H_a = float(str_H_a)
	D_a = float(str_D_a)
	w_b = float(str_w_b)
	h_b = float(str_h_b)
	d_b = float(str_d_b)
	SectionA = float(str_SectionA)
	SectionB = float(str_SectionB)
	meshSize = float(str_meshSize)
	#
	fieldsMatrix = (
		('Job name Skip-Deep-Step:',str(str_ModelName)),
		('Offset [0:OFF, -1:V; 1:H]:', str(offset)),
		('Straight Warp number:', str(Straight)),
		('Step of adjacent weft yarns:', str(Step)),
		('Skip of binder yarns span:', str(Skip)),
		('Deep of binding layers:', str(Deep)),
		('Steep of warp yarns:', str(Steep)),
		('Weft Tow Width   W_a:', str(W_a)),
		('Weft Tow Height  H_a:', str(H_a)),
		('Weft Tow Spacing D_a:', str(D_a)),
		('Warp Tow Width   w_b:', str(w_b)),
		('Warp Tow Height  h_b:', str(h_b)),
		('Warp Tow Spacing d_b:', str(d_b)),
		('Weft Tow Section (0,1]:', str(SectionA)),
		('Warp Tow Section [0,1]:', str(SectionB)),
		('Mesh Size:', str(meshSize)),)

	labelText = 'Enter the Geometric Parameters'
	dialogTitleText = 'Geometric_Parameters'
	ModelName,offset,Straight,Step,Skip,Deep,Steep,\
		W_a,H_a,D_a,w_b,h_b,d_b,SectionA,SectionB,meshSize = getInputs(
		fields=fieldsMatrix,
		label=labelText,
		dialogTitle=dialogTitleText,)
	#
	########### write the parameters to a file.
	s=offset+'\n'
	s=s+Straight+'\n'
	s=s+Step+'\n'
	s=s+Skip+'\n'
	s=s+Deep+'\n'
	s=s+Steep+'\n'
	s=s+str(W_a)+'\n'
	s=s+str(H_a)+'\n'
	s=s+str(D_a)+'\n'
	s=s+str(w_b)+'\n'
	s=s+str(h_b)+'\n'
	s=s+str(d_b)+'\n'
	s=s+SectionA+'\n'
	s=s+SectionB+'\n'
	s=s+meshSize+'\n'
	file=open('Input_Geometric_Parameters.txt','w')
	file.write(s)
	file.close
	file=open('Input_Geometric_Parameters.txt','a')
	file.close
	#
	offset = int(offset)
	Straight = int(Straight)
	Step = int(Step)
	Skip = int(Skip)
	Deep = int(Deep)
	Steep = int(Steep)
	W_a = float(W_a)
	H_a = float(H_a)
	D_a = float(D_a)
	w_b = float(w_b)
	h_b = float(h_b)
	d_b = float(d_b)
	SectionA = float(SectionA)
	SectionB = float(SectionB)
	Section = [SectionA,SectionB]
	meshSize = float(meshSize)
	if (Section[0] <= 0) or (Section[1] < 0):
		ErrorMessage(0)
		return(0)
	#
	return(ModelName,offset,Straight,Step,Skip,\
		Deep,Steep,W_a,H_a,D_a,w_b,h_b,d_b,Section,meshSize)
	
def Input_Material():
	############################## Input matrial parameters.	
	# getInputs returns strings.	
	#### matrix properties
	str_Em = '3380.0'
	str_vm = '0.30'
	#str_TEm = '0.001'
	### Axial weft Tow properties
	str_E1a = '3380.0'
	str_E2a = '3380.0'
	str_E3a = '3380.0'
	str_v12a= '0.30'
	str_v13a= '0.30'
	str_v23a= '0.30'
	str_G12a = '1300.0'
	str_G13a = '1300.0'
	str_G23a = '1300.0'
	
	### Bias warp Tow properties
	str_E1b = '3380.0'
	str_E2b = '3380.0'
	str_E3b = '3380.0'
	str_v12b= '0.30'
	str_v13b= '0.30'
	str_v23b= '0.30'
	str_G12b = '1300.0'
	str_G13b = '1300.0'
	str_G23b = '1300.0'
	
	file=open('Input_Mat_Yarns_Matrix.txt','a')
	file.close
	file=open('Input_Mat_Yarns_Matrix.txt','r')
	s=file.readline()
	if(s!=''):
		str_Em=s
		str_vm= file.readline()
		str_E1a = file.readline() 
		str_E2a = file.readline()
		str_E3a = file.readline()
		str_v12a= file.readline()
		str_v13a= file.readline()
		str_v23a= file.readline()
		str_G12a = file.readline()
		str_G13a =file.readline()
		str_G23a = file.readline()
		str_E1b = file.readline() 
		str_E2b = file.readline()
		str_E3b = file.readline()
		str_v12b= file.readline()
		str_v13b= file.readline()
		str_v23b= file.readline()
		str_G12b = file.readline()
		str_G13b =file.readline()
		str_G23b = file.readline()		   
	file.close		
	
	Em = float(str_Em)
	vm = float(str_vm)
	E1a= float(str_E1a)
	E2a = float(str_E2a)
	E3a = float(str_E3a)
	v12a= float(str_v12a)
	v13a= float(str_v13a)
	v23a= float(str_v23a)
	G12a = float(str_G12a)
	G13a = float(str_G13a)
	G23a = float(str_G23a)
	E1b= float(str_E1b)
	E2b = float(str_E2b)
	E3b = float(str_E3b)
	v12b= float(str_v12b)
	v13b= float(str_v13b)
	v23b= float(str_v23b)
	G12b = float(str_G12b)
	G13b = float(str_G13b)
	G23b = float(str_G23b)
	fieldsMatrix = (
		('Em:',str(Em)),
		('vm:',str(vm)),
		('E1a:', str(E1a)),
		('E2a:', str(E2a)),
		('E3a:', str(E3a)),
		('v12a:', str(v12a)),
		('v13a:', str(v13a)),
		('v23a:', str(v23a)),
		('G12a:', str(G12a)),
		('G13a:', str(G13a)),
		('G23a:', str(G23a)),
		('E1b:', str(E1b)),
		('E2b:', str(E2b)),
		('E3b:', str(E3b)),
		('v12b:', str(v12b)),
		('v13b:', str(v13b)),
		('v23b:', str(v23b)),
		('G12b:', str(G12b)),
		('G13b:', str(G13b)),
		('G23b:', str(G23b)),)

	labelText = 'Enter the material properties'
	dialogTitleText = 'Material properties : Elastic & Expansion'
	matArray = getInputs(
		fields=fieldsMatrix,
		label=labelText,
		dialogTitle=dialogTitleText,)
	
	########### write the parameters to a file.
	s=matArray[0]+'\n'
	s=s+matArray[1]+'\n' 
	s=s+matArray[2]+'\n' 
	s=s+matArray[3]+'\n' 
	s=s+matArray[4]+'\n'	 
	s=s+matArray[5]+'\n'	 
	s=s+matArray[6]+'\n'	 
	s=s+matArray[7]+'\n'			 
	s=s+matArray[8]+'\n' 
	s=s+matArray[9]+'\n' 
	s=s+matArray[10]+'\n'	 
	s=s+matArray[11]+'\n'
	s=s+matArray[12]+'\n' 
	s=s+matArray[13]+'\n' 
	s=s+matArray[14]+'\n'	  
	s=s+matArray[15]+'\n'	  
	s=s+matArray[16]+'\n'	  
	s=s+matArray[17]+'\n'			  
	s=s+matArray[18]+'\n' 
	s=s+matArray[19]

	file=open('Input_Mat_Yarns_Matrix.txt','w')
	file.write(s)
	file.close
	file=open('Input_Mat_Yarns_Matrix.txt','a')
	file.close
	return(matArray) 
	
def Input_Cohesive():
	############################## Input Cohesive parameters.	
	# getInputs returns strings.	
	#### matrix properties
	str_Failure = '1'
	str_Evolution = '1'
	str_En = '1e6'
	str_Gs = '1e6'
	str_Gt = '1e6'
	str_Sn = '73'
	str_Ss = '120'
	str_St = '120'
	str_GcI = '0.002665'  # Sn*Sn/En = 0.005329
	str_GcIIs = '0.0072'  # Sn*Sn/En = 0.0144
	str_GcIIt = '0.0072'
	str_Alpha = '2'
	str_m = '5'
	file=open('Input_Mat_Cohesive.txt','a')
	file.close
	file=open('Input_Mat_Cohesive.txt','r')
	s=file.readline()
	if(s!=''):
		str_Failure=s
		str_Evolution = file.readline()
		str_En = file.readline()
		str_Gs = file.readline()
		str_Gt = file.readline()
		str_Sn = file.readline()
		str_Ss = file.readline()
		str_St = file.readline()
		str_GcI = file.readline()
		str_GcIIs = file.readline()
		str_GcIIt = file.readline()
		str_Alpha = file.readline()
		str_m = file.readline()
	file.close		
	#
	Failure = float(str_Failure)
	Evolution = float(str_Evolution)
	En = float(str_En)
	Gs = float(str_Gs)
	Gt = float(str_Gt)
	Sn = float(str_Sn)
	Ss = float(str_Ss)
	St = float(str_St)
	GcI = float(str_GcI)
	GcIIs = float(str_GcIIs)
	GcIIt = float(str_GcIIt)
	Alpha = float(str_Alpha)
	m = float(str_m)
	fieldsMatrix = (
		('Stress/Disp.:',str(Failure)),
		('Evolution:',str(Evolution)),
		('Enn:',str(En)),
		('Ess:',str(Gs)),
		('Ett:', str(Gt)),
		('Snn:', str(Sn)),
		('Sss:', str(Ss)),
		('Stt:', str(St)),
		('GcI:', str(GcI)),
		('GcIIs:', str(GcIIs)),
		('GcIIt:', str(GcIIt)),
		('Alpha:', str(Alpha)),
		('m:', str(m)),)

	labelText = 'Damage modeling: 1-stress criterion;2-displacement criterion'
	dialogTitleText = 'Enter the Cohesive properties'
	matCohesive = getInputs(
		fields=fieldsMatrix,
		label=labelText,
		dialogTitle=dialogTitleText,)
	
	########### write the parameters to a file.
	s=matCohesive[0]+'\n'
	s=s+matCohesive[1]+'\n' 
	s=s+matCohesive[2]+'\n' 
	s=s+matCohesive[3]+'\n' 
	s=s+matCohesive[4]+'\n'	 
	s=s+matCohesive[5]+'\n'	 
	s=s+matCohesive[6]+'\n'	 
	s=s+matCohesive[7]+'\n'	 
	s=s+matCohesive[8]+'\n'	 
	s=s+matCohesive[9]+'\n'	 
	s=s+matCohesive[10]+'\n'
	s=s+matCohesive[11]+'\n'
	s=s+matCohesive[12]

	file=open('Input_Mat_Cohesive.txt','w')
	file.write(s)
	file.close
	file=open('Input_Mat_Cohesive.txt','a')
	file.close
	return(matCohesive) 
	
def func(Los,Xr,Yr,bb,a,b,d,t):
	k = -b*cos(t)/(a*sin(t))
	r = (a**2)*(sin(t)**2)+(b**2)*(cos(t)**2)
	xx = (a+ d*b/sqrt(r))*cos(t) + Los
	yy = (b+ d*a/sqrt(r))*sin(t) - bb
	k2 = (yy-Yr)/(xx-Xr)
	df = k-k2
	return df
# Normal Weaves
def Creat_Geometry_no_Offset(Straight,Step,Skip,Deep,Steep,W_a,H_a,D_a,w_b,h_b,d_b,Section,meshSize,d0,c1,c2):
	# Straight  number of straight warp
	# Step      step between two slices
	# skip      skip on the weft top
	# Deep      deep of warp 
	# Steep     steepness of warp
	n_z=Deep/Steep
	Long = 2*Skip*n_z
	Step = (Step+Long)%Long
	if Step !=0 and Step != Long and Steep <= Deep:
		print '### Architecture topological parametes are correct!'
	else:
		ErrorMessage(1)
		return(0)
	session.viewports['Viewport: 1'].makeCurrent()
	session.viewports['Viewport: 1'].maximize()
	executeOnCaeStartup()
	session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
		referenceRepresentation=ON)
	session.viewports['Viewport: 1'].view.setViewpoint(viewVector=(1.0, 0, 0), 
		cameraUpVector=(0, 0, 1))
	session.View(name='User-4', nearPlane=16.878, farPlane=50.635, width=3.0813, 
		height=14.848, projection=PARALLEL, cameraPosition=(33.756, 0, 0.8), 
		cameraUpVector=(0, 0, 1), cameraTarget=(0, 0, 0.8), viewOffsetX=0, 
		viewOffsetY=0, autoFit=ON)
	session.viewports['Viewport: 1'].view.setValues(session.views['User-4'])
	session.viewports['Viewport: 1'].maximize()
	Mdb()
	print '#   ____                      _               #'
	print '#  / ___| ___  ___  _ __ ___ | |_ _ __ _   _  #'
	print '# | |  _ / _ \/ _ \|  _ ` _ \| __| |__| | | | #'
	print '# | |_| |  __/ (_) | | | | | | |_| |  | |_| | #'
	print '#  \____|\___|\___/|_| |_| |_|\__|_|   \__, | #'
	print '#                                      |___/  #'
	#: A new model database has been created.
	#: The model "Model-1" has been created.
	#
	# average angle
	# h = h_b
	# D = D_a
	# H = H_a+(Steep-1)*(H_a+h_b)
	# if H==h:
		# Degree = 2*atan(H/D)
	# else:
		# Degree = 2*atan((-D+sqrt(D**2+H**2-h**2))/(H-h))
	# Degree2 = atan(Steep*(H_a+h_b)/(D_a+W_a))
	# Angle2 = degrees(Degree2)
	# print '### Average weaving angle is %0.2f' %(Angle2)
	#
	#d0 = 1.00
	#c1 = 1.00
	#c2 = 1.00
	H_top = c1*H_a
	H_bot = c2*H_a
	W_new = d0*W_a
	D_new = W_a+D_a - W_new
	n_z=Deep/Steep
	Long = 2*Skip*n_z
	Ly = Long*(W_a+D_a)
	Dz = ((H_top+H_bot)/2.0 + h_b)
	Wx = (w_b + d_b) 
	Wx = (Straight+1)*Wx
	print '### Size of Unit cell: Wx = %0.2f, Ly = %0.2f, Dz = %0.2f' %(Wx,Ly,Dz)
	#
	# #
	# for Section is Round Rectangular (Ellipse)
	# determine the Maximum interlocking angle
	gamma = Section[0]
	a = 0.5*gamma*W_a
	b = 0.5*H_a
	t1 = pi/2
	t0 = 0
	eps = 0.0000001
	delta = 1
	n = 0
	# print gamma,a,b,H_a,h_b
	while abs(delta)>eps:
		middle = 0.5*(t0+t1)
		n +=1
		if n > 199:
			break
		phi = middle
		delta=-a*(H_a+h_b)*sin(phi)+h_b*sqrt(b*b*cos(phi)*cos(phi)+a*a*sin(phi)*sin(phi))
		if delta > 0:
			t0 = middle
		else:
			t1 = middle
	# interlocking angle
	Angle_max = degrees(atan(b/a/tan(phi)))
	print '### Maximum interlocking angle = %0.2f' %(Angle_max)
	gamma = Section[0]
	a = 0.5*gamma*W_a
	b = 0.5*H_a
	r = sqrt(b*b*cos(phi)*cos(phi)+a*a*sin(phi)*sin(phi))
	D_min = (2*a+Steep*h_b*r/b)/cos(phi)-gamma*W_a
	print '### Minimum distance is %0.4f' %(D_min)
	# if (D_a < D_min):
		# ErrorMessage(2)
		# return(0)
#########################################################
	# determine the real interlocking angle
	D = D_a + gamma*W_a
	gamma = Section[0]
	a = 0.5*gamma*W_a
	b = 0.5*H_a
	t1 = pi/2
	t0 = 0
	eps = 0.0000001
	delta = 1
	n = 0
	# print gamma,a,b,H_a,h_b
	while abs(delta)>eps:
		middle = 0.5*(t0+t1)
		n +=1
		if n > 199:
			break
			print 'ERROR!\n Error input.'
		phi = middle
		delta=-a*(Steep-1)*(H_a+h_b)*sin(phi) \
			+D*b*cos(phi) -2*a*b \
			-h_b*sqrt(b*b*cos(phi)*cos(phi)+a*a*sin(phi)*sin(phi))
		if delta > 0:
			t0 = middle
		else:
			t1 = middle
	# interlocking angle
	Angle= degrees(atan(b/a/tan(phi)))
	print '### Original interlocking angle = %0.2f' %(Angle)
#
	# method 2 for angle
	H_top = c1*H_a
	H_bot = c2*H_a
	W_new = d0*W_a
	D_new = W_a+D_a - W_new
	
	aa = 0.5*(W_new+D_new)
	bb = 0.5*(H_top+h_b)
	gamma = Section[0]
	Los = aa*(Skip-1) + 0.5*(1-gamma)*W_new
	Xr = Skip*aa
	Yr = -Steep*Dz/2
	a = 0.5*gamma*W_new
	d = 0.5*h_b
	b = 0.5*H_top
	t1 = pi/2
	t0 = 0
	eps = 0.00000001
	delta = 1
	n = 0
	while abs(delta)>eps:
		middle = 0.5*(t0+t1)
		n +=1
		if n > 199:
			break
		if func(Los,Xr,Yr,bb,a,b,d,middle) < 0:
			t0 = middle
		else:
			t1 = middle
		delta = func(Los,Xr,Yr,bb,a,b,d,middle)
	# interlocking angle
	Angle = degrees(atan(b/a/tan(middle)))
	print '======================='
	# print 'middle=', middle
	print '### Real interlocking angle = %0.2f' %(Angle)
	# return()
#
	###################################
	## cubic matrix will be created. ##
	###################################
#                  _        _      
#  _ __ ___   __ _| |_ _ __(_)_  __
# | '_ ` _ \ / _` | __| '__| \ \/ /
# | | | | | | (_| | |_| |  | |>  < 
# |_| |_| |_|\__,_|\__|_|  |_/_/\_\
	if (Dz != 0):
		print '### Creat Matrix...'
		session.viewports['Viewport: 1'].setValues(displayedObject=None)
		s1 = mdb.models['Model-1'].ConstrainedSketch(name='__profile__', 
			sheetSize=5*Ly,gridSpacing=0.1*Ly)
		g, v, d, c = s1.geometry, s1.vertices, s1.dimensions, s1.constraints
		s1.setPrimaryObject(option=STANDALONE)
		s1.rectangle(point1=(-0.5*Wx, -0.5*Ly), point2=(0.5*Wx, 0.5*Ly))
		p = mdb.models['Model-1'].Part(name='Part-Matrix', dimensionality=THREE_D, 
			type=DEFORMABLE_BODY)
		p = mdb.models['Model-1'].parts['Part-Matrix']
		p.BaseSolidExtrude(sketch=s1, depth=Dz)
		s1.unsetPrimaryObject()
		p = mdb.models['Model-1'].parts['Part-Matrix']
		session.viewports['Viewport: 1'].setValues(displayedObject=p)
		del mdb.models['Model-1'].sketches['__profile__']
		print '### Creat Matrix successfully!'
	##################################################
	####### Sweep the Axial Tow along x-axis #########
	##################################################
# __        __    __ _   
# \ \      / /__ / _| |_ 
 # \ \ /\ / / _ \ |_| __|
  # \ V  V /  __/  _| |_ 
   # \_/\_/ \___|_|  \__|
	
	# weft_Gen = 1  # 0 -- Abaqus  # 1 -- TexGen
	
	if (Skip !=0 and weft_Gen == 1):
		step = mdb.openStep('Part-Weft_One.stp', scaleFromFile=OFF)
		mdb.models['Model-1'].PartFromGeometryFile(name='Part-Weft_Axis_One', geometryFile=step, 
			combine=False, dimensionality=THREE_D, type=DEFORMABLE_BODY)
		
	elif(Skip !=0 and weft_Gen == 0 ):
		print '### Generating the Weft tow...'
		# path line S
		t = (
			1.0, 0.0, 0.0,
			0.0, 0.0, 1.0,
			0.0,-1.0, 0.0,
			0.0, 0.0, 0.0)
		s = mdb.models['Model-1'].ConstrainedSketch(name='__sweep__', 
			sheetSize=2*Ly, gridSpacing=0.05*Ly, transform=t)
		g, v, d, c = s.geometry, s.vertices, s.dimensions, s.constraints
		s.setPrimaryObject(option=STANDALONE)
		s.Line(point1=(-0.5*Wx, 0.0), point2=(0.5*Wx, 0.0))
		s.unsetPrimaryObject()
		s.unsetPrimaryObject()
		# Section 
		t1 = (
			0.0, 1.0, 0.0,
			0.0, 0.0, 1.0,
			1.0, 0.0, 0.0,
			0.0, 0.0, 0.0)
		s1 = mdb.models['Model-1'].ConstrainedSketch(name='__profile__', 
			sheetSize=2*Ly, gridSpacing=0.1*Ly, transform=t1)
		g1, v1, d1, c1 = s1.geometry, s1.vertices, s1.dimensions, s1.constraints
		s1.setPrimaryObject(option=SUPERIMPOSE)
		H_a2 = 0.95*H_a
		# Section = 1 lenticular
		if Section[0] > 1:
			s1.Arc3Points(point1=(-0.5*W_a, 0.0), point2=(0.5*W_a, 0.0), point3=(0.0, 0.5*H_a2))
			s1.Arc3Points(point1=(-0.5*W_a, 0.0), point2=(0.5*W_a, 0.0), point3=(0.0, -0.5*H_a2))
			s1.ConstructionLine(point1=(0.0, 0.0), point2=(0.0, 0.5*H_a2))
			s1.breakCurve(curve1=g1[2], point1=(0.0, 0.5*H_a2), 
				curve2=g1[4], point2=(0.0, 0.5*H_a2))
			s1.breakCurve(curve1=g1[3], point1=(0.0, -0.5*H_a2), 
				curve2=g1[4], point2=(0.0, -0.5*H_a2))
			s1.unsetPrimaryObject()
		# Section = 1 pure Ellipse
		elif Section[0] == 1:
			s1.EllipseByCenterPerimeter(center=(0.0, 0.0), axisPoint1=(0.5*W_a, 0.0), axisPoint2=(0.0, 0.5*H_a2))
			s1.ConstructionLine(point1=(0.0, 0.0), point2=(0.5*W_a, 0.0))
			s1.ConstructionLine(point1=(0.0, 0.0), point2=(0.0, 0.5*H_a2))
			# break to add extra vertices for copy mesh
			s1.breakCurve(curve1=g1[2], point1=(-0.5*W_a, 0.0), 
				curve2=g1[4], point2=(-0.5*W_a, 0.0))
			s1.breakCurve(curve1=g1[6], point1=(0.0, 0.5*H_a2), 
				curve2=g1[5], point2=(0.0, 0.5*H_a2))
			s1.breakCurve(curve1=g1[7], point1=(-0.0, -0.5*H_a2), 
				curve2=g1[5], point2=(0.0, -0.5*H_a2))
			s1.unsetPrimaryObject()
		else:
			gamma = Section[0]
			a = 0.5*W_a*gamma
			X0 = 0.5*W_a-a
			Y0 = 0.5*H_a2
			s1.Line(point1=(-X0, Y0), point2=(X0, Y0))
			s1.Line(point1=(-X0, -Y0), point2=(X0, -Y0))
			s1.EllipseByCenterPerimeter(center=(X0, 0.0), axisPoint1=(X0, Y0), 
				axisPoint2=(0.5*W_a, 0.0))
			s1.autoTrimCurve(curve1=g1[4], point1=(0.5*W_a-2.0*a, 0))
			s1.EllipseByCenterPerimeter(center=(-X0, 0.0), axisPoint1=(-X0, Y0), 
				axisPoint2=(-0.5*W_a, 0.0))
			s1.autoTrimCurve(curve1=g1[7], point1=(-0.5*W_a+2.0*a, 0))
			#s1.rectangle(point1=(-0.5*W_a, -0.5*H_a2), point2=(0.5*W_a, 0.5*H_a2))
			s1.unsetPrimaryObject()
		p = mdb.models['Model-1'].Part(name='Part-Weft_Axis_One', dimensionality=THREE_D, 
			type=DEFORMABLE_BODY)
		p = mdb.models['Model-1'].parts['Part-Weft_Axis_One']
		p.BaseSolidSweep(sketch=s1, path=s)
		s1.unsetPrimaryObject()
		p = mdb.models['Model-1'].parts['Part-Weft_Axis_One']
		session.viewports['Viewport: 1'].setValues(displayedObject=p)
		del mdb.models['Model-1'].sketches['__profile__']
		del mdb.models['Model-1'].sketches['__sweep__']
		print '### Generating the Weft tow successfully!'
	elif(Skip ==0 ):
		print '### ERROR: Skip=0, on space for weft tow!'

	############################################
	###### Sweep the Warp Tow along Y-asix	####
	############################################
 # __        __               
 # \ \      / /_ _ _ __ _ __  
  # \ \ /\ / / _` | '__| '_ \ 
   # \ V  V / (_| | |  | |_) |
    # \_/\_/ \__,_|_|  | .__/ 
                     # |_| 
	# warp_Gen = 0  # 0 -- Abaqus  # 1 -- TexGen
	if (Deep!=0 and warp_Gen ==0): # Abaqus warp
		# path line S
		print '### Generating the Warp tow...'
		t = (
			0.0, 1.0, 0.0,
			0.0, 0.0, 1.0,
			1.0, 0.0, 0.0,
			0.0, 0.0, 0.0)
		s = mdb.models['Model-1'].ConstrainedSketch(name='__sweep__', 
			sheetSize=2*Ly, gridSpacing=0.05*Ly, transform=t)
		g, v, d, c = s.geometry, s.vertices, s.dimensions, s.constraints
		s.setPrimaryObject(option=STANDALONE)
		# path
		aa = 0.5*(W_a+D_a)
		bb = 0.5*(H_a+h_b)
		RefPoints=[]
		#
		# 1. Top Skip: Los
		n=int(6*Skip)
		Num1 = [1-1.0*x/n for x in range(0, n+1)]
		if Section[0] > 1:
			gamma = 1.0
		elif Section[0] <= 1:
			gamma = Section[0]
		Los = aa*(Skip-1) + 0.5*(1-gamma)*W_a
		for x in reversed(Num1[0:n+1]):
			Points=[(x*Los, 0.0),]
			# Points=[(aa*(Skip-1)*x, 0.0),]
			RefPoints=RefPoints+Points
			#
		# 2. interpolate the reference points of top lenticular arc 

		# Lenticular axial Weft tow
		if Section[0] >1:
			n=30
			Num2 = [1.0*x*x/n/n for x in range(0, n+1)]
			for i in Num2: #[0:n]
				Angle = degrees(Degree)
				a = 0.5*(W_a+1.2*h_b/sin(Degree))
				b = 0.5*(H_a+h_b)
				Radiu = (a**2 + b**2)/(2.0*b)
				theta = asin(a/Radiu)
				#theta = 1.0*Degree
				x = aa*(Skip-1)+Radiu*cos(pi/2.0-i*theta)
				y = -Radiu+Radiu*sin(pi/2.0-i*theta)
				point = [(x, y),]
				RefPoints=RefPoints+point
		# Elliptical round rectangle and pure ellipetical
		else: 
			# determine the interlocking angle
			# gamma = Section[0]
			Los = aa*(Skip-1) + 0.5*(1-gamma)*W_a
			# Xr = Skip*aa
			# Yr = -Steep*bb
			aa = 0.5*(W_a+D_a)
			bb = 0.5*(H_a+h_b)
			a = 0.5*gamma*W_a
			b = 0.5*H_a
			# d = 0.5*h_b
			dis = 0.5*h_b
			n=150
			Num2 = [1.0*x/n for x in range(0, n+1)]
			for i in Num2: #[0:n]
				Beta = 1.0*middle
				t = (0.5*pi-i*(pi/2-Beta))
				r = (a**2)*(sin(t)**2)+(b**2)*(cos(t)**2)
				x = (a+ dis*b/sqrt(r))*cos(t) + Los
				y = (b+ dis*a/sqrt(r))*sin(t) - bb
				point = [(x, y),]
				RefPoints=RefPoints+point

		# print RefPoints
		# # 3. add Depth in Z
		Xc = Skip*aa
		# Yc = -Steep*bb
		Yc = -bb-(Steep-1)*Dz/2
		pointc = [(Xc, Yc),]
		#print point
		RefPoints=RefPoints+pointc
		#print RefPoints
		for i in reversed(RefPoints):
			RotatedPoint= [(2*Xc-i[0],2*Yc-i[1]),]
			RefPoints.extend(RotatedPoint)
		# Repeat first g[1] by Deep number
		CopiedPoint = []
		n = int(Deep/Steep)
		for m in range(1,n):
			for i in RefPoints:
				CopiedPoint.extend([(i[0]+2*Xc*m,i[1]+2*Yc*m),])
		#print CopiedPoint
		RefPoints.extend(CopiedPoint)

		s.Spline(points=tuple(RefPoints))
		# Mirror half to full
		s.ConstructionLine(point1=(Ly/2.0, 0.0), angle=90.0)
		s.copyMirror(mirrorLine=g[3], objectList=(g[2], ))
		s.unsetPrimaryObject()
		# Section of warp tow
		t1 =(
			1.0, 0.0, 0.0,
			0.0,-1.0, 0.0,
			0.0, 0.0,-1.0,
			0.0, 0.0, 0.0)
		s1 = mdb.models['Model-1'].ConstrainedSketch(name='__profile__', 
			sheetSize=Ly, gridSpacing=0.01*Ly, transform=t1)
		g1, v1, d1, c1 = s1.geometry, s1.vertices, s1.dimensions, s1.constraints
		s1.setPrimaryObject(option=SUPERIMPOSE)
		################################
		# change section h_b to add gaps
		h_b2 = 0.95*h_b
		################################
		# Section = 1 Elenticular
		if Section[1] > 1:
			s1.Arc3Points(point1=(-0.5*w_b, 0.0), point2=(0.5*w_b, 0.0), point3=(0.0, 0.5*h_b2))
			s1.Arc3Points(point1=(-0.5*w_b, 0.0), point2=(0.5*w_b, 0.0), point3=(0.0, -0.5*h_b2))
			s1.ConstructionLine(point1=(0.0, 0.0), point2=(0.0, 0.5*h_b2))
			s1.breakCurve(curve1=g1[2], point1=(0.0, 0.5*h_b2), 
				curve2=g1[4], point2=(0.0, 0.5*h_b2))
			s1.breakCurve(curve1=g1[3], point1=(0.0, -0.5*h_b2), 
				curve2=g1[4], point2=(0.0, -0.5*h_b2))
			s1.unsetPrimaryObject()
		# Section = 2 Ellipse
		elif Section[1] ==1:
			s1.EllipseByCenterPerimeter(center=(0.0, 0.0), 
				axisPoint1=(0.5*w_b, 0.0), axisPoint2=(0.0, 0.5*h_b2))
			s1.ConstructionLine(point1=(0.0, 0.0), point2=(0.5*w_b, 0.0))
			s1.ConstructionLine(point1=(0.0, 0.0), point2=(0.0, 0.5*h_b2))
			# break to add extra vertices for copy mesh
			s1.breakCurve(curve1=g1[2], point1=(-0.5*w_b, 0.0), 
				curve2=g1[4], point2=(-0.5*w_b, 0.0))
			s1.breakCurve(curve1=g1[6], point1=(0.0, 0.5*h_b2), 
				curve2=g1[5], point2=(0.0, 0.5*h_b2))
			s1.breakCurve(curve1=g1[7], point1=(-0.0, -0.5*h_b2), 
				curve2=g1[5], point2=(0.0, -0.5*h_b2))
			s1.unsetPrimaryObject()
		# Section = 2 Round Rectancular
		elif Section[1] == 0:
			s1.rectangle(point1=(-0.5*w_b, -0.5*h_b2), point2=(0.5*w_b, 0.5*h_b2))
			s1.unsetPrimaryObject()
		else:
			gamma = Section[1]
			a = 0.5*w_b*gamma
			X0 = 0.5*w_b-a
			Y0 = 0.5*h_b2
			s1.Line(point1=(-X0, Y0), point2=(X0, Y0))
			s1.Line(point1=(-X0, -Y0), point2=(X0, -Y0))
			s1.EllipseByCenterPerimeter(center=(X0, 0.0), axisPoint1=(X0, Y0), 
				axisPoint2=(0.5*w_b, 0.0))
			s1.autoTrimCurve(curve1=g1[4], point1=(0.5*w_b-2.0*a, 0))
			s1.EllipseByCenterPerimeter(center=(-X0, 0.0), axisPoint1=(-X0, Y0), 
				axisPoint2=(-0.5*w_b, 0.0))
			s1.autoTrimCurve(curve1=g1[7], point1=(-0.5*w_b+2.0*a, 0))
			#s1.rectangle(point1=(-0.5*W_a, -0.5*H_a), point2=(0.5*W_a, 0.5*H_a))
			s1.unsetPrimaryObject()
		p = mdb.models['Model-1'].Part(name='Part-Warp_One', dimensionality=THREE_D, 
			type=DEFORMABLE_BODY)
		p = mdb.models['Model-1'].parts['Part-Warp_One']
		p.BaseSolidSweep(sketch=s1, path=s)
		s1.unsetPrimaryObject()
		p = mdb.models['Model-1'].parts['Part-Warp_One']
		session.viewports['Viewport: 1'].setValues(displayedObject=p)
		del mdb.models['Model-1'].sketches['__profile__']
		del mdb.models['Model-1'].sketches['__sweep__']
		print '### Generating the Warp tow successfully!'
	elif (Deep!=0 and warp_Gen ==1): # Texgen warp
		aa = 0.5*(W_a+D_a)
		bb = 0.5*(H_a+h_b)
		step = mdb.openStep('Part-Warp_One.stp', scaleFromFile=OFF)
		mdb.models['Model-1'].PartFromGeometryFile(name='Part-Warp_One', geometryFile=step, 
			combine=False, dimensionality=THREE_D, type=DEFORMABLE_BODY)
		p = mdb.models['Model-1'].parts['Part-Warp_One']
		session.viewports['Viewport: 1'].setValues(displayedObject=p)
		#\
	elif(Deep==0):
		print '### ERROR: Deep=0, on space for warp tow!'
	

	################################################################
	##Define surface for cohesive elements and material orientation#
	################################################################
#  ____              __                    
# / ___| _   _ _ __ / _| __ _  ___ ___ ___ 
# \___ \| | | | '__| |_ / _` |/ __/ _ \ __|
#  ___) | |_| | |  |  _| (_| | (__  __\__ \
# |____/ \__,_|_|  |_|  \__,_|\___\___|___/
	# Define surface of weft tows
	print '### Defining the Surfaces and edges for Orientation and Cohesive...'
	# Define surface of axial weft tows
	p = mdb.models['Model-1'].parts['Part-Weft_Axis_One']
	s, c = p.faces, p.cells
	cells = c.getSequenceFromMask(mask=('[#f ]', ), )
	p.Set(cells=cells, name='Set-Weft')
	if Section[0] > 1:
		side1Faces = s.getSequenceFromMask(mask=('[#3 ]', ), )
	elif Section[0] == 1:
		side1Faces = s.getSequenceFromMask(mask=('[#1 ]', ), )
	elif Section[0] < 1 :
		side1Faces = s.getSequenceFromMask(mask=('[#f ]', ), )
	p.Surface(side1Faces=side1Faces, name='Surf-Weft_Cohesive')
	#
	#
	#
	if(weft_Gen==1):
		p = mdb.models['Model-1'].parts['Part-Weft_Axis_One']
		s= p.faces
		del mdb.models['Model-1'].parts['Part-Weft_Axis_One'].surfaces['Surf-Weft_Cohesive']
		side1Faces = s.getSequenceFromMask(mask=('[#1 ]', ), )
		# side1Faces = s.getSequenceFromMask(mask=('[#3a00 ]', ), )
		# side1Faces = s.getSequenceFromMask(mask=('[#3810 ]', ), )
		p.Surface(side1Faces=side1Faces, name='Surf-Weft_Cohesive')
		p = mdb.models['Model-1'].parts['Part-Weft_Axis_One']
		e = p.edges
		# edges = e.getSequenceFromMask(mask=('[#1440a ]', ), )
		# edges = e.getSequenceFromMask(mask=('[#2120a ]', ), )
		edges = e.getSequenceFromMask(mask=('[#1 ]', ), )
		p.Set(edges=edges, name='Set-Weft_xline')
	#
	#


	# # Define surface of Warp tows
	p = mdb.models['Model-1'].parts['Part-Warp_One']
	s, e, c = p.faces, p.edges, p.cells
	cells = c.getSequenceFromMask(mask=('[#1 ]', ), )
	p.Set(cells=cells, name='Set-Warp')
	#
	# surface warp
	p = mdb.models['Model-1'].parts['Part-Warp_One']
	s, e, c = p.faces, p.edges, p.cells
	face1=s.getByBoundingBox(-Wx,-0.1*Ly,-Dz,Wx,0.1*Ly,Dz)
	face2=s.getByBoundingBox(-Wx,0.9*Ly,-Dz,Wx,1.1*Ly,Dz)
	p.Surface(side1Faces=face1+face2, name='Surf-Warp12')
	p.Surface(side1Faces=p.faces, name='Surf-Warp0')
	p=mdb.models['Model-1'].parts['Part-Warp_One']
	p.SurfaceByBoolean(name='Surf-Warp', operation=DIFFERENCE, surfaces=(
		p.surfaces['Surf-Warp0'], p.surfaces['Surf-Warp12'], ))	
	p.Surface(name='Surf-Warp_Cohesive', objectToCopy=p.surfaces['Surf-Warp'])
	p.deleteSurfaces(surfaceNames=('Surf-Warp0', 'Surf-Warp12', ))
	# p.Surface(side1Faces=side1FacesTop, name='Surf-Warp')
	# p.Surface(side1Faces=side1FacesAll, name='Surf-Warp_Cohesive')

	# Warp_xline
	p = mdb.models['Model-1'].parts['Part-Warp_One']
	s, e, c = p.faces, p.edges, p.cells
	edges1=e.getByBoundingBox(-Wx,-0.5*Ly,-Dz,Wx,0.25*Ly,Dz)
	edges2=e.getByBoundingBox(-Wx,0.4*Ly,-2*Deep*Dz,Wx,0.6*Ly,Dz)
	edges3=e.getByBoundingBox(-Wx,0.9*Ly,-Dz,Wx,1.1*Ly,Dz)
	p.Set(edges=p.edges, name='Set-Warp_0')
	p.Set(edges=edges1+edges2+edges3, name='Set-Warp_123')
	p=mdb.models['Model-1'].parts['Part-Warp_One']
	p.SetByBoolean(name='Set-Warp_xline', operation=DIFFERENCE, sets=(p.sets['Set-Warp_0'], 
		p.sets['Set-Warp_123'], ))
	p.deleteSets(setNames=('Set-Warp_0', 'Set-Warp_123', ))
	# return(0)
	# #
	# Define surface of straight warp tows
	if (Straight != 0):
		p = mdb.models['Model-1'].parts['Part-Straight_Warp']
		s, c = p.faces, p.cells
		# cells = c.getSequenceFromMask(mask=('[#1 ]', ), )
		p.Set(cells=p.cells, name='Set-Warp_Straight')
		if Section[0] > 1:
			side1Faces = s.getSequenceFromMask(mask=('[#3 ]', ), )
		elif Section[0] == 1:
			side1Faces = s.getSequenceFromMask(mask=('[#1 ]', ), )
		elif Section[0] < 1 :
			side1Faces = s.getSequenceFromMask(mask=('[#f ]', ), )
		p.Surface(side1Faces=side1Faces, name='Surf-Warp_Cohesive')
		
		
	print '### successfully!'
	# #
	print '### Defining the Surfaces for PBC ...'
	# ====================================
	# # Partition matrix
	# ====================================
	p = mdb.models['Model-1'].parts['Part-Matrix']
	s = p.faces
	side1Faces = s.findAt(((-Wx/2.0, 0.0, Dz/2.0), ))
	side2Faces = s.findAt((( Wx/2.0, 0.0, Dz/2.0), ))
	p.Surface(side1Faces=side1Faces, name='Surf-X0')
	p.Surface(side1Faces=side2Faces, name='Surf-X1')
	# #
	p = mdb.models['Model-1'].parts['Part-Matrix']
	f, e, d = p.faces, p.edges, p.datums
	t = p.MakeSketchTransform(sketchPlane=f[2], sketchUpEdge=e[5], 
		sketchPlaneSide=SIDE1, origin=(Wx/2.0, Ly/2.0, 0.0))
	s = mdb.models['Model-1'].ConstrainedSketch(name='__profile__', 
		sheetSize=2.0*Ly, gridSpacing=0.1*Ly, transform=t)
	g, v, d1, c = s.geometry, s.vertices, s.dimensions, s.constraints
	s.setPrimaryObject(option=SUPERIMPOSE)
	p = mdb.models['Model-1'].parts['Part-Matrix']
	p.projectReferencesOntoSketch(sketch=s, filter=COPLANAR_EDGES)
	for i in range(Long-1):
		s.Line(point1=(-(i+1)*(D_a+W_a), 0.0), point2=(-(i+1)*(D_a+W_a), Dz))
	# #
	p = mdb.models['Model-1'].parts['Part-Matrix']
	f = p.faces
	pickedFaces = f.getSequenceFromMask(mask=('[#4 ]', ), )
	e1, d2 = p.edges, p.datums
	p.PartitionFaceBySketch(sketchUpEdge=e1[5], faces=pickedFaces, sketch=s)
	s.unsetPrimaryObject()
	del mdb.models['Model-1'].sketches['__profile__']
	#
	p = mdb.models['Model-1'].parts['Part-Matrix']
	f, e, v, d= p.faces, p.edges, p.vertices, p.datums
	ee = e.findAt(((-Wx/2.0, -Ly/2.0, Dz/2.0),))
	ff = f.findAt(((-Wx/2.0, 0.0, Dz/2.0),),)
	# #
	t = p.MakeSketchTransform(sketchPlane=ff[0], sketchUpEdge=ee[0], 
		sketchPlaneSide=SIDE1, origin=(-Wx/2.0, -Ly/2.0, 0.0))
	s = mdb.models['Model-1'].ConstrainedSketch(name='__profile__', 
		sheetSize=2.0*Ly, gridSpacing=0.1*Ly, transform=t)
	g, v, d1, c = s.geometry, s.vertices, s.dimensions, s.constraints
	s.setPrimaryObject(option=SUPERIMPOSE)
	p = mdb.models['Model-1'].parts['Part-Matrix']
	p.projectReferencesOntoSketch(sketch=s, filter=COPLANAR_EDGES)
	for i in range(Long-1):
		s.Line(point1=(-(i+1)*(D_a+W_a), 0.0), point2=(-(i+1)*(D_a+W_a), Dz))
	p = mdb.models['Model-1'].parts['Part-Matrix']
	p.PartitionFaceBySketch(sketchUpEdge=ee[0], faces=ff[0], sketch=s)
	s.unsetPrimaryObject()
	del mdb.models['Model-1'].sketches['__profile__']
	# #
	p = mdb.models['Model-1'].parts['Part-Matrix']
	session.viewports['Viewport: 1'].setValues(displayedObject=p)
	p = mdb.models['Model-1'].parts['Part-Matrix']
	c = p.cells
	cells = c.getSequenceFromMask(mask=('[#1 ]', ), )
	p.Set(cells=cells, name='Set-Matrix-Intact')
	p.Set(edges=p.edges, name='Set-OutBox')
	# #
	p = mdb.models['Model-1'].parts['Part-Matrix']
	s = p.faces
	# Z surfaces
	side1Faces = s.findAt(((0.0, 0.0, 0.0), ))
	side1Faces2 = s.findAt(((0.0, 0.0, Dz), ))
	p.Surface(side1Faces=side1Faces, name='Surf-Z0')
	p.Surface(side1Faces=side1Faces2, name='Surf-Z1')
	# Y surface
	side1Faces = s.findAt(((0.0, -Ly/2.0, Dz/2.0), ))
	side1Faces2 = s.findAt(((0.0, Ly/2.0, Dz/2.0), ))
	p.Surface(side1Faces=side1Faces, name='Surf-Y0')
	p.Surface(side1Faces=side1Faces2, name='Surf-Y1')
	# X surfaces
		# Xb0 and Xb1
	p = mdb.models['Model-1'].parts['Part-Matrix']
	s = p.faces
	AllfacesXb0 = ''
	AllfacesXb1 = ''
	for i in range(Step):
		face0 = s.findAt(((-Wx/2.0, -Ly/2.0+(0.5+i)*(D_a+W_a), Dz/2.0), ))
		p.Surface(side1Faces=face0, name='Surf-Xb0_'+str(i))
		face1 = s.findAt(((Wx/2.0, Ly/2.0-(0.5+i)*(D_a+W_a), Dz/2.0), ))
		p.Surface(side1Faces=face1, name='Surf-Xb1_'+str(i))
		AllfacesXb0 = ( AllfacesXb0 + 'p.surfaces[\'Surf-Xb0_'+str(i)+'\'], ')
		AllfacesXb1 = ( AllfacesXb1 + 'p.surfaces[\'Surf-Xb1_'+str(i)+'\'], ')
	Merge0 = 'p.SurfaceByBoolean(name=\'Surf-Xb0\', surfaces=('+AllfacesXb0+'))'
	Merge1 = 'p.SurfaceByBoolean(name=\'Surf-Xb1\', surfaces=('+AllfacesXb1+'))'
	eval(Merge0)
	eval(Merge1)
	p = mdb.models['Model-1'].parts['Part-Matrix']
	for i in range(Step):
		del p.surfaces['Surf-Xb0_'+str(i)]
		del p.surfaces['Surf-Xb1_'+str(i)]
	# Surface Xa0 and Xa1
	p.SurfaceByBoolean(name='Surf-Xa0', operation=DIFFERENCE, surfaces=(
		p.surfaces['Surf-X0'], p.surfaces['Surf-Xb0'], ))
	p.SurfaceByBoolean(name='Surf-Xa1', operation=DIFFERENCE, surfaces=(
		p.surfaces['Surf-X1'], p.surfaces['Surf-Xb1'], ))
 # #
 # #
	faces0 = p.surfaces['Surf-X0'].faces
	faces1 = p.surfaces['Surf-X1'].faces
	for i in range(len(faces0)):
		p.Surface(side1Faces=faces0[i:i+1], name='Surfs-X0_0'+str(i))
		p.Surface(side1Faces=faces1[i:i+1], name='Surfs-X1_0'+str(i))
	# reorder Surfs-Z_Bottom by Centroid on Y
	index_0 = {}
	index_1 = {}
	for i in range(0,len(faces0)):
		index_0[i] = p.surfaces['Surfs-X0_0'+str(i)].faces[0].getCentroid()
		index_1[i] = p.surfaces['Surfs-X1_0'+str(i)].faces[0].getCentroid()
	# print index_Y0
	# print index_Y1
	SortedIndex_0 = sorted(index_0, key=lambda k: index_0[k][0][1])
	SortedIndex_1 = sorted(index_1, key=lambda k: index_1[k][0][1])

	# Rename surface order
	for i in range(0,len(faces0)):
		p.surfaces.changeKey(fromName='Surfs-X0_0'+str(SortedIndex_0[i]), 
			toName='Surfs-X0_'+str(i))
		p.surfaces.changeKey(fromName='Surfs-X1_0'+str(SortedIndex_1[i]), 
			toName='Surfs-X1_'+str(i))  
	# 
    #
	# #### Copy a part to maintain the geometry
	p = mdb.models['Model-1'].Part(name='Part-Matrix-Intact', 
		objectToCopy=mdb.models['Model-1'].parts['Part-Matrix'], compressFeatureList=ON)
	# viewport
	p1 = mdb.models['Model-1'].parts['Part-Warp_One']
	session.viewports['Viewport: 1'].setValues(displayedObject=p1)
	session.viewports['Viewport: 1'].view.setValues(session.views['User-4'])
	mdb.models['Model-1'].parts['Part-Warp_One'].setValues(geometryRefinement=FINE)
	print '### successfully!'
	#
	############################################
	# Assembly axial waft tows	 #
	############################################
	print '#     _                           _     _       '
	print '#    / \   ___ ___  ___ _ __ ___ | |__ | |_   _ '
	print '#   / _ \ / __/ __|/ _ \  _ ` _ \|  _ \| | | | |'
	print '#  / ___ \\__ \__ \  __/ | | | | | |_) | | |_| |'
	print '# /_/   \_\___/___/\___|_| |_| |_|_.__/|_|\__, |'
	print '#                                         |___/ '
	print '### Begin Assenbly.' 
	# #
	# # Weft
	# #
	a1 = mdb.models['Model-1'].rootAssembly
	a1.DatumCsysByDefault(CARTESIAN)
	p = mdb.models['Model-1'].parts['Part-Matrix']
	a1.Instance(name='Part-Matrix-1', part=p, dependent=ON)
	p = mdb.models['Model-1'].parts['Part-Weft_Axis_One']
	a1.Instance(name='Part-Weft_Axis-Top-1', part=p, dependent=ON)
	# a1.translate(instanceList=('Part-Weft_Axis-Top-1', ), vector=(0.0, -4.0, -4.0))
	a2 = mdb.models['Model-1'].rootAssembly
	p = mdb.models['Model-1'].parts['Part-Weft_Axis_One']
	a2.Instance(name='Part-Weft_Axis-Bottom-1', part=p, dependent=ON)
	# a2.translate(instanceList=('Part-Weft_Axis-Bottom-1', ), vector=(0.0, -4.0, -4.0))
	# p = mdb.models['Model-1'].parts['Part-Weft_Axis_One']
	# a3.Instance(name='Part-Weft_Axis-Center-1', part=p, dependent=ON)
	a = mdb.models['Model-1'].rootAssembly
	if (Skip % 2) != 0:
		a.translate(instanceList=('Part-Weft_Axis-Top-1', ), vector=(0.0, -Ly/2.0, 0.0))
		#a.translate(instanceList=('Part-Weft_Axis-Center-1', ), vector=(0.0, -Ly/2.0, Dz/2.0))
		a.translate(instanceList=('Part-Weft_Axis-Bottom-1', ), vector=(0.0, -Ly/2.0, Dz))
	if (Skip % 2) == 0:
		a.translate(instanceList=('Part-Weft_Axis-Top-1', ), vector=(0.0, aa-Ly/2.0, 0.0))
		#a.translate(instanceList=('Part-Weft_Axis-Center-1', ), vector=(0.0, aa-Ly/2.0, Dz/2.0))
		a.translate(instanceList=('Part-Weft_Axis-Bottom-1', ), vector=(0.0, aa-Ly/2.0, Dz))
	# three axial weft tows
	a1 = mdb.models['Model-1'].rootAssembly
	a1.InstanceFromBooleanMerge(name='Part-Weft_AxisTBC', instances=(
		a1.instances['Part-Weft_Axis-Top-1'], 
		a1.instances['Part-Weft_Axis-Bottom-1'],),
		keepIntersections=ON, originalInstances=DELETE, domain=GEOMETRY)
	# All axial weft tows
	p = mdb.models['Model-1'].parts['Part-Weft_AxisTBC']
	a = mdb.models['Model-1'].rootAssembly
	for i in range(2*Skip*Deep):
		a.Instance(name='Part-Weft_AxisTBC-'+str(i+2), part=p, dependent=ON)
		a.translate(instanceList=('Part-Weft_AxisTBC-'+str(i+2), ), vector=( 0.0,(i+1)*(W_a+D_a),0.0))
	print '### Merge all axial weft tows....'
	# Rotate the center by 180 degree for compressed weft tow
	a1 = mdb.models['Model-1'].rootAssembly
	a1.rotate(instanceList=('Part-Weft_AxisTBC-2', ), axisPoint=(-Wx/2, 0.0, Dz/2.0), 
		axisDirection=(1, 0.0, 0.0), angle=180.0)
	
	# return()
	Allinstances = ''	
	for n in range(2*Skip*Deep+1):
		newPartName = 'Part-Weft_AxisTBC-'+str(int(n+1))
		Allinstances = ( Allinstances + 'a1.instances[\''+newPartName+'\'], ')
	a1 = mdb.models['Model-1'].rootAssembly
	Merge = 'a1.InstanceFromBooleanMerge(name=\'Part-Weft_AxisAll\', instances=(' \
		+Allinstances+'),keepIntersections=ON, originalInstances=DELETE, domain=GEOMETRY)'
			# suppress DELETE
	eval(Merge)
	print '### Successfully!'
	# #
	print '### Cut the extal axial Weft tows for unit cell...'
	a1 = mdb.models['Model-1'].rootAssembly
	a1.InstanceFromBooleanCut(name='Part-Weft_AxisExtra', 
		instanceToBeCut=mdb.models['Model-1'].rootAssembly.instances['Part-Weft_AxisAll-1'], 
		cuttingInstances=(a1.instances['Part-Matrix-1'], ), 
		originalInstances=SUPPRESS)
	a1 = mdb.models['Model-1'].rootAssembly
	a1.features['Part-Weft_AxisAll-1'].resume()
	a2 = mdb.models['Model-1'].rootAssembly
	a2.InstanceFromBooleanCut(name='Part-Weft_x', 
		instanceToBeCut=mdb.models['Model-1'].rootAssembly.instances['Part-Weft_AxisAll-1'], 
		cuttingInstances=(a2.instances['Part-Weft_AxisExtra-1'], ), 
		originalInstances=DELETE)
	print '### Successfully!'
	# #
	# # Warp
	# #
	a1 = mdb.models['Model-1'].rootAssembly
	a1.features['Part-Matrix-1'].resume()
	a1.features['Part-Weft_x-1'].suppress()
	# move warp tow
	a = mdb.models['Model-1'].rootAssembly
	p = mdb.models['Model-1'].parts['Part-Warp_One']
	a.Instance(name='Part-Warp_One-1', part=p, dependent=ON)
	a = mdb.models['Model-1'].rootAssembly
	a.translate(instanceList=('Part-Warp_One-1', ), vector=(0.0, -Ly/2.0, bb))
	# Generate the warp tow array
	a2 = mdb.models['Model-1'].rootAssembly
	a2.LinearInstancePattern(instanceList=('Part-Warp_One-1', ), direction1=(0.0, 0.0, 1.0), 
		direction2=(0.0, 1.0, 0.0), number1=int(2*Skip+2*Deep-2), number2=1, spacing1=Dz, spacing2=0)
	# # 
	print '### Merge all axial weft tows....'
	# Change the instanceList name.
	for n in range(2*Skip+2*Deep-3):
		PartName = 'Part-Warp_One-1-lin-' + str(int(n+2))+'-1'
		newPartName = 'Part-Warp_One-' + str(int(n+2))
		mdb.models['Model-1'].rootAssembly.features.changeKey(
			fromName=PartName, toName=newPartName)
	Allinstances = ''
	for n in range(2*Skip+2*Deep-2):
		newPartName = 'Part-Warp_One-'+str(int(n+1))
		Allinstances = ( Allinstances + 'a1.instances[\''+newPartName+'\'], ')
	a1 = mdb.models['Model-1'].rootAssembly
	Merge = 'a1.InstanceFromBooleanMerge(name=\'Part-Warp_All\', instances=(' \
		+Allinstances+'),originalInstances=DELETE, domain=GEOMETRY)'
			# SUPPRESS DELETE
	eval(Merge)
	# return()
	print '### Successfully!'
	# #
	# Define the black to Cut the warp 
	print '### Cut the Warp tows for unit cell...'
	session.viewports['Viewport: 1'].setValues(displayedObject=None)
	s1 = mdb.models['Model-1'].ConstrainedSketch(name='__profile__', 
		sheetSize=5*Ly,gridSpacing=0.1*Ly)
	g, v, d, c = s1.geometry, s1.vertices, s1.dimensions, s1.constraints
	s1.setPrimaryObject(option=STANDALONE)
	s1.rectangle(point1=(-0.52*Wx, -0.52*Ly), point2=(0.52*Wx, 0.52*Ly))
	p = mdb.models['Model-1'].Part(name='Part-CutDomain', dimensionality=THREE_D, 
		type=DEFORMABLE_BODY)
	p = mdb.models['Model-1'].parts['Part-CutDomain']
	p.BaseSolidExtrude(sketch=s1, depth=(2*Skip+2*Deep-2)*Dz)
	s1.unsetPrimaryObject()
	p = mdb.models['Model-1'].parts['Part-CutDomain']
	session.viewports['Viewport: 1'].setValues(displayedObject=p)
	del mdb.models['Model-1'].sketches['__profile__']
	# Cut the bootom extra warp tows
	a4 = mdb.models['Model-1'].rootAssembly
	p = mdb.models['Model-1'].parts['Part-CutDomain']
	a4.Instance(name='Part-CutDomain-1', part=p, dependent=ON)
	a5 = mdb.models['Model-1'].rootAssembly
	a5.translate(instanceList=('Part-CutDomain-1', ), vector=(0.0, 0.0, Dz))
	a5 = mdb.models['Model-1'].rootAssembly
	a5.features['Part-Matrix-1'].suppress()
	a6 = mdb.models['Model-1'].rootAssembly
	a6.InstanceFromBooleanCut(name='Part-Warp_Half', 
		instanceToBeCut=mdb.models['Model-1'].rootAssembly.instances['Part-Warp_All-1'], 
		cuttingInstances=(a6.instances['Part-CutDomain-1'], ), 
		originalInstances=DELETE)
	# #
	a7 = mdb.models['Model-1'].rootAssembly
	p = mdb.models['Model-1'].parts['Part-CutDomain']
	a7.Instance(name='Part-CutDomain-1', part=p, dependent=ON)
	a7 = mdb.models['Model-1'].rootAssembly
	a7.translate(instanceList=('Part-CutDomain-1', ), vector=(0, 0.0, -(2*Skip+2*Deep-2)*Dz))
	a8 = mdb.models['Model-1'].rootAssembly
	a8.InstanceFromBooleanCut(name='Part-Warp_y', 
		instanceToBeCut=mdb.models['Model-1'].rootAssembly.instances['Part-Warp_Half-1'], 
		cuttingInstances=(a7.instances['Part-CutDomain-1'], ), originalInstances=DELETE)
	print '### Successfully!'
	# #
	# Move warp tow to position
	
	a1 = mdb.models['Model-1'].rootAssembly
	a1.translate(instanceList=('Part-Warp_y-1', ), vector=((Wx-w_b-d_b)/2.0, 0.0, 0.0))
	# add stright warp
	if(Straight != 0):
		a1 = mdb.models['Model-1'].rootAssembly
		for i in range(Straight):
			p = mdb.models['Model-1'].parts['Part-Straight_Warp']
			a1.Instance(name='Part-Warp_y-'+str(i+2), part=p, dependent=ON)
			# move stright warp
			a1.translate(instanceList=('Part-Warp_y-'+str(i+2), ), 
				vector=((-(i+1)*(w_b+d_b)+(Wx-w_b-d_b)/2.0, 0.0, Dz/2)))

	# # Unit celll
	# print '### Merge to Unit cell...'
	a = mdb.models['Model-1'].rootAssembly
	a.resumeFeatures(('Part-Matrix-1', 'Part-Weft_x-1', ))
	# for i in range(Straight+1):

	
	Allinstances=''
	for n in range(Straight+1):
		newPartName = 'Part-Warp_y-'+str(int(n+1))
		Allinstances = ( Allinstances + 'a.instances[\''+newPartName+'\'], ')
	Allinstances = Allinstances+ 'a.instances[\'Part-Weft_x-1\'], a.instances[\'Part-Matrix-1\'], ' 
	Merge = 'a.InstanceFromBooleanMerge(name=\'Part-UnitCell\', instances=(' \
		+Allinstances+'), keepIntersections=ON, originalInstances=DELETE, domain=GEOMETRY)'
			# SUPPRESS DELETE
	a = mdb.models['Model-1'].rootAssembly
	eval(Merge)
	print '### Successfully!'
	# return()
	# # Delete useless parts
	del mdb.models['Model-1'].parts['Part-Warp_Half']
	del mdb.models['Model-1'].parts['Part-CutDomain']
	del mdb.models['Model-1'].parts['Part-Weft_AxisExtra']
	# del mdb.models['Model-1'].parts['Part-Weft_Axis_One']
	del mdb.models['Model-1'].parts['Part-Weft_AxisTBC']
	del mdb.models['Model-1'].parts['Part-Weft_AxisAll']
	# del mdb.models['Model-1'].parts['Part-Warp_One']
	del mdb.models['Model-1'].parts['Part-Warp_All']
	del mdb.models['Model-1'].parts['Part-Matrix-Intact']
	# # # Delete useless instanceList
	# a = mdb.models['Model-1'].rootAssembly
	# a.deleteFeatures(('Part-Weft_x-1', 'Part-Warp_y-1', 'Part-Matrix-1', ))
	# #
	a = mdb.models['Model-1'].rootAssembly
	session.viewports['Viewport: 1'].setValues(displayedObject=a)
	session.viewports['Viewport: 1'].view.setValues(session.views['User-4'])
	session.viewports['Viewport: 1'].maximize()
	p = mdb.models['Model-1'].parts['Part-UnitCell']
	session.viewports['Viewport: 1'].setValues(displayedObject=p)
	session.viewports['Viewport: 1'].view.setValues(session.views['User-4'])
	print '### End Assenbly.' 
	# # #
	print '### Calculate Fiber volume ratio:' 
	volumeUnitcell=mdb.models['Model-1'].parts['Part-Matrix'].getVolume()
	volumeWeft=mdb.models['Model-1'].parts['Part-Weft_x'].getVolume()
	volumeWarp=mdb.models['Model-1'].parts['Part-Warp_y'].getVolume()
	volumeWarpS = 0.0
	if (Straight !=0):
		volumeWarpS=mdb.models['Model-1'].parts['Part-Straight_Warp'].getVolume()
		volumeWarpS = Straight*volumeWarpS
	volumeWarp = volumeWarp+volumeWarpS
	FV = (volumeWeft+volumeWarp)/volumeUnitcell
	Weft_Warp = volumeWeft/volumeWarp
	print '### The fiber tow volume ratio is %1.4f ' %(FV)
	print '### The Weft/Warp ratio is %1.4f' %(Weft_Warp)
	#
	# # mdb.models['Model-1'].parts['Part-Matrix'].writeStepFile(
		# # 'Part-Matrix.stp')
	# # mdb.models['Model-1'].parts['Part-axialYarn'].writeStepFile(
		# # 'Part-axialYarn.stp')
	# # mdb.models['Model-1'].parts['Part-biasYarn_A'].writeStepFile(
		# # 'Part-biasYarn_A.stp')
	# # mdb.models['Model-1'].parts['Part-biasYarn_B'].writeStepFile(
		# # 'Part-biasYarn_B.stp')
	# print '### 3D Ply-to-Ply Interlock Woven Geometry has been created into folder:'
	ModelName = '3D_Anglelocked_S'+str(int(Step))+'_G'+str(int(Skip))+'_D'+str(int(Deep))+'_'+str(int(Steep))
	mdb.saveAs(pathName=ModelName+'.cae')
	# # message
	return Angle,volumeWeft,volumeWarp,volumeUnitcell, FV, Weft_Warp, ModelName,Angle_max,D_min

# Assign material properties

def ViewportDisplay(LoadVector,ModelName):
	session.viewports['Viewport: 1'].minimize()
	# o1 = visualization.openOdb(path=fileName, readOnly=True)
	jobName = 'Job-'+ModelName+'.odb'
	Open3 = session.openOdb(name=jobName)
	session.viewports['Viewport: 1'].setValues(displayedObject=Open3)
	session.linkedViewportCommands.setValues(linkViewports=False)
	frameIndexOffset=0
	if ( LoadVector[0]!=0.0):
		session.Viewport(name='Pure X load',titleStyle=CUSTOM,
			customTitleString='Pure X load')
		session.viewports['Pure X load'].setValues(displayedObject=Open3)
		# Align the viewport with its load case results.
		session.viewports['Pure X load'].odbDisplay.setFrame(
			step=0, frame=1)
		session.viewports['Pure X load'].odbDisplay.display.setValues(
			plotState=CONTOURS_ON_DEF)
		session.viewports['Pure X load'].odbDisplay.setPrimaryVariable(
			variableLabel='S', outputPosition=INTEGRATION_POINT, 
			refinement=(COMPONENT,'S11'), )
		session.viewports['Pure X load'].view.setValues(session.views['Bottom'])
	else:
		frameIndexOffset = frameIndexOffset + 1
	if ( LoadVector[1]!=0.0):
		session.Viewport(
			name='Pure Y load',
			titleStyle=CUSTOM,
			customTitleString='Pure Y load')
		session.viewports['Pure Y load'].setValues(displayedObject=Open3)
		# Align the viewport with its load case results.
		session.viewports['Pure Y load'].odbDisplay.setFrame(
			step=0,
			frame=(3-frameIndexOffset))
		session.viewports['Pure Y load'].odbDisplay.display.setValues(
			plotState=CONTOURS_ON_DEF)
		session.viewports['Pure Y load'].odbDisplay.setPrimaryVariable(
			variableLabel='S',
			outputPosition=INTEGRATION_POINT,
			refinement=(COMPONENT,'S22'), )

		session.viewports['Pure Y load'].view.setValues(session.views['Bottom'])
	else:
		frameIndexOffset = frameIndexOffset + 1
	if ( LoadVector[2]!=0.0):
		session.Viewport(
			name='Pure Z load',
			titleStyle=CUSTOM,
			customTitleString='Pure Z load')
		session.viewports['Pure Z load'].setValues(displayedObject=Open3)
		# Align the viewport with its load case results.
		session.viewports['Pure Z load'].odbDisplay.setFrame(
			step=0,
			frame=(5-frameIndexOffset))
		session.viewports['Pure Z load'].odbDisplay.display.setValues(
			plotState=CONTOURS_ON_DEF)
		session.viewports['Pure Z load'].odbDisplay.setPrimaryVariable(
			variableLabel='S',
			outputPosition=INTEGRATION_POINT,
			refinement=(COMPONENT,'S33'), )
		session.viewports['Pure Z load'].view.setValues(session.views['Bottom'])
	else:
		frameIndexOffset = frameIndexOffset + 1			
	if ( LoadVector[5]!=0.0):
		session.Viewport(
			name='Pure XY shear load',
			titleStyle=CUSTOM,
			customTitleString='Pure XY shear load')
		session.viewports['Pure XY shear load'].setValues(displayedObject=Open3)
		# Align the viewport with its load case results.
		session.viewports['Pure XY shear load'].odbDisplay.setFrame(
			step=0,
			frame=(2-frameIndexOffset))
		session.viewports['Pure XY shear load'].odbDisplay.display.setValues(
			plotState=CONTOURS_ON_DEF)
		session.viewports['Pure XY shear load'].odbDisplay.setPrimaryVariable(
			variableLabel='S',
			outputPosition=INTEGRATION_POINT,
			refinement=(COMPONENT,'S12'), )
		session.viewports['Pure XY shear load'].view.setValues(session.views['Bottom'])
	else:
		frameIndexOffset = frameIndexOffset + 1
	# read Job-2A3D_symm_anti.odb
	Open4 = session.openOdb(name=jobName)
	session.viewports['Viewport: 1'].setValues(displayedObject=Open4)
	if ( LoadVector[3]!=0.0):
		session.Viewport(
			name='Pure YZ shear load',
			titleStyle=CUSTOM,
			customTitleString='Pure YZ shear load')
		session.viewports['Pure YZ shear load'].setValues(displayedObject=Open4)
		# Align the viewport with its load case results.
		session.viewports['Pure YZ shear load'].odbDisplay.setFrame(
			step=0,
			frame=(4-frameIndexOffset))
		session.viewports['Pure YZ shear load'].odbDisplay.display.setValues(
			plotState=CONTOURS_ON_DEF)
		session.viewports['Pure YZ shear load'].odbDisplay.setPrimaryVariable(
			variableLabel='S',
			outputPosition=INTEGRATION_POINT,
			refinement=(COMPONENT,'S23'), )
		session.viewports['Pure YZ shear load'].view.setValues(session.views['Bottom'])
	else:
		frameIndexOffset = frameIndexOffset + 1 
	if ( LoadVector[4]!=0.0):
		session.Viewport(
			name='Pure ZX shear load',
			titleStyle=CUSTOM,
			customTitleString='Pure ZX shear load')
		session.viewports['Pure ZX shear load'].setValues(displayedObject=Open4)
		# Align the viewport with its load case results.
		session.viewports['Pure ZX shear load'].odbDisplay.setFrame(
			step=0,
			frame=(6-frameIndexOffset))
		session.viewports['Pure ZX shear load'].odbDisplay.display.setValues(
			plotState=CONTOURS_ON_DEF)
		session.viewports['Pure ZX shear load'].odbDisplay.setPrimaryVariable(
			variableLabel='S',
			outputPosition=INTEGRATION_POINT,
			refinement=(COMPONENT,'S13'), )
		session.viewports['Pure ZX shear load'].view.setValues(session.views['Bottom'])
	else:
		frameIndexOffset = frameIndexOffset + 1
	#
	# Transform stress from matrial orientation to global coordinates
	#
	Open3 = session.openOdb(name=jobName )
	session.viewports['Viewport: 1'].setValues(displayedObject=Open3)
	scratchOdb = session.ScratchOdb(Open3)
	scratchOdb.rootAssembly.DatumCsysByThreePoints(name='Global_SYS', coordSysType=CARTESIAN,
		origin=(0.0, 0.0, 0.0), point1=(1.0, 0.0, 0.0), point2=(0.0, 1.0, 0.0))
	dtm = session.scratchOdbs[jobName].rootAssembly.datumCsyses['Global_SYS']
	session.viewports['Pure X load'].odbDisplay.basicOptions.setValues(
		transformationType=USER_SPECIFIED, datumCsys=dtm)
	session.viewports['Pure Y load'].odbDisplay.basicOptions.setValues(
		transformationType=USER_SPECIFIED, datumCsys=dtm)
	session.viewports['Pure Z load'].odbDisplay.basicOptions.setValues(
		transformationType=USER_SPECIFIED, datumCsys=dtm)
	session.viewports['Pure XY shear load'].odbDisplay.basicOptions.setValues(
		transformationType=USER_SPECIFIED, datumCsys=dtm)
	session.viewports['Pure YZ shear load'].odbDisplay.basicOptions.setValues(
		transformationType=USER_SPECIFIED, datumCsys=dtm)	 
	session.viewports['Pure ZX shear load'].odbDisplay.basicOptions.setValues(
		transformationType=USER_SPECIFIED, datumCsys=dtm)
	# Defromation scale set as 1
	session.viewports['Pure X load'].odbDisplay.commonOptions.setValues(
		deformationScaling=UNIFORM, uniformScaleFactor=1)
	session.viewports['Pure Y load'].odbDisplay.commonOptions.setValues(
		deformationScaling=UNIFORM, uniformScaleFactor=1)
	session.viewports['Pure Z load'].odbDisplay.commonOptions.setValues(
		deformationScaling=UNIFORM, uniformScaleFactor=1)
	session.viewports['Pure XY shear load'].odbDisplay.commonOptions.setValues(
		deformationScaling=UNIFORM, uniformScaleFactor=1)
	session.viewports['Pure YZ shear load'].odbDisplay.commonOptions.setValues(
		deformationScaling=UNIFORM, uniformScaleFactor=1)
	session.viewports['Pure ZX shear load'].odbDisplay.commonOptions.setValues(
		deformationScaling=UNIFORM, uniformScaleFactor=1)
	#
	# # Vertical viewports.
	#
	a = session.viewports['Viewport: 1']
	a.maximize()
	MaxHeight=a.currentHeight
	MaxWidth =a.currentWidth
	Origin = a.currentOrigin
	BoxHeight = MaxHeight/2.0
	BoxWidth = MaxWidth/3.0
	session.viewports['Viewport: 1'].minimize()
	# session.viewports['Viewport: 2'].minimize()
	# # Vertical viewports.		
	viewPortIndexOffset = 0
	if (LoadVector[0]!=0.0):
		session.viewports['Pure X load'].setValues(
			origin=(Origin[0], Origin[1]+BoxHeight),
			width=BoxWidth,
			height=BoxHeight)
	else:
		viewPortIndexOffset = viewPortIndexOffset + 1
	if (LoadVector[1]!=0.0):
		session.viewports['Pure Y load'].setValues(
			origin=(Origin[0]+BoxWidth, Origin[1]+BoxHeight),
			width=BoxWidth,
			height=BoxHeight)
	else:
		viewPortIndexOffset = viewPortIndexOffset + 1
	if (LoadVector[2]!=0.0):
		session.viewports['Pure Z load'].setValues(
			origin=(Origin[0]+2.0*BoxWidth, Origin[1]+BoxHeight),
			width=BoxWidth,
			height=BoxHeight)
	else:
		viewPortIndexOffset = viewPortIndexOffset + 1
	if (LoadVector[5]!=0.0):
		session.viewports['Pure XY shear load'].setValues(
			origin=(Origin[0], Origin[1]),
			width=BoxWidth,
			height=BoxHeight)
	else:
		viewPortIndexOffset = viewPortIndexOffset + 1
	if (LoadVector[3]!=0.0):
		session.viewports['Pure YZ shear load'].setValues(
			origin=(Origin[0]+BoxWidth, Origin[1]),
			width=BoxWidth,
			height=BoxHeight)
	else:
		viewPortIndexOffset = viewPortIndexOffset + 1		
	if (LoadVector[4]!=10):
		session.viewports['Pure ZX shear load'].setValues(
			origin=(Origin[0]+2.0*BoxWidth, Origin[1]),
			width=BoxWidth,
			height=BoxHeight)
	else:
		viewPortIndexOffset = viewPortIndexOffset + 1
	#
	session.linkedViewportCommands.setValues(linkViewports=True)
	session.viewports['Viewport: 1'].view.setViewpoint(viewVector=(1, -1, 1), 
		cameraUpVector=(0, 0, 1))
	session.viewports['Viewport: 1'].view.fitView()

def Calculate_Properties(ModelName,Volume, LoadVector,scale):
	# The constraints are stored in the load-vector.
	# # symmetric loading Fx, Fy, Fz, Shear_xy.
	jobName = 'Job-'+ModelName+'.odb'
	if LoadVector[0] !=0 :
		rODB = session.odbs[jobName]
		# Collect the various steps.
		isothermalStep = rODB.steps.values()[0]
		#thermoMechanicalStep = rODB.steps.values()[1]
		# The load-cases are held in frames.
		# Index 0 holds the reference frame.
		# 1 holds the Fx load-case.
		frameFx = rODB.steps['Step-Mechanical'].frames[1].fieldOutputs['U']
		# 2 holds the Fxy load-case.
		frameFxy = rODB.steps['Step-Mechanical'].frames[2].fieldOutputs['U']
		# 3 holds the Fy load-case.
		frameFy = rODB.steps['Step-Mechanical'].frames[3].fieldOutputs['U']
		# 4 holds the Fyz load-case.
		frameFyz = rODB.steps['Step-Mechanical'].frames[4].fieldOutputs['U']
		# 5 holds the Fz load-case.
		frameFz = rODB.steps['Step-Mechanical'].frames[5].fieldOutputs['U']
		# 4 holds the Fzx load-case.
		frameFzx = rODB.steps['Step-Mechanical'].frames[6].fieldOutputs['U']
		# Index 0 holds the reference frame.
		#frameThermomechanical = rODB.steps[thermoMechanicalStep.name].frames[1]
		Driver1 = rODB.rootAssembly.instances['PART-1-1'].nodeSets['CONSTRAINTS_DRIVER1']
		Driver2 = rODB.rootAssembly.instances['PART-1-1'].nodeSets['CONSTRAINTS_DRIVER2']
		Driver3 = rODB.rootAssembly.instances['PART-1-1'].nodeSets['CONSTRAINTS_DRIVER3']
		Driver4 = rODB.rootAssembly.instances['PART-1-1'].nodeSets['CONSTRAINTS_DRIVER4']
		Driver5 = rODB.rootAssembly.instances['PART-1-1'].nodeSets['CONSTRAINTS_DRIVER5']
		Driver6 = rODB.rootAssembly.instances['PART-1-1'].nodeSets['CONSTRAINTS_DRIVER6']
		# Load case Fx.
		Driver1Displacement = frameFx.getSubset(region=Driver1)
		Driver2Displacement = frameFx.getSubset(region=Driver2)
		Driver3Displacement = frameFx.getSubset(region=Driver3)
		Driver4Displacement = frameFx.getSubset(region=Driver4)
		Driver5Displacement = frameFx.getSubset(region=Driver5)
		Driver6Displacement = frameFx.getSubset(region=Driver6)
		Fx_eps0_x = Driver1Displacement.values[0].data[0]
		Fx_eps0_y = Driver2Displacement.values[0].data[0]
		Fx_eps0_z = Driver3Displacement.values[0].data[0]
		Fx_gamma0_yz = Driver4Displacement.values[0].data[0]
		Fx_gamma0_zx = Driver5Displacement.values[0].data[0]
		Fx_gamma0_xy = Driver6Displacement.values[0].data[0]
		# # Load case FY.	 
		Driver1Displacement = frameFy.getSubset(region=Driver1)
		Driver2Displacement = frameFy.getSubset(region=Driver2)
		Driver3Displacement = frameFy.getSubset(region=Driver3)
		Driver4Displacement = frameFy.getSubset(region=Driver4)
		Driver5Displacement = frameFy.getSubset(region=Driver5)
		Driver6Displacement = frameFy.getSubset(region=Driver6)
		Fy_eps0_x = Driver1Displacement.values[0].data[0]
		Fy_eps0_y = Driver2Displacement.values[0].data[0]
		Fy_eps0_z = Driver3Displacement.values[0].data[0]
		Fy_gamma0_yz = Driver4Displacement.values[0].data[0]
		Fy_gamma0_zx = Driver5Displacement.values[0].data[0]
		Fy_gamma0_xy = Driver6Displacement.values[0].data[0]
		# # Load case Fz.
		Driver1Displacement = frameFz.getSubset(region=Driver1)
		Driver2Displacement = frameFz.getSubset(region=Driver2)
		Driver3Displacement = frameFz.getSubset(region=Driver3)
		Driver4Displacement = frameFz.getSubset(region=Driver4)
		Driver5Displacement = frameFz.getSubset(region=Driver5)
		Driver6Displacement = frameFz.getSubset(region=Driver6)
		Fz_eps0_x = Driver1Displacement.values[0].data[0]
		Fz_eps0_y = Driver2Displacement.values[0].data[0]
		Fz_eps0_z = Driver3Displacement.values[0].data[0]
		Fz_gamma0_yz = Driver4Displacement.values[0].data[0]
		Fz_gamma0_zx = Driver5Displacement.values[0].data[0]
		Fz_gamma0_xy = Driver6Displacement.values[0].data[0]
		# Load case Fyz
		Driver1Displacement = frameFyz.getSubset(region=Driver1)
		Driver2Displacement = frameFyz.getSubset(region=Driver2)
		Driver3Displacement = frameFyz.getSubset(region=Driver3)
		Driver4Displacement = frameFyz.getSubset(region=Driver4)
		Driver5Displacement = frameFyz.getSubset(region=Driver5)
		Driver6Displacement = frameFyz.getSubset(region=Driver6)
		Fyz_eps0_x = Driver1Displacement.values[0].data[0]
		Fyz_eps0_y = Driver2Displacement.values[0].data[0]
		Fyz_eps0_z = Driver3Displacement.values[0].data[0]
		Fyz_gamma0_yz = Driver4Displacement.values[0].data[0]
		Fyz_gamma0_zx = Driver5Displacement.values[0].data[0]
		Fyz_gamma0_xy = Driver6Displacement.values[0].data[0]
		# Load case Fzx
		Driver1Displacement = frameFzx.getSubset(region=Driver1)
		Driver2Displacement = frameFzx.getSubset(region=Driver2)
		Driver3Displacement = frameFzx.getSubset(region=Driver3)
		Driver4Displacement = frameFzx.getSubset(region=Driver4)
		Driver5Displacement = frameFzx.getSubset(region=Driver5)
		Driver6Displacement = frameFzx.getSubset(region=Driver6)
		Fzx_eps0_x = Driver1Displacement.values[0].data[0]
		Fzx_eps0_y = Driver2Displacement.values[0].data[0]
		Fzx_eps0_z = Driver3Displacement.values[0].data[0]
		Fzx_gamma0_yz = Driver4Displacement.values[0].data[0]
		Fzx_gamma0_zx = Driver5Displacement.values[0].data[0]
		Fzx_gamma0_xy = Driver6Displacement.values[0].data[0]
		# Load case Fxy
		Driver1Displacement = frameFxy.getSubset(region=Driver1)
		Driver2Displacement = frameFxy.getSubset(region=Driver2)
		Driver3Displacement = frameFxy.getSubset(region=Driver3)
		Driver4Displacement = frameFxy.getSubset(region=Driver4)
		Driver5Displacement = frameFxy.getSubset(region=Driver5)
		Driver6Displacement = frameFxy.getSubset(region=Driver6)
		Fxy_eps0_x = Driver1Displacement.values[0].data[0]
		Fxy_eps0_y = Driver2Displacement.values[0].data[0]
		Fxy_eps0_z = Driver3Displacement.values[0].data[0]
		Fxy_gamma0_yz = Driver4Displacement.values[0].data[0]
		Fxy_gamma0_zx = Driver5Displacement.values[0].data[0]
		Fxy_gamma0_xy = Driver6Displacement.values[0].data[0]
		# Material properties.
		E0_x = LoadVector[0]/Volume/Fx_eps0_x
		v0_xy = -Fx_eps0_y/Fx_eps0_x
		v0_xz = -Fx_eps0_z/Fx_eps0_x
		#
		E0_y = LoadVector[1]/Volume/Fy_eps0_y
		v0_yx = -Fy_eps0_x/Fy_eps0_y
		v0_yz = -Fy_eps0_z/Fy_eps0_y
		#
		E0_z = LoadVector[2]/Volume/Fz_eps0_z
		v0_zx = -Fz_eps0_x/Fz_eps0_z
		v0_zy = -Fz_eps0_y/Fz_eps0_z
		#
		G0_yz = LoadVector[3]/Volume/Fyz_gamma0_yz 
		G0_xz = LoadVector[4]/Volume/Fzx_gamma0_zx
		G0_xy = LoadVector[5]/Volume/Fxy_gamma0_xy
		#
		# anisotropic
		n0_13_2 = Fx_gamma0_yz/Fx_eps0_x
		n0_23_2 = Fx_gamma0_zx/Fx_eps0_x
		n0_12_2 = Fx_gamma0_xy/Fx_eps0_x
		n0_13_1 = Fy_gamma0_yz/Fy_eps0_y
		n0_23_1 = Fy_gamma0_zx/Fy_eps0_y
		n0_12_1 = Fy_gamma0_xy/Fy_eps0_y
		n0_13_3 = Fz_gamma0_yz/Fz_eps0_z
		n0_23_3 = Fz_gamma0_zx/Fz_eps0_z
		n0_12_3 = Fz_gamma0_xy/Fz_eps0_z
		n0_13_23 = Fzx_gamma0_zx/Fzx_gamma0_zx
		n0_12_23 = Fzx_gamma0_xy/Fzx_gamma0_zx
		n0_12_13 = Fyz_gamma0_xy/Fyz_gamma0_yz
	# Now adding the displacements.
	# print E0_x, v0_xy, v0_xz
	# print E0_y, v0_yx, v0_yz
	# print E0_z, v0_zx, v0_zy
	# print G0_xy, G0_yz, G0_xz
	# materialProperties =(E0_x, v0_xy, v0_xz,
		# E0_y, v0_yx, v0_yz,
		# E0_z, v0_zx, v0_zy,
		# G0_yz, G0_xz, G0_xy,
		# n0_23_1, n0_31_1, n0_12_1,
		# n0_23_2, n0_31_2, n0_12_2,
		# n0_23_3, n0_31_3, n0_12_3,
		# n0_13_23, n0_12_23, n0_12_13)
	materialProperties =(E0_y, v0_yx, v0_yz, E0_x, v0_xy, v0_xz, E0_z, v0_zy, v0_zx,
		G0_xz, G0_yz, G0_xy,
		n0_23_1, n0_13_1, n0_12_1,
		n0_23_2, n0_13_2, n0_12_2,
		n0_23_3, n0_13_3, n0_12_3,
		n0_13_23, n0_12_23, n0_12_13)
	return materialProperties

def DisplayUCMaterialProperties(ModelName,materialProperties,startTime,geoTime,endTime,FV, Weft_Warp,volumeWeft,volumeWarp,Volume,Angle,Angle_max,D_min):
	# Use getInputs for a nicely formatted pop-up box and ignore the returned value.
	strE1  = "%1.4f GPa" % (materialProperties[0]/1000.0)
	strv12 = "%1.4f" % materialProperties[1]
	strv13 = "%1.4f" % materialProperties[2]
	strE2  = "%1.4f GPa" % (materialProperties[3]/1000.0)
	strv21 = "%1.4f" % materialProperties[4]
	strv23 = "%1.4f" % materialProperties[5]
	strE3  = "%1.4f GPa" % (materialProperties[6]/1000.0)
	strv31 = "%1.4f" % materialProperties[7]
	strv32 = "%1.4f" % materialProperties[8]
	strG23 = "%1.4f GPa" % (materialProperties[9]/1000.0)
	strG31 = "%1.4f GPa" % (materialProperties[10]/1000.0)
	strG12 = "%1.4f GPa" % (materialProperties[11]/1000.0)
	
	# ########## write the properties to a file.
	TowVolumeRatio = "%0.4f" %(FV)
	Weft_Warp = "%0.4f" %(Weft_Warp)
	timeA = "%0.2f" % (geoTime-startTime)
	timeB = "%0.2f" % (endTime-geoTime)
	timeC = "%0.2f" % (endTime-startTime)
	s='# Analysis Time (s):'+'\n'
	s=s+'Geomtery modelling time is '+str(timeA)+'\n'
	s=s+'Calculation time is '+str(timeB)+'\n'
	s=s+'Total time is: '+str(timeC)+'\n'
	s=s+'Interlocking angle is: '+ str(Angle)+'\n'
	s=s+'Max. interlocking angle is: '+ str(Angle_max)+'\n'
	s=s+'Min. distance is: '+ str(D_min)+'\n'
	s=s+'# Volume of unit cell is : '+str(Volume)+'\n'
	s=s+'# Volume of weft tows is : '+str(volumeWeft)+'\n'
	s=s+'# Volume of warp tows is : '+str(volumeWarp)+'\n'
	s=s+'# Fiber Tow Volume Fraction is: '+str(TowVolumeRatio)+'\n'
	s=s+'# Weft/Warp Ratio is: '+str(Weft_Warp)+'\n'
	s=s+'# Material Properties:'+'\n'
	s=s+strE1+'\n'
	s=s+strv12+'\n'	   
	s=s+strv13+'\n'	   
	s=s+strE2+'\n'
	s=s+strv21+'\n'
	s=s+strv23+'\n'
	s=s+strE3+'\n'
	s=s+strv31+'\n'
	s=s+strv32+'\n'
	s=s+strG23+'\n'
	s=s+strG31+'\n'
	s=s+strG12+'\n'
	fileName = ModelName+'.txt'
	file=open(fileName,'w')
	file.write(s)
	file.close
	#
	file=open(fileName,'a')
	sUCDisplacements = '\n\n\nOutput results:\n\nEffective compliance matrix:'
	# Displacements at key degrees of freedom.
	strS11 = "%1.3e" % (1e-6/materialProperties[0])
	strS12 = "%1.3e" % (-1e-6*materialProperties[1]/materialProperties[0])
	strS13 = "%1.3e" % (-1e-6*materialProperties[2]/materialProperties[0])
	strS14 = "%1.3e" % (1e-6*materialProperties[12]/materialProperties[0])
	strS15 = "%1.3e" % (1e-6*materialProperties[13]/materialProperties[0])
	strS16 = "%1.3e" % (1e-6*materialProperties[14]/materialProperties[0])
	#)
	strS22 = "%1.3e" % (1e-6/materialProperties[3])
	strS23 = "%1.3e" % (-1e-6*materialProperties[5]/materialProperties[3])
	strS24 = "%1.3e" % (1e-6*materialProperties[15]/materialProperties[3])
	strS25 = "%1.3e" % (1e-6*materialProperties[16]/materialProperties[3])
	strS26 = "%1.3e" % (1e-6*materialProperties[17]/materialProperties[3])
	#)
	strS33 = "%1.3e" % (1e-6/materialProperties[6])
	strS34 = "%1.3e" % (1e-6*materialProperties[18]/materialProperties[6])
	strS35 = "%1.3e" % (1e-6*materialProperties[19]/materialProperties[6])
	strS36 = "%1.3e" % (1e-6*materialProperties[20]/materialProperties[6])
	#
	strS44 = "%1.3e" % (1e-6/materialProperties[9])
	strS45 = "%1.3e" % (1e-6*materialProperties[21]/materialProperties[9])
	strS46 = "%1.3e" % (1e-6*materialProperties[22]/materialProperties[9])
	#
	strS55 = "%1.3e" % (1e-6/materialProperties[10])
	strS56 = "%1.3e" % (1e-6*materialProperties[23]/materialProperties[10])
	#
	strS66 = "%1.3e" % (1e-6/materialProperties[11])
	#
	sUCDisplacements = sUCDisplacements + '\n'
	sUCDisplacements = sUCDisplacements + strS11+'\t'+strS12+'\t'+strS13+'\t'+strS14+'\t'+strS15+'\t'+strS16+'\t'
	sUCDisplacements = sUCDisplacements + '\n'
	sUCDisplacements = sUCDisplacements + strS12+'\t'+strS22+'\t'+strS23+'\t'+strS24+'\t'+strS25+'\t'+strS26+'\t'
	sUCDisplacements = sUCDisplacements + '\n'
	sUCDisplacements = sUCDisplacements + strS13+'\t'+strS23+'\t'+strS33+'\t'+strS34+'\t'+strS35+'\t'+strS36+'\t'
	sUCDisplacements = sUCDisplacements + '\n'
	sUCDisplacements = sUCDisplacements + strS14+'\t'+strS24+'\t'+strS34+'\t'+strS44+'\t'+strS45+'\t'+strS46+'\t'
	sUCDisplacements = sUCDisplacements + '\n'
	sUCDisplacements = sUCDisplacements + strS15+'\t'+strS25+'\t'+strS35+'\t'+strS45+'\t'+strS55+'\t'+strS56+'\t'
	sUCDisplacements = sUCDisplacements + '\n'
	sUCDisplacements = sUCDisplacements + strS16+'\t'+strS26+'\t'+strS36+'\t'+strS46+'\t'+strS56+'\t'+strS66+'\t'
	file.write(sUCDisplacements)
	file.close
	#
	# 
	print '### Save propeties to data file.'
	# #
	message='Elastic & Expansion\nEffective properties.\n\n'
	message=message+'E1  = '+strE1+'\n'
	message=message+'v12 = '+ strv12+'\n'
	message=message+'v13 = '+ strv13+'\n'
	message=message+'E2  = '+strE2+'\n'
	message=message+'v21 = '+ strv21+'\n'
	message=message+'v23 = '+ strv23+'\n'
	message=message+'E3  = '+ strE3+'\n'
	message=message+'v31 = '+ strv31+'\n'
	message=message+'v32 = '+ strv32+'\n'
	message=message+'G23 = '+ strG23+'\n'
	message=message+'G31 = '+ strG31+'\n'
	message=message+'G12 = '+ strG12+'\n'
	getWarningReply(message=message,buttons=(YES,))
	print '=========================================='
	print '#  _____ _       _     _              _  #'
	print '# |  ___(_)_ __ (_)___| |__   ___  __| | #'
	print '# | |_  | | `_ \| / __| |_ \ / _ \/ _` | #'
	print '# |  _| | | | | | \__ \ | | |  __/ (_| | #'
	print '# |_|   |_|_| |_|_|___/_| |_|\___|\__,_| #'
	print '=========================================='
	





# ##### #
# Begin #
# ##### #'
#  ____             _       
# | __ )  ___  __ _(_)_ __  
# |  _ \ / _ \/ _` | | '_ \ 
# | |_) |  __/ (_| | | | | |
# |____/ \___|\__, |_|_| |_|
#             |___/ 

import time
startTime = time.time()
import time
startTime = time.time()
# Els_Fail = [1,0]
Els_Fail = [1,0]
Cohesive = 0
# Els_Fail=[1,0] = Elastic properties analysis
# Els_Fail=[0,1] = Failure properties analysis
#
# 1. Input_Geometry_data
ModelName,offset,Straight,Step,Skip,Deep,Steep,\
	W_a,H_a,D_a,w_b,h_b,d_b,Section,meshSize=Input_Geometry_data()
# 2. Input_Material_data
matArray = Input_Material()
#

weft_Gen = 1  # 0 -- Abaqus  # 1 -- TexGen
warp_Gen = 0  # 0 -- Abaqus  # 1 -- TexGen
# weft compression ratio
d0 = 1.00
c1 = 1.05
c2 = 2.0-c1
# 3. Creat_Geometry

Angle,volumeWeft,volumeWarp,Volume, FV, Weft_Warp, ModelName,Angle_max,D_min \
	= Creat_Geometry_no_Offset(Straight,Step,Skip,Deep,Steep,W_a,H_a,D_a,w_b,h_b,d_b,Section,meshSize,d0,c1,c2)
n_z=Deep/Steep
Long = 2*Skip*n_z
Ly = Long*(W_a+D_a)

# Dz = H_a + h_b
Wx = (Straight+1)*(w_b + d_b)
H_top = c1*H_a
H_bot = c2*H_a
W_new = d0*W_a
D_new = W_a+D_a - W_new
Dz = ((H_top+H_bot)/2.0 + h_b)
Wx = (w_b + d_b)
Wx = (Straight+1)*Wx


# Gometric parameters
# binder angle, Thickness, shape of unit cell
print '#'*40
print 'Model parameters: '+ModelName 
print 'Skip=%d, Deep=%d, Step=%d, Straight=%d, Interlocking Angle= %2.2f' %(Skip,Deep,Step,Straight,Angle)
print 'Original warp: w_b=%0.2f, h_b=%0.2f, d_b=%0.2f' %(w_b,h_b,d_b,)
print 'Original weft: W_a=%0.2f, H_a=%0.2f, D_a=%0.2f' %(W_a,H_a,D_a)
print 'Altered weft: W_a=%0.2f, top_H_a=%0.2f, bottom_H_a=%0.2f, D_a=%0.2f' %(W_new,H_top,H_bot,D_new)
print 'Maximum interlocking angle = %2.2f, minimum distance = %2.2f' %(Angle_max,D_min)
print 'Ly=%0.2f, Wx=%0.2f, Dz=%0.2f, Volume=%2.4f' %(Ly,Wx,Dz,Volume)
print 'Weft tow volume = %2.4f' %(volumeWeft)
print 'Warp tow volume = %2.4f' %(volumeWarp)
print 'Tow volume ratio = %1.2f%%' %(FV*100)
print 'The Weft/Warp ratio is %1.4f' %(Weft_Warp)
print '#'*40
mdb.save()
geoTime = time.time()

LoadVector = [Volume,Volume,Volume,Volume,Volume,Volume] # LoadVector=[Fxx,Fyy,Fzz,Fyz,Fxz,Fxy]

endTime = time.time()
print '### Geomtery modelling time is %0.2f s' %(geoTime-startTime)
print '### Calculation time is %0.2f s' %(endTime-geoTime)
print '### Total time is %0.2f s' %(endTime-startTime)
	# 11. Display Viewports
ViewportDisplay(LoadVector,ModelName)
	# 12. Calculate_Properties
scale = 1
UCMat = Calculate_Properties(ModelName,Volume, LoadVector,scale)
DisplayUCMaterialProperties(ModelName,UCMat,startTime,geoTime,endTime,FV,Weft_Warp,volumeWeft,volumeWarp,Volume,Angle,Angle_max,D_min)
