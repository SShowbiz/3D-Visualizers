import bpy

def print(*datas):
    window=bpy.context.window_manager.windows[0]
    screen = window.screen
    for area in screen.areas:
        if area.type == 'CONSOLE':
            for data in datas:
                bpy.ops.console.scrollback_append(
                    {'window': window, 'screen': screen, 'area': area},
                    text=str(data))