import pymel.core as pm

en = True

sel_list = pm.ls(sl = True)[0]

fol_list = pm.listRelatives(sel_list, type = 'follicle', ad = True)
fol_list = list(set(fol_list))
 
for fol in fol_list:
    if en:
        fol.simulationMethod.set(2)
    else:
        fol.simulationMethod.set(0)
