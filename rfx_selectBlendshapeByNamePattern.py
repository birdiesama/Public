import pymel.core as pm
import re

name_patern = 'OUTPUT'

name_filter = re.compile(r'({0})'.format(name_patern))
to_select_list = []

blendshape_list = pm.ls(type = 'blendShape')
for blendshape in blendshape_list:
    if name_filter.search(blendshape.nodeName()):
        to_select_list.append(blendshape)

pm.select(to_select_list)
#print to_select_list
