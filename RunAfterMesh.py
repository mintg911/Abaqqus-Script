# 2021.01.13 Create Node Sets for equations

def Adding_sets(Wx,Ly,Dz,Step,W_a,D_a):
	de = 1e-4
	Lb = Step*(W_a+D_a)
	La = Ly -Lb
	# Faces
	a = mdb.models['Model-1'].rootAssembly
	n1 = a.instances['Part-UnitCell-1'].nodes
	nodes1 = n1.getByBoundingBox(-Wx/2-de,-Ly/2-de,-de,-Wx/2+de,Ly/2+de,Dz+de)
	a.Set(nodes=nodes1, name='NodeSet-SURFS-X0')
	nodes1 = n1.getByBoundingBox(Wx/2-de,-Ly/2-de,-de,Wx/2+de,Ly/2+de,Dz+de)
	a.Set(nodes=nodes1, name='NodeSet-SURFS-X1')
	nodes1 = n1.getByBoundingBox(-Wx/2-de,-Ly/2-de,-de,Wx/2+de,-Ly/2+de,Dz+de)
	a.Set(nodes=nodes1, name='NodeSet-SURFS-Y0')
	nodes1 = n1.getByBoundingBox(-Wx/2-de,Ly/2-de,-de,Wx/2+de,Ly/2+de,Dz+de)
	a.Set(nodes=nodes1, name='NodeSet-SURFS-Y1')
	nodes1 = n1.getByBoundingBox(-Wx/2-de,-Ly/2-de,-de,Wx/2+de,Ly/2+de,de)
	a.Set(nodes=nodes1, name='NodeSet-SURFS-Z0')
	nodes1 = n1.getByBoundingBox(-Wx/2-de,-Ly/2-de,Dz-de,Wx/2+de,Ly/2+de,Dz+de)
	a.Set(nodes=nodes1, name='NodeSet-SURFS-Z1')
	# Faces
	a = mdb.models['Model-1'].rootAssembly
	n1 = a.instances['Part-UnitCell-1'].nodes
	nodes1 = n1.getByBoundingBox(Wx/2-de,-Ly/2-de,-de,Wx/2+de,-Ly/2+de,de)
	a.Set(nodes=nodes1, name='Face_1')
	nodes1 = n1.getByBoundingBox(Wx/2-de,-Ly/2-de,Dz-de,Wx/2+de,-Ly/2+de,Dz+de)
	a.Set(nodes=nodes1, name='Face_2')
	nodes1 = n1.getByBoundingBox(-Wx/2-de,-Ly/2-de,-de,-Wx/2+de,-Ly/2+de,de)
	a.Set(nodes=nodes1, name='Face_3')
	nodes1 = n1.getByBoundingBox(-Wx/2-de,-Ly/2-de,Dz-de,-Wx/2+de,-Ly/2+de,Dz+de)
	a.Set(nodes=nodes1, name='Face_4')
	nodes1 = n1.getByBoundingBox(-Wx/2-de,Lb-Ly/2-de,-de,-Wx/2+de,Lb-Ly/2+de,de)
	a.Set(nodes=nodes1, name='Face_5')
	nodes1 = n1.getByBoundingBox(-Wx/2-de,Lb-Ly/2-de,Dz-de,-Wx/2+de,Lb-Ly/2+de,Dz+de)
	a.Set(nodes=nodes1, name='Face_6')
	nodes1 = n1.getByBoundingBox(Wx/2-de,Ly/2-Lb-de,-de,Wx/2+de,Ly/2-Lb+de,de)
	a.Set(nodes=nodes1, name='Face_7')
	nodes1 = n1.getByBoundingBox(Wx/2-de,Ly/2-Lb-de,Dz-de,Wx/2+de,Ly/2-Lb+de,Dz+de)
	a.Set(nodes=nodes1, name='Face_8')
	# Edges
	a = mdb.models['Model-1'].rootAssembly
	n1 = a.instances['Part-UnitCell-1'].nodes
	nodes1 = n1.getByBoundingBox(Wx/2-de,-Ly/2-de,-de,Wx/2+de,-Ly/2+de,de)
	a.Set(nodes=nodes1, name='Edge_1')
	nodes1 = n1.getByBoundingBox(Wx/2-de,-Ly/2-de,Dz-de,Wx/2+de,-Ly/2+de,Dz+de)
	a.Set(nodes=nodes1, name='Edge_2')
	nodes1 = n1.getByBoundingBox(-Wx/2-de,-Ly/2-de,-de,-Wx/2+de,-Ly/2+de,de)
	a.Set(nodes=nodes1, name='Edge_3')
	nodes1 = n1.getByBoundingBox(-Wx/2-de,-Ly/2-de,Dz-de,-Wx/2+de,-Ly/2+de,Dz+de)
	a.Set(nodes=nodes1, name='Edge_4')
	nodes1 = n1.getByBoundingBox(-Wx/2-de,Lb-Ly/2-de,-de,-Wx/2+de,Lb-Ly/2+de,de)
	a.Set(nodes=nodes1, name='Edge_5')
	nodes1 = n1.getByBoundingBox(-Wx/2-de,Lb-Ly/2-de,Dz-de,-Wx/2+de,Lb-Ly/2+de,Dz+de)
	a.Set(nodes=nodes1, name='Edge_6')
	nodes1 = n1.getByBoundingBox(Wx/2-de,Ly/2-Lb-de,-de,Wx/2+de,Ly/2-Lb+de,de)
	a.Set(nodes=nodes1, name='Edge_7')
	nodes1 = n1.getByBoundingBox(Wx/2-de,Ly/2-Lb-de,Dz-de,Wx/2+de,Ly/2-Lb+de,Dz+de)
	a.Set(nodes=nodes1, name='Edge_8')
	nodes1 = n1.getByBoundingBox(Wx/2-de,Ly/2-de,-de,Wx/2+de,Ly/2+de,de)
	a.Set(nodes=nodes1, name='Edge_9')
	nodes1 = n1.getByBoundingBox(Wx/2-de,Ly/2-de,Dz-de,Wx/2+de,Ly/2+de,Dz+de)
	a.Set(nodes=nodes1, name='Edge_10')
	nodes1 = n1.getByBoundingBox(-Wx/2-de,Ly/2-de,-de,-Wx/2+de,Ly/2+de,de)
	a.Set(nodes=nodes1, name='Edge_11')
	nodes1 = n1.getByBoundingBox(-Wx/2-de,Ly/2-de,Dz-de,-Wx/2+de,Ly/2+de,Dz+de)
	a.Set(nodes=nodes1, name='Edge_12')
	nodes1 = n1.getByBoundingBox(Wx/2-de,-Ly/2-de,-de,Wx/2+de,-Ly/2+de,de)
	a.Set(nodes=nodes1, name='Edge_13')
	nodes1 = n1.getByBoundingBox(Wx/2-de,-Ly/2-de,Dz-de,Wx/2+de,-Ly/2+de,Dz+de)
	a.Set(nodes=nodes1, name='Edge_14')
	nodes1 = n1.getByBoundingBox(-Wx/2-de,-Ly/2-de,-de,-Wx/2+de,-Ly/2+de,de)
	a.Set(nodes=nodes1, name='Edge_15')
	nodes1 = n1.getByBoundingBox(-Wx/2-de,-Ly/2-de,Dz-de,-Wx/2+de,-Ly/2+de,Dz+de)
	a.Set(nodes=nodes1, name='Edge_16')
	nodes1 = n1.getByBoundingBox(-Wx/2-de,Lb-Ly/2-de,-de,-Wx/2+de,Lb-Ly/2+de,de)
	a.Set(nodes=nodes1, name='Edge_17')
	nodes1 = n1.getByBoundingBox(-Wx/2-de,Lb-Ly/2-de,Dz-de,-Wx/2+de,Lb-Ly/2+de,Dz+de)
	a.Set(nodes=nodes1, name='Edge_18')

	# Vertices
	a = mdb.models['Model-1'].rootAssembly
	n1 = a.instances['Part-UnitCell-1'].nodes
	nodes1 = n1.getByBoundingBox(Wx/2-de,-Ly/2-de,-de,Wx/2+de,-Ly/2+de,de)
	a.Set(nodes=nodes1, name='Vertex_1')
	nodes1 = n1.getByBoundingBox(Wx/2-de,-Ly/2-de,Dz-de,Wx/2+de,-Ly/2+de,Dz+de)
	a.Set(nodes=nodes1, name='Vertex_2')
	nodes1 = n1.getByBoundingBox(-Wx/2-de,-Ly/2-de,-de,-Wx/2+de,-Ly/2+de,de)
	a.Set(nodes=nodes1, name='Vertex_3')
	nodes1 = n1.getByBoundingBox(-Wx/2-de,-Ly/2-de,Dz-de,-Wx/2+de,-Ly/2+de,Dz+de)
	a.Set(nodes=nodes1, name='Vertex_4')
	nodes1 = n1.getByBoundingBox(-Wx/2-de,Lb-Ly/2-de,-de,-Wx/2+de,Lb-Ly/2+de,de)
	a.Set(nodes=nodes1, name='Vertex_5')
	nodes1 = n1.getByBoundingBox(-Wx/2-de,Lb-Ly/2-de,Dz-de,-Wx/2+de,Lb-Ly/2+de,Dz+de)
	a.Set(nodes=nodes1, name='Vertex_6')
	nodes1 = n1.getByBoundingBox(Wx/2-de,Ly/2-Lb-de,-de,Wx/2+de,Ly/2-Lb+de,de)
	a.Set(nodes=nodes1, name='Vertex_7')
	nodes1 = n1.getByBoundingBox(Wx/2-de,Ly/2-Lb-de,Dz-de,Wx/2+de,Ly/2-Lb+de,Dz+de)
	a.Set(nodes=nodes1, name='Vertex_8')
	nodes1 = n1.getByBoundingBox(Wx/2-de,Ly/2-de,-de,Wx/2+de,Ly/2+de,de)
	a.Set(nodes=nodes1, name='Vertex_9')
	nodes1 = n1.getByBoundingBox(Wx/2-de,Ly/2-de,Dz-de,Wx/2+de,Ly/2+de,Dz+de)
	a.Set(nodes=nodes1, name='Vertex_10')
	nodes1 = n1.getByBoundingBox(-Wx/2-de,Ly/2-de,-de,-Wx/2+de,Ly/2+de,de)
	a.Set(nodes=nodes1, name='Vertex_11')
	nodes1 = n1.getByBoundingBox(-Wx/2-de,Ly/2-de,Dz-de,-Wx/2+de,Ly/2+de,Dz+de)
	a.Set(nodes=nodes1, name='Vertex_12')



	# #########################################################
	#
	# Constraints Driver 1-6
	#
	print '### Define Constraints Driver 1-6...'
	p = mdb.models['Model-1'].parts['Part-UnitCell']
	p.Set(nodes=p.nodes, name='Set-node_all')
	#
	node0 = p.Node(coordinates=(0.0, 0.0, -1.0))
	b=node0.label
	p.Set(nodes=p.nodes[b-1:b], name='Constraints_Driver1')
	#
	node0 = p.Node(coordinates=(0.0, 0.0, -1.0))
	b=node0.label
	p.Set(nodes=p.nodes[b-1:b], name='Constraints_Driver2')
	#
	node0 = p.Node(coordinates=(0.0, 0.0, -1.0))
	b=node0.label
	p.Set(nodes=p.nodes[b-1:b], name='Constraints_Driver3')	   
	#
	node0 = p.Node(coordinates=(0.0, 0.0, -1.0))
	b=node0.label
	p.Set(nodes=p.nodes[b-1:b], name='Constraints_Driver4')
	#
	node0 = p.Node(coordinates=(0.0, 0.0, -1.0))
	b=node0.label
	p.Set(nodes=p.nodes[b-1:b], name='Constraints_Driver5')
	#
	node0 = p.Node(coordinates=(0.0, 0.0, -1.0))
	b=node0.label
	p.Set(nodes=p.nodes[b-1:b], name='Constraints_Driver6')	 
	#
	print '### Successfully.'
		# ################# 
	#
	print '### Define Constraints Driver 1-6 for equation...'
	a = mdb.models['Model-1'].rootAssembly
	Inst = a.allInstances['Part-UnitCell-1']
	node_O = Inst.sets['Constraints_Driver1'].nodes
	a.Set(name='Constraints_Driver1',nodes=node_O)
	node_O = Inst.sets['Constraints_Driver2'].nodes
	a.Set(name='Constraints_Driver2',nodes=node_O)
	node_O = Inst.sets['Constraints_Driver3'].nodes
	a.Set(name='Constraints_Driver3',nodes=node_O)
	node_O = Inst.sets['Constraints_Driver4'].nodes
	a.Set(name='Constraints_Driver4',nodes=node_O)
	node_O = Inst.sets['Constraints_Driver5'].nodes
	a.Set(name='Constraints_Driver5',nodes=node_O)
	node_O = Inst.sets['Constraints_Driver6'].nodes
	a.Set(name='Constraints_Driver6',nodes=node_O)
	print '### Successfully!'



