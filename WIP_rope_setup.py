
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

////

import pymel.core as pm


target = pm.PyNode('SR_mouth_riv')

startFrame = pm.playbackOptions(q = True, min = True)
endFrame = pm.playbackOptions(q = True, max = True)

pos_list = []

for i in range(int(startFrame), int(endFrame+1)):
    pos_list.append(pm.getAttr(target.t, time = i))

pm.curve(d = 3, p = pos_list)

////

import pymel.core as pm

sel_list = pm.ls(sl = True)
jnt_list = pm.listRelatives(sel_list, ad = True)

tfm_grp = pm.group(em = True, n = 'pxy_grp')

target_crv = pm.PyNode('SR_rope_anim_crv')

counter = 0

for jnt in jnt_list:
    poci = pm.createNode('pointOnCurveInfo', n = jnt.nodeName() + '_poci')
    target_crv.worldSpace >> poci.inputCurve
    poci.turnOnPercentage.set(True)
    par = 1.0/(len(jnt_list)-1)*counter
    poci.parameter.set(par)
    pxy_grp = pm.group(em = True, n = jnt.nodeName() + '_pxy')
    pm.parent(pxy_grp, tfm_grp)
    poci.position >> pxy_grp.t
    pm.parentConstraint(pxy_grp, jnt, skipRotate = 'none', skipTranslate = 'none', mo = False)
    counter += 1
