
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

 ////

import pymel.core as pm

target_crv = pm.PyNode('rope_crv_skin')

cp = target_crv.cp.get(s = True)

jnt_list = []
jnt_cv_list = []

for i in range(0, cp):
    cv = pm.PyNode('{0}.cv[{1}]'.format(target_crv.nodeName(), i))
    cluster = pm.cluster(cv)[1]
    jnt = pm.createNode('joint', n = target_crv.nodeName() + '_1')
    pos = pm.xform(cluster, q = True, ws = True, rp = True)
    pm.xform(jnt, t = pos)
    pm.delete(cluster)
    jnt_list.append(jnt)
    jnt_cv_list.append([jnt, cv])

skinCluster = pm.skinCluster(target_crv, jnt_list)

for jnt_cv in jnt_cv_list:
    jnt, cv = jnt_cv    
    pm.skinPercent(skinCluster, cv, transformValue = [(jnt, 1)])
 
 #cmds.skinPercent( 'skinCluster1', 'pPlane1.vtx[100]', transformValue=[('joint1', 0.2), ('joint3', 0.8)])

/////

import pymel.core as pm

sel = pm.ls(sl = True)

tfm_list = pm.listRelatives(sel, ad = True)
tfm_list.sort()
tfm_list.reverse()

for tfm in tfm_list:
    pm.reorder(tfm, front = True)

/////

import pymel.core as pm

sel_list = pm.ls(sl = True)
jnt_list = pm.listRelatives(sel_list, ad = True)

tfm_grp = pm.group(em = True, n = 'pxy_grp')
pm.addAttr(tfm_grp, ln = 'par_max', at = 'double', min = 0, max = 1, dv = 1, keyable = True)
pm.addAttr(tfm_grp, ln = 'par_min', at = 'double', min = 0, max = 1, dv = 0, keyable = True)

target_crv = pm.PyNode('SL_rope_anim_crv')

counter = 0

for jnt in jnt_list:
    poci = pm.createNode('pointOnCurveInfo', n = jnt.nodeName() + '_poci')
    target_crv.worldSpace >> poci.inputCurve
    poci.turnOnPercentage.set(True)
    
    # parameter range
    parRange_pma = pm.createNode('plusMinusAverage', n = jnt.nodeName() + '_parRange_pma')
    parRange_pma.operation.set(2)
    tfm_grp.par_max >> parRange_pma.input2D[0].input2Dx
    tfm_grp.par_min >> parRange_pma.input2D[1].input2Dx
    
    # parameter value
    parVal_mdv = pm.createNode('multiplyDivide', n = jnt.nodeName() + '_parVal_1_mdv')

    parVal_mdv.operation.set(2)
    parRange_pma.output2D.output2Dx >> parVal_mdv.i1x
    parVal_mdv.i2x.set(len(jnt_list)-1)
    
    parVal_2_mdv = pm.createNode('multiplyDivide', n = jnt.nodeName() + '_parVal_2_mdv')
    parVal_2_mdv.operation.set(1)
    parVal_mdv.ox >> parVal_2_mdv.i1x
    parVal_2_mdv.i2x.set(counter)
    
    parVal_2_mdv.ox >> poci.parameter
    
    pxy_grp = pm.group(em = True, n = jnt.nodeName() + '_pxy')
    pm.parent(pxy_grp, tfm_grp)
    poci.position >> pxy_grp.t
    pm.parentConstraint(pxy_grp, jnt, skipRotate = 'none', skipTranslate = 'none', mo = False)
    counter += 1
