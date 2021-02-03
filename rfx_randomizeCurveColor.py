import pymel.core as pm
import random

class RandomCurveColor(object):

    def __init__(self, *args, **kwargs):

        super(RandomCurveColor, self).__init__(*args, **kwargs)

        self.color_rgb_dict = {}

        self.color_rgb_dict['blue']         = (0, 0, 1)
        self.color_rgb_dict['light_blue']   = (0, 0.8, 1)

        # self.color_rgb_dict['sea_green']    = (0.2, 0.55, 0.35)
        # self.color_rgb_dict['light_sea_green'] = (0.55, 0.75, 0.55)
        self.color_rgb_dict['sea_green']    = (0, 0.55, 0.55)
        self.color_rgb_dict['light_sea_green'] = (0, 0.75, 0.75)

        self.color_rgb_dict['green']        = (0, 1, 0)
        self.color_rgb_dict['light_green']  = (0.5, 1, 0.5)

        self.color_rgb_dict['yellow']       = (1, 1, 0)
        self.color_rgb_dict['light_yellow'] = (1, 1, 0.5)

        self.color_rgb_dict['orange']       = (1, 0.65, 0)
        self.color_rgb_dict['light_orange'] = (1, 0.6, 0.4)

        self.color_rgb_dict['red']          = (1, 0, 0)
        self.color_rgb_dict['light_red']    = (1, 0.25, 0.5)

        self.color_rgb_dict['brown']        = (0.6, 0.1, 0.1)
        self.color_rgb_dict['light_brown']  = (0.6, 0.3, 0.3)

        self.color_rgb_dict['purple']       = (0.6, 0, 0.8)
        self.color_rgb_dict['light_purple'] = (0.85, 0.6, 0.85)

        self.color_rgb_dict['pink']         = (1, 0.4, 0.7)
        self.color_rgb_dict['light_pink']   = (1, 0.7, 0.75)

        self.color_rgb_dict['skin']         = (1, 0.85, 0.75)
        self.color_rgb_dict['skin_light']   = (1, 0.9, 0.9)
        self.color_rgb_dict['skin_dark']    = (0.75, 0.55, 0.55)

        self.color_rgb_dict['black']        = (0, 0, 0)
        self.color_rgb_dict['dark_grey']    = (0.25, 0.25, 0.25)
        self.color_rgb_dict['grey']         = (0.5, 0.5, 0.5)
        self.color_rgb_dict['light_grey']   = (0.75, 0.75, 0.75)
        self.color_rgb_dict['white']        = (1, 1, 1)
        
    def is_list(self, target_list):
        if not isinstance(target_list, list):
            target_list = [target_list]
        return target_list
    
    def get_visible_shape(self, mesh):
        mesh = pm.PyNode(mesh)
        try:
            mesh_shape = mesh.getShape()
            if mesh_shape.isIntermediate():  # It's not the shape we see? Lets run through every shape and see
                mesh_shape_list = mesh.getShapes()
                for mesh_shape_prx in mesh_shape_list:
                    if not mesh_shape_prx.isIntermediate():
                        mesh_shape = mesh_shape_prx
            return mesh_shape
        except:
            return None

    def set_curve_shape_color(self, target_list, rgb=(0, 0, 0)):
        target_list = self.is_list(target_list) # general.misc
        for target in target_list:
            target = pm.PyNode(target)
            target_shape = self.get_visible_shape(target) # general.cleanup
            if rgb:
                r, g, b = rgb
                target_shape.overrideRGBColors.set(True)
                target_shape.overrideEnabled.set(True)
                target_shape.overrideColorRGB.set(r, g, b)
            else:
                target_shape.overrideEnabled.set(False)
   
    def random_curve_color(self, target, enable=True):
        
        system_random = random.SystemRandom()
        random_color_list = []
        random_color_list.append('white')
        random_color_list.append('light_yellow')
        random_color_list.append('light_blue')
        random_color_list.append('light_pink')
        random_color_list.append('light_brown')
        random_color_list.append('light_green')
        random_color_list.append('light_purple')

        crv_shape_list = pm.listRelatives(target, ad = True, type = 'nurbsCurve')
        crv_list = pm.listRelatives(crv_shape_list, parent = True)
        crv_list = list(set(crv_list))

        if enable:
            for crv in crv_list:
                self.set_curve_shape_color(crv, rgb = self.color_rgb_dict[str(system_random.choice(random_color_list))])
        else:
            self.set_curve_shape_color(crv_list, rgb = None)
    
    def run(self):
        selection_list = pm.ls(sl = True)
        curve_shape_list = pm.listRelatives(selection_list, ad = True, type = 'nurbsCurve')
        curve_list = pm.listRelatives(curve_shape_list, parent = True)
        curve_list = list(set(curve_list))
        self.random_curve_color(curve_list, enable = True)
        
rcc = RandomCurveColor()
rcc.run()