def Sort_node_sets(Wx,Ly,Dz):
	eps1 = 1e-3
	Lb = Step*(W_a+D_a)
	La = Ly -Lb
	#
	a = mdb.models['Model-1'].rootAssembly
	nodes_0 = a.sets['NodeSet-SURFS-Y0'].nodes
	NodeDict_E1 = {}
	NodeDict_E6 = {}
	NodeDict_E15 = {}
	NodeDict_E16 = {}
	NodeDict_Y0 = {}
	for i in nodes_0:
		Di_Keys = i.label
		Di_Vaule = i.coordinates
		xx = round(i.coordinates[0],4)
		yy = round(i.coordinates[1],4)
		zz = round(i.coordinates[2],4)
		if(xx>-Wx/2.0 and xx<Wx/2.0 and zz>0.0 and zz<Dz):
			NodeDict_Y0[Di_Keys] = Di_Vaule
		if(xx==-Wx/2.0 and yy==-Ly/2.0 and zz>0.0 and zz<Dz):
			NodeDict_E1[Di_Keys] = Di_Vaule
		if(xx== Wx/2.0 and yy==-Ly/2.0 and zz>0.0 and zz<Dz):
			NodeDict_E6[Di_Keys] = Di_Vaule
		if(xx>-Wx/2.0 and xx<Wx/2.0 and zz==0.0):
			NodeDict_E15[Di_Keys] = Di_Vaule
		if(xx>-Wx/2.0 and xx<Wx/2.0 and zz==Dz):
			NodeDict_E16[Di_Keys] = Di_Vaule
	SortedLable_Y0 = sorted(NodeDict_Y0, key=lambda k: (round(NodeDict_Y0[k][0],6),round(NodeDict_Y0[k][2],6),k))
	SortedLable_E1 = sorted(NodeDict_E1, key=lambda k: (round(NodeDict_E1[k][0],6),round(NodeDict_E1[k][2],6),k))
	SortedLable_E6 = sorted(NodeDict_E6, key=lambda k: (round(NodeDict_E6[k][0],6),round(NodeDict_E6[k][2],6),k))
	SortedLable_E15 = sorted(NodeDict_E15, key=lambda k: (round(NodeDict_E15[k][0],6),round(NodeDict_E15[k][2],6),k))
	SortedLable_E16 = sorted(NodeDict_E16, key=lambda k: (round(NodeDict_E16[k][0],6),round(NodeDict_E16[k][2],6),k))
	# print NodeDict_Y0
	# print SortedLable_Y0
	# print len(SortedLable_Y0)
	# print 'SortedLable_E1', SortedLable_E1
	# print 'SortedLable_E6', SortedLable_E6
	# print 'SortedLable_E15', SortedLable_E15
	# print 'SortedLable_E16', SortedLable_E16
	# #####
	a = mdb.models['Model-1'].rootAssembly
	nodes_0 = a.sets['NodeSet-SURFS-Y1'].nodes
	NodeDict_E3 = {}
	NodeDict_E4 = {}
	NodeDict_E17 = {}
	NodeDict_E18 = {}
	NodeDict_Y1 = {}
	for i in nodes_0:
		Di_Keys = i.label
		Di_Vaule = i.coordinates
		xx = round(i.coordinates[0],4)
		yy = round(i.coordinates[1],4)
		zz = round(i.coordinates[2],4)
		if(xx>-Wx/2.0 and xx<Wx/2.0 and zz>0.0 and zz<Dz):
			NodeDict_Y1[Di_Keys] = Di_Vaule
		if(xx==-Wx/2.0 and yy==Ly/2.0 and zz>0.0 and zz<Dz):
			NodeDict_E3[Di_Keys] = Di_Vaule
		if(xx== Wx/2.0 and yy==Ly/2.0 and zz>0.0 and zz<Dz):
			NodeDict_E4[Di_Keys] = Di_Vaule
		if(xx>-Wx/2.0 and xx<Wx/2.0 and zz==0.0):
			NodeDict_E17[Di_Keys] = Di_Vaule
		if(xx>-Wx/2.0 and xx<Wx/2.0 and zz==Dz):
			NodeDict_E18[Di_Keys] = Di_Vaule
	SortedLable_Y1 = sorted(NodeDict_Y1, key=lambda k: (round(NodeDict_Y1[k][0],6),round(NodeDict_Y1[k][2],6),k))
	SortedLable_E3 = sorted(NodeDict_E3, key=lambda k: (round(NodeDict_E3[k][0],6),round(NodeDict_E3[k][2],6),k))
	SortedLable_E4 = sorted(NodeDict_E4, key=lambda k: (round(NodeDict_E4[k][0],6),round(NodeDict_E4[k][2],6),k))
	SortedLable_E17 = sorted(NodeDict_E17, key=lambda k: (round(NodeDict_E17[k][0],6),round(NodeDict_E17[k][2],6),k))
	SortedLable_E18 = sorted(NodeDict_E18, key=lambda k: (round(NodeDict_E18[k][0],6),round(NodeDict_E18[k][2],6),k))
	# print NodeDict_Y1
	# print SortedLable_Y1
	# print len(SortedLable_Y1)
	# print 'SortedLable_E1', SortedLable_E3
	# print 'SortedLable_E6', SortedLable_E4
	# print 'SortedLable_E17', SortedLable_E17
	# print 'SortedLable_E18', SortedLable_E18
	#
	#
	#
	a = mdb.models['Model-1'].rootAssembly
	nodes_0 = a.sets['NodeSet-SURFS-Z0'].nodes
	NodeDict_E7 = {}
	NodeDict_E10 = {}
	NodeDict_E11 = {}
	NodeDict_E14 = {}
	NodeDict_Z0 = {}
	for i in nodes_0:
		Di_Keys = i.label
		Di_Vaule = i.coordinates
		xx = round(i.coordinates[0],4)
		yy = round(i.coordinates[1],4)
		zz = round(i.coordinates[2],4)
		if(xx>-Wx/2.0 and xx<Wx/2.0 and yy>-Ly/2.0 and yy<Ly/2.0):
			NodeDict_Z0[Di_Keys] = Di_Vaule
		if(xx==-Wx/2.0 and yy>Lb-Ly/2.0 and yy<Ly/2.0):
			NodeDict_E7[Di_Keys] = Di_Vaule
		if(xx==-Wx/2.0 and yy>-Ly/2.0 and yy<Lb-Ly/2.0):
			NodeDict_E11[Di_Keys] = Di_Vaule
		if(xx== Wx/2.0 and yy>-Ly/2.0 and yy<Ly/2.0-Lb):
			NodeDict_E10[Di_Keys] = Di_Vaule
		if(xx== Wx/2.0 and yy>Ly/2.0-Lb and yy<Ly/2.0):
			NodeDict_E14[Di_Keys] = Di_Vaule
	SortedLable_Z0 = sorted(NodeDict_Z0, key=lambda k: (round(NodeDict_Z0[k][0],6),round(NodeDict_Z0[k][1],6),k))
	SortedLable_E7 = sorted(NodeDict_E7, key=lambda k: (round(NodeDict_E7[k][0],6),round(NodeDict_E7[k][1],6),k))
	SortedLable_E10 = sorted(NodeDict_E10, key=lambda k: (round(NodeDict_E10[k][0],6),round(NodeDict_E10[k][1],6),k))
	SortedLable_E11 = sorted(NodeDict_E11, key=lambda k: (round(NodeDict_E11[k][0],6),round(NodeDict_E11[k][1],6),k))
	SortedLable_E14 = sorted(NodeDict_E14, key=lambda k: (round(NodeDict_E14[k][0],6),round(NodeDict_E14[k][1],6),k))
	# print SortedLable_Z0
	# print 'SortedLable_E7', SortedLable_E7
	# print 'SortedLable_E10', SortedLable_E10
	# print 'SortedLable_E11', SortedLable_E11
	# print 'SortedLable_E14', SortedLable_E14
	print len(SortedLable_Z0),len(SortedLable_E7),len(SortedLable_E10),len(SortedLable_E11),len(SortedLable_E14)
	# #
	#
	#
	#
	a = mdb.models['Model-1'].rootAssembly
	nodes_0 = a.sets['NodeSet-SURFS-Z1'].nodes
	NodeDict_E8 = {}
	NodeDict_E9 = {}
	NodeDict_E12 = {}
	NodeDict_E13 = {}
	NodeDict_Z1 = {}
	for i in nodes_0:
		Di_Keys = i.label
		Di_Vaule = i.coordinates
		xx = round(i.coordinates[0],4)
		yy = round(i.coordinates[1],4)
		zz = round(i.coordinates[2],4)
		if(xx>-Wx/2.0 and xx<Wx/2.0 and yy>-Ly/2.0 and yy<Ly/2.0):
			NodeDict_Z1[Di_Keys] = Di_Vaule
		if(xx==-Wx/2.0 and yy>Lb-Ly/2.0 and yy<Ly/2.0):
			NodeDict_E8[Di_Keys] = Di_Vaule
		if(xx==-Wx/2.0 and yy>-Ly/2.0 and yy<Lb-Ly/2.0):
			NodeDict_E12[Di_Keys] = Di_Vaule
		if(xx== Wx/2.0 and yy>-Ly/2.0 and yy<Ly/2.0-Lb):
			NodeDict_E9[Di_Keys] = Di_Vaule
		if(xx== Wx/2.0 and yy>Ly/2.0-Lb and yy<Ly/2.0):
			NodeDict_E13[Di_Keys] = Di_Vaule
	SortedLable_Z1 = sorted(NodeDict_Z1, key=lambda k: (round(NodeDict_Z1[k][0],6),round(NodeDict_Z1[k][1],6),k))
	SortedLable_E8 = sorted(NodeDict_E8, key=lambda k: (round(NodeDict_E8[k][0],6),round(NodeDict_E8[k][1],6),k))
	SortedLable_E9 = sorted(NodeDict_E9, key=lambda k: (round(NodeDict_E9[k][0],6),round(NodeDict_E9[k][1],6),k))
	SortedLable_E12 = sorted(NodeDict_E12, key=lambda k: (round(NodeDict_E12[k][0],6),round(NodeDict_E12[k][1],6),k))
	SortedLable_E13 = sorted(NodeDict_E13, key=lambda k: (round(NodeDict_E13[k][0],6),round(NodeDict_E13[k][1],6),k))
	# print SortedLable_Z1
	# print 'SortedLable_E8', SortedLable_E8
	# print 'SortedLable_E9', SortedLable_E9
	# print 'SortedLable_E12', SortedLable_E12
	# print 'SortedLable_E14', SortedLable_E13
	print len(SortedLable_Z1),len(SortedLable_E8),len(SortedLable_E9),len(SortedLable_E12),len(SortedLable_E13)

	#
	#
	#
	a = mdb.models['Model-1'].rootAssembly
	nodes_0 = a.sets['NodeSet-SURFS-X0'].nodes
	NodeDict_E2 = {}
	NodeDict_Xa0 = {}
	NodeDict_Xb0 = {}
	for i in nodes_0:
		Di_Keys = i.label
		Di_Vaule = i.coordinates
		xx = round(i.coordinates[0],4)
		yy = round(i.coordinates[1],4)
		zz = round(i.coordinates[2],4)
		if(yy<Ly/2.0 and yy>Lb-Ly/2.0 and zz>0.0 and zz<Dz):
			NodeDict_Xa0[Di_Keys] = Di_Vaule
		if(yy>-Ly/2.0 and yy<Lb-Ly/2.0 and zz>0.0 and zz<Dz):
			NodeDict_Xb0[Di_Keys] = Di_Vaule
		if(yy==Lb-Ly/2.0 and zz>0.0 and zz<Dz):
			NodeDict_E2[Di_Keys] = Di_Vaule
	SortedLable_Xa0 = sorted(NodeDict_Xa0, key=lambda k: (round(NodeDict_Xa0[k][1],6),round(NodeDict_Xa0[k][2],6),k))
	SortedLable_Xb0 = sorted(NodeDict_Xb0, key=lambda k: (round(NodeDict_Xb0[k][1],6),round(NodeDict_Xb0[k][2],6),k))
	SortedLable_E2 = sorted(NodeDict_E2, key=lambda k: (round(NodeDict_E2[k][1],6),round(NodeDict_E2[k][2],6),k))

	print len(SortedLable_Xa0),len(SortedLable_Xb0),len(SortedLable_E2)
	# #
	#
	#
	#
	a = mdb.models['Model-1'].rootAssembly
	nodes_0 = a.sets['NodeSet-SURFS-X1'].nodes
	NodeDict_E5 = {}
	NodeDict_Xa1 = {}
	NodeDict_Xb1 = {}
	for i in nodes_0:
		Di_Keys = i.label
		Di_Vaule = i.coordinates
		xx = round(i.coordinates[0],4)
		yy = round(i.coordinates[1],4)
		zz = round(i.coordinates[2],4)
		if(yy>-Ly/2.0 and yy<Ly/2.0-Lb and zz>0.0 and zz<Dz):
			NodeDict_Xa1[Di_Keys] = Di_Vaule
		if(yy>Ly/2.0-Lb and yy<Ly/2.0 and zz>0.0 and zz<Dz):
			NodeDict_Xb1[Di_Keys] = Di_Vaule
		if(yy==Ly/2.0-Lb and zz>0.0 and zz<Dz):
			NodeDict_E5[Di_Keys] = Di_Vaule
	SortedLable_Xa1 = sorted(NodeDict_Xa1, key=lambda k: (round(NodeDict_Xa1[k][1],6),round(NodeDict_Xa1[k][2],6),k))
	SortedLable_Xb1 = sorted(NodeDict_Xb1, key=lambda k: (round(NodeDict_Xb1[k][1],6),round(NodeDict_Xb1[k][2],6),k))
	SortedLable_E5 = sorted(NodeDict_E5, key=lambda k: (round(NodeDict_E5[k][1],6),round(NodeDict_E5[k][2],6),k))

	print len(SortedLable_Xa1),len(SortedLable_Xb1),len(SortedLable_E5)
	
	
	#
	SortedLable_E = []
	for i in range(18):
		p=eval('SortedLable_E'+ str(i+1))
		SortedLable_E = SortedLable_E + [p]
	SortedLable_F = [SortedLable_Xb0]+[SortedLable_Xb1]+[SortedLable_Xa0]+[SortedLable_Xa1]+ \
		[SortedLable_Y0]+[SortedLable_Y1]+[SortedLable_Z0]+[SortedLable_Z1]
	return (SortedLable_E,SortedLable_F)

