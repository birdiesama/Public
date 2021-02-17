import pymel.core as pm

value = 0.25

selection_list = pm.ls(sl = True)

crv_shape_list = pm.listRelatives(selection_list, type = 'nurbsCurve')
crv_shape_list = list(set(crv_shape_list))

for shape in crv_shape_list:
    if shape.isIntermediate():
        crv_shape_list.remove(shape)

bsh_list = pm.listConnections(crv_shape_list, type = 'blendShape')
bsh_list = list(set(bsh_list))

for bsh in bsh_list[0:1]:
    if 'OUTPUT' in bsh.nodeName():
        attrNm = bsh.stripNamespace().split('_BS')[0]
        pm.setAttr('{0}.{1}Shape'.format(bsh.nodeName(), attrNm), value)
