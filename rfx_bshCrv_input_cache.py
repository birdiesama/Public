import pymel.core as pm

selection_list = pm.ls(sl = True)
geo_shape_list = pm.listRelatives(selection_list, ad = True, type = 'nurbsCurve')

geo_list = pm.listRelatives(geo_shape_list, parent = True)

geo_list = list(set(geo_list))

for geo in geo_list:
    driven = geo
    driver = geo.nodeName().replace(':', ':cache:')
    driver = driver.replace('_INPUT', '_CRV')
    driver = pm.PyNode(driver)
    pm.blendShape(driver, driven, origin='world', automatic=True, weight=[0, 1], envelope=1)[0]
        
