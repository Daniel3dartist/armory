from arm.logicnode.arm_nodes import *


class FunctionNode(ArmLogicTreeNode):
    """Function node"""
    bl_idname = 'LNFunctionNode'
    bl_label = 'Function'
    arm_version = 1
    min_outputs = 1

    def __init__(self):
        array_nodes[str(id(self))] = self

    def init(self, context):
        super(FunctionNode, self).init(context)
        self.add_output('ArmNodeSocketAction', 'Out')

    function_name: StringProperty(name="Name")

    def draw_buttons(self, context, layout):
        row = layout.row(align=True)
        row.prop(self, 'function_name')
        row = layout.row(align=True)
        op = row.operator('arm.node_add_output', text='Add Arg', icon='PLUS', emboss=True)
        op.node_index = str(id(self))
        op.socket_type = 'NodeSocketShader'
        op.name_format = "Arg {0}"
        op.index_name_offset = 0
        op2 = row.operator('arm.node_remove_output', text='', icon='X', emboss=True)
        op2.node_index = str(id(self))


add_node(FunctionNode, category=PKG_AS_CATEGORY, section='function')
