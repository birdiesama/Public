import pymel.core as pm

# select your curve
selection_list = pm.ls(sl = True)

# list all curve nodes from selection
crv_shape_list = pm.listRelatives(selection_list, type = 'nurbsCurve')
# remove duplicates
crv_shape_list = list(set(crv_shape_list))

# remove unused shapes (e.g. orig)
for shape in crv_shape_list:
    if shape.isIntermediate():
        crv_shape_list.remove(shape)

# list blendshapes from crv nodes
#bsh_list = pm.listConnections(crv_shape_list, type = 'blendShape')
con_list = pm.listConnections(crv_shape_list, shapes = True)
con_list = list(set(con_list))

for con in con_list:
    if 'OUTPUT_BSSet' in con.nodeName():
        bsn = pm.PyNode(con.nodeName().replace('_BSSet', '_BS'))
        bsn.en.disconnect()


'''
import pymel.core as pm

# select your curve / group
selection_list = pm.ls(sl = True)

# list all curve nodes from selection
crv_shape_list = pm.listRelatives(selection_list, type = 'nurbsCurve')
# remove duplicates
crv_shape_list = list(set(crv_shape_list))
# remove unused shapes (e.g. orig)
for shape in crv_shape_list:
    if shape.isIntermediate():
        crv_shape_list.remove(shape)

# list blendshapes from crv nodes
bsh_list = pm.listConnections(crv_shape_list, type = 'blendShape')
# remove duplicates
bsh_list = list(set(bsh_list))
# check the blendshape name just in case
for bsh in bsh_list:
    if 'OUTPUT' in bsh.nodeName():
        bsh.en.disconnect()
'''
