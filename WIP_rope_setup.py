
import pymel.core as pm

rope_crv = pm.PyNode('rope_crv')
rope_crv = rope_crv.getShape()

pointOnCurveInfo = pm.createNode('pointOnCurveInfo')

rope_crv.worldSpace >> pointOnCurveInfo.inputCurve
pointOnCurveInfo.turnOnPercentage.set(True)

detail = 1000
val_list = [0]

for i in range(1, (detail-1)):
    val = (1.0/(detail-1))*i
    val_list.append(val)

val_list.append(1)

prev_joint = None

for val in val_list:
    pointOnCurveInfo.parameter.set(val)
    pos = (pointOnCurveInfo.position.get())
    joint = pm.createNode('joint')
    pm.xform(joint, t = pos)
    
    if prev_joint:
        pm.parent(joint, prev_joint)
    prev_joint = joint
       
pm.delete(pointOnCurveInfo)

#print(pointOnCurveInfo)