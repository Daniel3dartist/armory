from arm.logicnode.arm_nodes import *

class RpConfigNode(ArmLogicTreeNode):
    """Configure renderpath node"""
    bl_idname = 'LNRpConfigNode'
    bl_label = 'Rp Config'
    property0: EnumProperty(
        items = [('SSGI', 'SSGI', 'SSGI'),
                 ('SSR', 'SSR', 'SSR'),
                 ('Bloom', 'Bloom', 'Bloom'),
                 ('GI', 'GI', 'GI'),
                 ('Motion Blur', 'Motion Blur', 'Motion Blur')
                 ],
        name='', default='SSGI')

    def init(self, context):
        self.add_input('ArmNodeSocketAction', 'In')
        self.add_input('NodeSocketBool', 'On')
        self.add_output('ArmNodeSocketAction', 'Out')

    def draw_buttons(self, context, layout):
        layout.prop(self, 'property0')

add_node(RpConfigNode, category=PKG_AS_CATEGORY)