def Create_steps(LoadVector):
	# session.viewports['Viewport: 1'].assemblyDisplay.setValues(adaptiveMeshConstraints=ON)
	print '#  ____  _        _   _        ____  _             #'
	print '# / ___|| |_ __ _| |_(_) ___  / ___|| |_ ___ _ __  #'
	print '# \___ \| __/ _` | __| |/ __| \___ \| __/ _ \ `_ \ #'
	print '#  ___) | |_ (_| | |_| | (__   ___) | |_  __/ |_) |#'
	print '# |____/ \__\__,_|\__|_|\___| |____/ \__\___| .__/ #'
	print '#                                           |_|    #'
	#
	# Using Multiple load case in one perturbation step
	#
	mdb.models['Model-1'].StaticLinearPerturbationStep(name='Step-Mechanical', 
		previous='Initial', description='Step_Homogenized_properties')
	print '### Create Static Linear Perturbation Step Successfully!'

	# fixed BC of Vertex_3
	a = mdb.models['Model-1'].rootAssembly
	region = a.sets['Vertex_3']
	mdb.models['Model-1'].DisplacementBC(name='BC-Fixed', createStepName='Initial', 
		region=region, u1=SET, u2=SET, u3=SET, ur1=UNSET, ur2=UNSET, ur3=UNSET, 
		amplitude=UNSET, distributionType=UNIFORM, fieldName='', localCsys=None)
	#
	# Add Loading on Constraints_Driver
	#
	print '### Begin to create load case step Fxx, Fyy, Fzz, Fxy, Fyz, Fxz...'
	a = mdb.models['Model-1'].rootAssembly
	region = a.sets['Constraints_Driver1']
	mdb.models['Model-1'].ConcentratedForce(name='Load-Fx', 
		createStepName='Step-Mechanical', region=region, cf1=LoadVector[0], 
		distributionType=UNIFORM, field='', localCsys=None)
	a = mdb.models['Model-1'].rootAssembly
	region = a.sets['Constraints_Driver2']
	mdb.models['Model-1'].ConcentratedForce(name='Load-Fy', 
		createStepName='Step-Mechanical', region=region, cf1=LoadVector[1], 
		distributionType=UNIFORM, field='', localCsys=None)
	a = mdb.models['Model-1'].rootAssembly
	region = a.sets['Constraints_Driver3']
	mdb.models['Model-1'].ConcentratedForce(name='Load-Fz', 
		createStepName='Step-Mechanical', region=region, cf1=LoadVector[2], 
		distributionType=UNIFORM, field='', localCsys=None)
	a = mdb.models['Model-1'].rootAssembly
	region = a.sets['Constraints_Driver4']
	mdb.models['Model-1'].ConcentratedForce(name='Load-Fyz', 
		createStepName='Step-Mechanical', region=region, cf1=LoadVector[3], 
		distributionType=UNIFORM, field='', localCsys=None)	
	a = mdb.models['Model-1'].rootAssembly
	region = a.sets['Constraints_Driver5']
	mdb.models['Model-1'].ConcentratedForce(name='Load-Fzx', 
		createStepName='Step-Mechanical', region=region, cf1=LoadVector[4], 
		distributionType=UNIFORM, field='', localCsys=None)	
	a = mdb.models['Model-1'].rootAssembly
	region = a.sets['Constraints_Driver6']
	mdb.models['Model-1'].ConcentratedForce(name='Load-Fxy', 
		createStepName='Step-Mechanical', region=region, cf1=LoadVector[5], 
		distributionType=UNIFORM, field='', localCsys=None)			
	#
	# Using Multiple load case in one perturbation step
	#
	mdb.models['Model-1'].steps['Step-Mechanical'].LoadCase(name='LoadCases_Fx', 
		loads=(('Load-Fx', 1.0), ),boundaryConditions=(('BC-Fixed', 1.0), ))
	mdb.models['Model-1'].steps['Step-Mechanical'].LoadCase(name='LoadCases_Fy', 
		loads=(('Load-Fy', 1.0), ),boundaryConditions=(('BC-Fixed', 1.0), ))
	mdb.models['Model-1'].steps['Step-Mechanical'].LoadCase(name='LoadCases_Fz', 
		loads=(('Load-Fz', 1.0), ),boundaryConditions=(('BC-Fixed', 1.0), ))
	mdb.models['Model-1'].steps['Step-Mechanical'].LoadCase(name='LoadCases_Fyz', 
		loads=(('Load-Fyz', 1.0), ),boundaryConditions=(('BC-Fixed', 1.0), ))		
	mdb.models['Model-1'].steps['Step-Mechanical'].LoadCase(name='LoadCases_Fzx', 
		loads=(('Load-Fzx', 1.0), ),boundaryConditions=(('BC-Fixed', 1.0), ))		
	mdb.models['Model-1'].steps['Step-Mechanical'].LoadCase(name='LoadCases_Fxy', 
		loads=(('Load-Fxy', 1.0), ),boundaryConditions=(('BC-Fixed', 1.0), ))	
	#
	# output of Constraints_Driver 1-6
	# 
	mdb.models['Model-1'].fieldOutputRequests['F-Output-1'].setValues(variables=('S', 'U'))
	regionDef=mdb.models['Model-1'].rootAssembly.sets['Constraints_Driver1']
	mdb.models['Model-1'].FieldOutputRequest(name='F-Output-Displacement1', 
		createStepName='Step-Mechanical', variables=('U', ), frequency=1, 
		region=regionDef, sectionPoints=DEFAULT, rebar=EXCLUDE)
	regionDef=mdb.models['Model-1'].rootAssembly.sets['Constraints_Driver2']
	mdb.models['Model-1'].FieldOutputRequest(name='F-Output-Displacement2', 
		createStepName='Step-Mechanical', variables=('U', ), frequency=1, 
		region=regionDef, sectionPoints=DEFAULT, rebar=EXCLUDE)
	regionDef=mdb.models['Model-1'].rootAssembly.sets['Constraints_Driver3']
	mdb.models['Model-1'].FieldOutputRequest(name='F-Output-Displacement3', 
		createStepName='Step-Mechanical', variables=('U', ), frequency=1, 
		region=regionDef, sectionPoints=DEFAULT, rebar=EXCLUDE)
	regionDef=mdb.models['Model-1'].rootAssembly.sets['Constraints_Driver4']
	mdb.models['Model-1'].FieldOutputRequest(name='F-Output-Displacement4', 
		createStepName='Step-Mechanical', variables=('U', ), frequency=1, 
		region=regionDef, sectionPoints=DEFAULT, rebar=EXCLUDE)
	regionDef=mdb.models['Model-1'].rootAssembly.sets['Constraints_Driver5']
	mdb.models['Model-1'].FieldOutputRequest(name='F-Output-Displacement5', 
		createStepName='Step-Mechanical', variables=('U', ), frequency=1, 
		region=regionDef, sectionPoints=DEFAULT, rebar=EXCLUDE)
	regionDef=mdb.models['Model-1'].rootAssembly.sets['Constraints_Driver6']
	mdb.models['Model-1'].FieldOutputRequest(name='F-Output-Displacement6', 
		createStepName='Step-Mechanical', variables=('U', ), frequency=1, 
		region=regionDef, sectionPoints=DEFAULT, rebar=EXCLUDE)
	print '### Successfully!'

