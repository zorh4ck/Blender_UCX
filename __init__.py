bl_info = {
    "name": "UCX",
    "blender": (2, 80, 0),
    "category": "Object",
    "author": "Mickael Brotons",
    "version": (1, 0, 0),
    "location": "View3D > Object > UCX",
    "description": "Addon pour dupliquer et renommer des objets sélectionnés pour créer les collision UE5.",
}

if "bpy" in locals():
    import importlib
    if "UCX" in locals():
        importlib.reload(UCX)

else:
    from . import UCX

def register():
    UCX.register()

def unregister():
    UCX.unregister()

if __name__ == "__main__":
    register()
