bl_info = {
    "name": "UCX",
    "blender": (2, 80, 0),
    "category": "Object",
    "author": "Mickael Brotons",
    "version": (1, 0, 0),
    "location": "View3D > Object > UCX",
    "description": "Addon pour dupliquer et renommer des objets sélectionnés pour créer les collision UE5.",
}

import bpy

class SimpleDuplicateRenameOperator(bpy.types.Operator):
    bl_idname = "object.simple_duplicate_rename"
    bl_label = "Duplicate and Rename Selected"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        # Récupérer les objets sélectionnés
        selected_objects = bpy.context.selected_objects

        for obj in selected_objects:
            # Dupliquer l'objet
            duplicate_obj = obj.copy()
            duplicate_obj.data = obj.data.copy()
            bpy.context.collection.objects.link(duplicate_obj)

            # Renommer l'objet avec le préfixe "UCX_"
            duplicate_obj.name = "UCX_" + obj.name

        return {'FINISHED'}

def register():
    bpy.utils.register_class(SimpleDuplicateRenameOperator)
    bpy.types.VIEW3D_MT_edit_mesh.append(menu_func)
    bpy.context.window_manager.keyconfigs.addon.keymaps.new(name='Mesh', space_type='EMPTY')
    km = bpy.context.window_manager.keyconfigs.addon.keymaps[-1]
    kmi = km.keymap_items.new('object.simple_duplicate_rename', 'F5', 'PRESS', ctrl=False, shift=False, alt=False)
    kmi.active = True

def unregister():
    bpy.utils.unregister_class(SimpleDuplicateRenameOperator)
    bpy.types.VIEW3D_MT_edit_mesh.remove(menu_func)
    km = bpy.context.window_manager.keyconfigs.addon.keymaps[-1]
    km.keymap_items.remove(km.keymap_items.get('object.simple_duplicate_rename'))

def menu_func(self, context):
    self.layout.operator(SimpleDuplicateRenameOperator.bl_idname)

if __name__ == "__main__":
    register()