def Insert_Equations(W_a, D_a, Wx, Ly, Dz, Step):
	print '#  _____            _   _                  #'
	print '# | ____|__ _ _   _| |_(_) ___  _ __  ___  #'
	print '# |  _| / _` | | | | __| |/ _ \| `_ \/ __| #'
	print '# | |___ (_| | |_| | |_| | (_) | | | \__ \ #'
	print '# |_____\__, |\__,_|\__|_|\___/|_| |_|___/ #'
	print '#          |_|                             #'
	print '### Creat PBC Equations for faces, edges, vertices...'
	Lb = Step * (W_a+D_a)
	La = Ly - Lb
	# session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=OFF, bcs=OFF, 
		# predefinedFields=OFF, interactions=ON, constraints=ON, engineeringFeatures=ON)
	#
	# Faces
	#
	# Faces 1-2
	mdb.models['Model-1'].Equation(name='Equ-Face121', terms=(
		(1.0, 'Face_2', 1), (-1.0, 'Face_1', 1), 
		(-1.0*Wx, 'Constraints_Driver1', 1), (-1.0*La, 'Constraints_Driver6', 1)))
	mdb.models['Model-1'].Equation(name='Equ-Face122', terms=(
		(1.0, 'Face_2', 2), (-1.0, 'Face_1', 2), 
		(-1.0*La, 'Constraints_Driver2', 1)))
	mdb.models['Model-1'].Equation(name='Equ-Face123', terms=(
		(1.0, 'Face_2', 3), (-1.0, 'Face_1', 3), ))
	# Face 3-4
	mdb.models['Model-1'].Equation(name='Equ-Face341', terms=(
		(1.0, 'Face_4', 1), (-1.0, 'Face_3', 1), 
		(-1.0*Wx, 'Constraints_Driver1', 1), (1.0*Lb, 'Constraints_Driver6', 1)))
	mdb.models['Model-1'].Equation(name='Equ-Face342', terms=(
		(1.0, 'Face_4', 2), (-1.0, 'Face_3', 2), 
		(1.0*Lb, 'Constraints_Driver2', 1)))
	mdb.models['Model-1'].Equation(name='Equ-Face343', terms=(
		(1.0, 'Face_4', 3), (-1.0, 'Face_3', 3), ))
	# Face 5-6
	mdb.models['Model-1'].Equation(name='Equ-Face561', terms=(
		(1.0, 'Face_6', 1), (-1.0, 'Face_5', 1), 
		(-1.0*Ly, 'Constraints_Driver6', 1)))
	mdb.models['Model-1'].Equation(name='Equ-Face562', terms=(
		(1.0, 'Face_6', 2), (-1.0, 'Face_5', 2), 
		(-1.0*Ly, 'Constraints_Driver2', 1)))
	mdb.models['Model-1'].Equation(name='Equ-Face563', terms=(
		(1.0, 'Face_6', 3), (-1.0, 'Face_5', 3), ))
	# Face 7-8
	mdb.models['Model-1'].Equation(name='Equ-Face781', terms=(
		(1.0, 'Face_8', 1), (-1.0, 'Face_7', 1), 
		(-1.0*Dz, 'Constraints_Driver5', 1), ))
	mdb.models['Model-1'].Equation(name='Equ-Face782', terms=(
		(1.0, 'Face_8', 2), (-1.0, 'Face_7', 2), 
		(-1.0*Dz, 'Constraints_Driver4', 1)))
	mdb.models['Model-1'].Equation(name='Equ-Face783', terms=(
		(1.0, 'Face_8', 3), (-1.0, 'Face_7', 3), 
		(-1.0*Dz, 'Constraints_Driver3', 1)))	
	#
	# Edges
	#
	# Edges 3-1
	mdb.models['Model-1'].Equation(name='Equ-Edge11', terms=(
		(1.0, 'Edge_3', 1), (-1.0, 'Edge_1', 1), 
		(-1.0*Ly, 'Constraints_Driver6', 1)))
	mdb.models['Model-1'].Equation(name='Equ-Edge12', terms=(
		(1.0, 'Edge_3', 2), (-1.0, 'Edge_1', 2), 
		(-1.0*Ly, 'Constraints_Driver2', 1)))
	mdb.models['Model-1'].Equation(name='Equ-Edge13', terms=(
		(1.0, 'Edge_3', 3), (-1.0, 'Edge_1', 3), ))	
	# Edges 5-1
	mdb.models['Model-1'].Equation(name='Equ-Edge21', terms=(
		(1.0, 'Edge_5', 1), (-1.0, 'Edge_1', 1), 
		(-1.0*Wx, 'Constraints_Driver1', 1), (-1.0*La, 'Constraints_Driver6', 1)))
	mdb.models['Model-1'].Equation(name='Equ-Edge22', terms=(
		(1.0, 'Edge_5', 2), (-1.0, 'Edge_1', 2), 
		(-1.0*La, 'Constraints_Driver2', 1)))
	mdb.models['Model-1'].Equation(name='Equ-Edge23', terms=(
		(1.0, 'Edge_5', 3), (-1.0, 'Edge_1', 3), ))
	# Edge 6-4
	mdb.models['Model-1'].Equation(name='Equ-Edge31', terms=(
		(-1.0, 'Edge_6', 1), (1.0, 'Edge_4', 1), 
		(-1.0*Ly, 'Constraints_Driver6', 1)))
	mdb.models['Model-1'].Equation(name='Equ-Edge32', terms=(
		(-1.0, 'Edge_6', 2), (1.0, 'Edge_4', 2), 
		(-1.0*Ly, 'Constraints_Driver2', 1)))
	mdb.models['Model-1'].Equation(name='Equ-Edge33', terms=(
		(-1.0, 'Edge_6', 3), (1.0, 'Edge_4', 3), ))			
	# Edge 4-2
	mdb.models['Model-1'].Equation(name='Equ-Edge41', terms=(
		(1.0, 'Edge_4', 1), (-1.0, 'Edge_2', 1), 
		(-1.0*Wx, 'Constraints_Driver1', 1), (-1.0*La, 'Constraints_Driver6', 1)))
	mdb.models['Model-1'].Equation(name='Equ-Edge42', terms=(
		(1.0, 'Edge_4', 2), (-1.0, 'Edge_2', 2), 
		(-1.0*La, 'Constraints_Driver2', 1)))
	mdb.models['Model-1'].Equation(name='Equ-Edge43', terms=(
		(1.0, 'Edge_4', 3), (-1.0, 'Edge_2', 3), ))
	# Edge 8-7
	mdb.models['Model-1'].Equation(name='Equ-Edge51', terms=(
		(1.0, 'Edge_8', 1), (-1.0, 'Edge_7', 1), 
		(-1.0*Dz, 'Constraints_Driver5', 1), ))
	mdb.models['Model-1'].Equation(name='Equ-Edge52', terms=(
		(1.0, 'Edge_8', 2), (-1.0, 'Edge_7', 2), 
		(-1.0*Dz, 'Constraints_Driver4', 1)))
	mdb.models['Model-1'].Equation(name='Equ-Edge53', terms=(
		(1.0, 'Edge_8', 3), (-1.0, 'Edge_7', 3), 
		(-1.0*Dz, 'Constraints_Driver3', 1)))	
	# Edge 9-10
	mdb.models['Model-1'].Equation(name='Equ-Edge61', terms=(
		(1.0, 'Edge_9', 1), (-1.0, 'Edge_10', 1), 
		(-1.0*Dz, 'Constraints_Driver5', 1), ))
	mdb.models['Model-1'].Equation(name='Equ-Edge62', terms=(
		(1.0, 'Edge_9', 2), (-1.0, 'Edge_10', 2), 
		(-1.0*Dz, 'Constraints_Driver4', 1)))
	mdb.models['Model-1'].Equation(name='Equ-Edge63', terms=(
		(1.0, 'Edge_9', 3), (-1.0, 'Edge_10', 3), 
		(-1.0*Dz, 'Constraints_Driver3', 1)))
	# Edge 10-7
	mdb.models['Model-1'].Equation(name='Equ-Edge71', terms=(
		(1.0, 'Edge_10', 1), (-1.0, 'Edge_7', 1), 
		(-1.0*Wx, 'Constraints_Driver1', 1), (1.0*Lb, 'Constraints_Driver6', 1)))
	mdb.models['Model-1'].Equation(name='Equ-Edge72', terms=(
		(1.0, 'Edge_10', 2), (-1.0, 'Edge_7', 2), 
		(1.0*Lb, 'Constraints_Driver2', 1)))
	mdb.models['Model-1'].Equation(name='Equ-Edge73', terms=(
		(1.0, 'Edge_10', 3), (-1.0, 'Edge_7', 3),))
	# Edge 13-12 
	mdb.models['Model-1'].Equation(name='Equ-Edge81', terms=(
		(1.0, 'Edge_13', 1), (-1.0, 'Edge_12', 1), 
		(-1.0*Wx, 'Constraints_Driver1', 1), (-1.0*La, 'Constraints_Driver6', 1)))
	mdb.models['Model-1'].Equation(name='Equ-Edge82', terms=(
		(1.0, 'Edge_13', 2), (-1.0, 'Edge_12', 2), 
		(-1.0*La, 'Constraints_Driver2', 1)))
	mdb.models['Model-1'].Equation(name='Equ-Edge83', terms=(
		(1.0, 'Edge_13', 3), (-1.0, 'Edge_12', 3), ))
	# Edge 12-11
	mdb.models['Model-1'].Equation(name='Equ-Edge91', terms=(
		(1.0, 'Edge_12', 1), (-1.0, 'Edge_11', 1), 
		(-1.0*Dz, 'Constraints_Driver5', 1), ))
	mdb.models['Model-1'].Equation(name='Equ-Edge92', terms=(
		(1.0, 'Edge_12', 2), (-1.0, 'Edge_11', 2), 
		(-1.0*Dz, 'Constraints_Driver4', 1)))
	mdb.models['Model-1'].Equation(name='Equ-Edge93', terms=(
		(1.0, 'Edge_12', 3), (-1.0, 'Edge_11', 3), 
		(-1.0*Dz, 'Constraints_Driver3', 1)))
	# Edge 14-11
	mdb.models['Model-1'].Equation(name='Equ-Edge101', terms=(
		(1.0, 'Edge_14', 1), (-1.0, 'Edge_11', 1), 
		(-1.0*Wx, 'Constraints_Driver1', 1), (-1.0*La, 'Constraints_Driver6', 1)))
	mdb.models['Model-1'].Equation(name='Equ-Edge102', terms=(
		(1.0, 'Edge_14', 2), (-1.0, 'Edge_11', 2), 
		(-1.0*La, 'Constraints_Driver2', 1)))
	mdb.models['Model-1'].Equation(name='Equ-Edge103', terms=(
		(1.0, 'Edge_14', 3), (-1.0, 'Edge_11', 3), ))
	# Edge 17-16
	mdb.models['Model-1'].Equation(name='Equ-Edge111', terms=(
		(1.0, 'Edge_17', 1), (-1.0, 'Edge_16', 1), 
		(-1.0*Ly, 'Constraints_Driver6', 1)))
	mdb.models['Model-1'].Equation(name='Equ-Edge112', terms=(
		(1.0, 'Edge_17', 2), (-1.0, 'Edge_16', 2), 
		(-1.0*Ly, 'Constraints_Driver2', 1)))
	mdb.models['Model-1'].Equation(name='Equ-Edge113', terms=(
		(1.0, 'Edge_17', 3), (-1.0, 'Edge_16', 3), ))	
	# Edge 16-15
	mdb.models['Model-1'].Equation(name='Equ-Edge121', terms=(
		(1.0, 'Edge_16', 1), (-1.0, 'Edge_15', 1), 
		(-1.0*Dz, 'Constraints_Driver5', 1), ))
	mdb.models['Model-1'].Equation(name='Equ-Edge122', terms=(
		(1.0, 'Edge_16', 2), (-1.0, 'Edge_15', 2), 
		(-1.0*Dz, 'Constraints_Driver4', 1)))
	mdb.models['Model-1'].Equation(name='Equ-Edge123', terms=(
		(1.0, 'Edge_16', 3), (-1.0, 'Edge_15', 3), 
		(-1.0*Dz, 'Constraints_Driver3', 1)))
	# Edge 18-15
	mdb.models['Model-1'].Equation(name='Equ-Edge131', terms=(
		(1.0, 'Edge_18', 1), (-1.0, 'Edge_15', 1), 
		(-1.0*Ly, 'Constraints_Driver6', 1)))
	mdb.models['Model-1'].Equation(name='Equ-Edge132', terms=(
		(1.0, 'Edge_18', 2), (-1.0, 'Edge_15', 2), 
		(-1.0*Ly, 'Constraints_Driver2', 1)))
	mdb.models['Model-1'].Equation(name='Equ-Edge133', terms=(
		(1.0, 'Edge_18', 3), (-1.0, 'Edge_15', 3), ))
	#
	# Vertex
	#
	# Vertex 2-1
	mdb.models['Model-1'].Equation(name='Equ-Vertex11', terms=(
		(1.0, 'Vertex_2', 1), (-1.0, 'Vertex_1', 1), 
		(-1.0*Dz, 'Constraints_Driver5', 1), ))
	mdb.models['Model-1'].Equation(name='Equ-Vertex12', terms=(
		(1.0, 'Vertex_2', 2), (-1.0, 'Vertex_1', 2), 
		(-1.0*Dz, 'Constraints_Driver4', 1)))
	mdb.models['Model-1'].Equation(name='Equ-Vertex13', terms=(
		(1.0, 'Vertex_2', 3), (-1.0, 'Vertex_1', 3), 
		(-1.0*Dz, 'Constraints_Driver3', 1)))
	# Vertex 6-5
	mdb.models['Model-1'].Equation(name='Equ-Vertex21', terms=(
		(1.0, 'Vertex_6', 1), (-1.0, 'Vertex_5', 1), 
		(-1.0*Dz, 'Constraints_Driver5', 1), ))
	mdb.models['Model-1'].Equation(name='Equ-Vertex22', terms=(
		(1.0, 'Vertex_6', 2), (-1.0, 'Vertex_5', 2), 
		(-1.0*Dz, 'Constraints_Driver4', 1)))
	mdb.models['Model-1'].Equation(name='Equ-Vertex23', terms=(
		(1.0, 'Vertex_6', 3), (-1.0, 'Vertex_5', 3), 
		(-1.0*Dz, 'Constraints_Driver3', 1)))
	# Vertex 10-9
	mdb.models['Model-1'].Equation(name='Equ-Vertex31', terms=(
		(1.0, 'Vertex_10', 1), (-1.0, 'Vertex_9', 1), 
		(-1.0*Dz, 'Constraints_Driver5', 1), ))
	mdb.models['Model-1'].Equation(name='Equ-Vertex32', terms=(
		(1.0, 'Vertex_10', 2), (-1.0, 'Vertex_9', 2), 
		(-1.0*Dz, 'Constraints_Driver4', 1)))
	mdb.models['Model-1'].Equation(name='Equ-Vertex33', terms=(
		(1.0, 'Vertex_10', 3), (-1.0, 'Vertex_9', 3), 
		(-1.0*Dz, 'Constraints_Driver3', 1)))
	# Vertex 1-5
	mdb.models['Model-1'].Equation(name='Equ-Vertex41', terms=(
		(1.0, 'Vertex_1', 1), (-1.0, 'Vertex_5', 1), 
		(-1.0*Wx, 'Constraints_Driver1', 1), (1.0*Lb, 'Constraints_Driver6', 1)))
	mdb.models['Model-1'].Equation(name='Equ-Vertex42', terms=(
		(1.0, 'Vertex_1', 2), (-1.0, 'Vertex_5', 2), 
		(1.0*Lb, 'Constraints_Driver2', 1)))
	mdb.models['Model-1'].Equation(name='Equ-Vertex43', terms=(
		(1.0, 'Vertex_1', 3), (-1.0, 'Vertex_5', 3), ))
	# Vertex 9-1
	mdb.models['Model-1'].Equation(name='Equ-Vertex51', terms=(
		(1.0, 'Vertex_9', 1), (-1.0, 'Vertex_1', 1), 
		(-1.0*Ly, 'Constraints_Driver6', 1)))
	mdb.models['Model-1'].Equation(name='Equ-Vertex52', terms=(
		(1.0, 'Vertex_9', 2), (-1.0, 'Vertex_1', 2), 
		(-1.0*Ly, 'Constraints_Driver2', 1)))
	mdb.models['Model-1'].Equation(name='Equ-Vertex53', terms=(
		(1.0, 'Vertex_9', 3), (-1.0, 'Vertex_1', 3), ))	
	# Vertex 4-3
	mdb.models['Model-1'].Equation(name='Equ-Vertex61', terms=(
		(1.0, 'Vertex_4', 1), (-1.0, 'Vertex_3', 1), 
		(-1.0*Dz, 'Constraints_Driver5', 1), ))
	mdb.models['Model-1'].Equation(name='Equ-Vertex62', terms=(
		(1.0, 'Vertex_4', 2), (-1.0, 'Vertex_3', 2), 
		(-1.0*Dz, 'Constraints_Driver4', 1)))
	mdb.models['Model-1'].Equation(name='Equ-Vertex63', terms=(
		(1.0, 'Vertex_4', 3), (-1.0, 'Vertex_3', 3), 
		(-1.0*Dz, 'Constraints_Driver3', 1)))
	# Vertex 8-7
	mdb.models['Model-1'].Equation(name='Equ-Vertex71', terms=(
		(1.0, 'Vertex_8', 1), (-1.0, 'Vertex_7', 1), 
		(-1.0*Dz, 'Constraints_Driver5', 1), ))
	mdb.models['Model-1'].Equation(name='Equ-Vertex72', terms=(
		(1.0, 'Vertex_8', 2), (-1.0, 'Vertex_7', 2), 
		(-1.0*Dz, 'Constraints_Driver4', 1)))
	mdb.models['Model-1'].Equation(name='Equ-Vertex73', terms=(
		(1.0, 'Vertex_8', 3), (-1.0, 'Vertex_7', 3), 
		(-1.0*Dz, 'Constraints_Driver3', 1)))
	# Vertex 12-11
	mdb.models['Model-1'].Equation(name='Equ-Vertex81', terms=(
		(1.0, 'Vertex_12', 1), (-1.0, 'Vertex_11', 1), 
		(-1.0*Dz, 'Constraints_Driver5', 1), ))
	mdb.models['Model-1'].Equation(name='Equ-Vertex82', terms=(
		(1.0, 'Vertex_12', 2), (-1.0, 'Vertex_11', 2), 
		(-1.0*Dz, 'Constraints_Driver4', 1)))
	mdb.models['Model-1'].Equation(name='Equ-Vertex83', terms=(
		(1.0, 'Vertex_12', 3), (-1.0, 'Vertex_11', 3), 
		(-1.0*Dz, 'Constraints_Driver3', 1)))
	# Vertex 7-11
	mdb.models['Model-1'].Equation(name='Equ-Vertex91', terms=(
		(1.0, 'Vertex_7', 1), (-1.0, 'Vertex_11', 1), 
		(-1.0*Wx, 'Constraints_Driver1', 1), (1.0*Lb, 'Constraints_Driver6', 1)))
	mdb.models['Model-1'].Equation(name='Equ-Vertex92', terms=(
		(1.0, 'Vertex_7', 2), (-1.0, 'Vertex_11', 2), 
		(1.0*Lb, 'Constraints_Driver2', 1)))
	mdb.models['Model-1'].Equation(name='Equ-Vertex93', terms=(
		(1.0, 'Vertex_7', 3), (-1.0, 'Vertex_11', 3), ))
	# Vertex 11-3
	mdb.models['Model-1'].Equation(name='Equ-Vertex101', terms=(
		(1.0, 'Vertex_11', 1), (-1.0, 'Vertex_3', 1), 
		(-1.0*Ly, 'Constraints_Driver6', 1)))
	mdb.models['Model-1'].Equation(name='Equ-Vertex102', terms=(
		(1.0, 'Vertex_11', 2), (-1.0, 'Vertex_3', 2), 
		(-1.0*Ly, 'Constraints_Driver2', 1)))
	mdb.models['Model-1'].Equation(name='Equ-Vertex103', terms=(
		(1.0, 'Vertex_11', 3), (-1.0, 'Vertex_3', 3), ))
	#
	print '### Finished!' 


