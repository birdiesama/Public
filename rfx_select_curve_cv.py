import pymel.core as pm

selection_list = pm.ls(sl = True)
curve_shp_list = pm.listRelatives(selection_list, ad = True, type = 'nurbsCurve')
curve_shp_list = list(set(curve_shp_list))
curve_list = pm.listRelatives(curve_shp_list, parent = True)
curve_list = list(set(curve_list))
to_select_list = []
for crv in curve_list:
    to_select_list.append(crv.nodeName() + '.cv[0:1]')
pm.select(to_select_list)
