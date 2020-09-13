from arm.logicnode.arm_nodes import *

class VolumeTriggerNode(ArmLogicTreeNode):
    """Volume trigger node"""
    bl_idname = 'LNVolumeTriggerNode'
    bl_label = 'Volume Trigger'
    arm_version = 1
    property0: EnumProperty(
        items = [('Enter', 'Enter', 'Enter'),
                 ('Leave', 'Leave', 'Leave'),
                 ('Overlap', 'Overlap', 'Overlap')],
        name='', default='Enter')

    def init(self, context):
        super(VolumeTriggerNode, self).init(context)
        self.add_input('ArmNodeSocketObject', 'Object')
        self.add_input('ArmNodeSocketObject', 'Volume', default_value='Volume')
        self.add_output('NodeSocketBool', 'Bool')

    def draw_buttons(self, context, layout):
        layout.prop(self, 'property0')

add_node(VolumeTriggerNode, category=PKG_AS_CATEGORY, section='misc')