def Rewrite_inp(SortedLable_E,SortedLable_F):
	# FACEs
	print '### Begin to reorder nodelabel_Edges...'

	s_E = []
	for n in range(18):
		ss=''
		count=0
		for i in range(len(SortedLable_E[n])):
			label = '%8d, ' %SortedLable_E[n][i]
			count+=1
			if count == 16:
				label = '%8d\n' %SortedLable_E[n][i]
				count = 0
			ss = ss+label
		nset = 'Edge_'+str(n+1)
		s_E = s_E +['*Nset, nset='+nset+', Unsorted\n' +ss +'\n']
	# print s_E
	print '### Finished!'

	print '### Begin to reorder nodelabel_Faces...'
	s_F = []
	for n in range(8):
		sf=''
		count=0
		for i in range(len(SortedLable_F[n])):
			label = '%8d, ' %SortedLable_F[n][i]
			count+=1
			if count == 16:
				label = '%8d\n' %SortedLable_F[n][i]
				count = 0
			sf = sf+label
		nset = 'Face_'+str(n+1)
		s_F = s_F +['*Nset, nset='+nset+', Unsorted\n' +sf +'\n']
	# print s_F[6:8]
	Reorderde_nodeSets = s_E+s_F
	print '### Finished!'
	
	
	# ####################
	# Rewrite INP file	##
	# ####################
	
	jobName = 'Job-'+ModelName
	mdb.Job(name=jobName, model='Model-1', description='', type=ANALYSIS, 
		atTime=None, waitMinutes=0, waitHours=0, queue=None, memory=99, 
		memoryUnits=PERCENTAGE, getMemoryFromAnalysis=True, 
		explicitPrecision=SINGLE, nodalOutputPrecision=SINGLE, echoPrint=OFF, 
		modelPrint=OFF, contactPrint=OFF, historyPrint=OFF, 
		userSubroutine='', 
		scratch='', resultsFormat=ODB, parallelizationMethodExplicit=DOMAIN, 
		numDomains=1, activateLoadBalancing=False, multiprocessingMode=DEFAULT, 
		numCpus=1, numGPUs=0)
	mdb.jobs[jobName].writeInput(consistencyChecking=OFF)
	
	import shutil
	shutil.copyfile(jobName+'.inp',jobName+'_pre.inp')
	f = open(jobName+'.inp','r+')
	line=f.readline()
	R_inp=[]
	i = 0
	deleter1=0
	deleter2=0
	deleter3=0
	deleter4=0
	deleter5=0
	while (line!=''):
		R_inp.append(line)
		if(line[0:31]=='*Nset, nset=Constraints_Driver6'):	 ## find the start of Edges node sets		 
			deleter1=i+2
		if(line[0:28]=='*Nset, nset=NodeSet-SURFS-X0'):	 ## find the start of useless Element sets		 
			deleter2=i
		line=f.readline()
		i+=1
	f.close	  
	#print deleter
	New_inp = R_inp[0:deleter1] + Reorderde_nodeSets + R_inp[deleter2:]
	print  '### Rewriting INP file under symmetric_loading Fxx,Fyy,Fzz,Fxy,Fyz,Fxz...'
	f2 = open(jobName+'.inp', 'w')
	for j in range(len(New_inp)):
		f2.write(New_inp[j])
	f2.close
	print '### Finished!' 
	
