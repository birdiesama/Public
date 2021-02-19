import pymel.core as pm
import re

name_patern = 'OUTPUT'
key_value = 2.0
mode = 1 #1 = key, 0 = delete
bsn_attr_slot = 1 #0 = en, 1 = attr under the en


name_filter = re.compile(r'({0})'.format(name_patern))
to_select_list = []

blendshape_list = pm.ls(type = 'blendShape')
for blendshape in blendshape_list:
    if name_filter.search(blendshape.nodeName()):
        to_select_list.append(blendshape)

pm.select(to_select_list[0:1])

for each in to_select_list[0:1]:
    if bsn_attr_slot == 0:
        if mode:
            pm.setKeyframe(each, v = key_value, at = 'en')
        else:
            pm.cutKey(each, at = 'en')
    elif bsn_attr_slot == 1:         
        attr = pm.PyNode(each.nodeName() + '.' + 'weight[0]')
        if mode:
            pm.setKeyframe(attr, v = key_value)
        else:
            pm.cutKey(attr)