def Submit_Jobs(ModelName):
	print '#      _                _           _      #'
	print '#     / \   _ __   __ _| |_   _ ___(_)___  #'
	print '#    / _ \ | `_ \ / _` | | | | / __| / __| #'
	print '#   / ___ \| | | | (_| | | |_| \__ \ \__ \ #'
	print '#  /_/   \_\_| |_|\__,_|_|\__, |___/_|___/ #'
	print '#                         |___/            #'
	a = mdb.models['Model-1'].rootAssembly
	session.viewports['Viewport: 1'].setValues(displayedObject=a)
	# session.viewports['Viewport: 1'].assemblyDisplay.setValues(
		# optimizationTasks=OFF, geometricRestrictions=OFF, stopConditions=OFF)
	print '### Submit Job into Abaqus...'
	mdb.models['Model-1'].setValues(noPartsInputFile=ON)
	jobName = 'Job-'+ModelName
	mdb.Job(name=jobName, model='Model-1', description='', type=ANALYSIS, 
		atTime=None, waitMinutes=0, waitHours=0, queue=None, memory=99, 
		memoryUnits=PERCENTAGE, getMemoryFromAnalysis=True, 
		explicitPrecision=SINGLE, nodalOutputPrecision=SINGLE, echoPrint=OFF, 
		modelPrint=OFF, contactPrint=OFF, historyPrint=OFF, userSubroutine='', 
		scratch='', resultsFormat=ODB, multiprocessingMode=DEFAULT, numCpus=8, 
		numDomains=8, numGPUs=0)
	#mdb.jobs[jobName].writeInput(consistencyChecking=OFF)
	mdb.jobs[jobName].submit(consistencyChecking=OFF)
	mdb.jobs[jobName].waitForCompletion()



Wx = 2.060
Ly = 18.00
Dz = 0.800
Step = 1
W_a = 2.00
D_a = 2.50

Adding_sets(Wx,Ly,Dz,Step,W_a,D_a)
SortedLable_E,SortedLable_F = Sort_node_sets(Wx,Ly,Dz)
Rewrite_inp(SortedLable_E,SortedLable_F)