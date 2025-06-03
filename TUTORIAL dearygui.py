import dearpygui.dearpygui as dpg

# PRIMERO CREAR UN CONTEXTO

dpg.create_context()

# FUNCION PARA PERSONALIZAR

with dpg.window(label="Prueba"):
    # CREA UN TEZTO CULIAO
    dpg.add_text("Hello, world")
    # CREA UN BOTON SIN FUNCION
    dpg.add_button(label="Save")
    # CREA UNA CAJA DE TEXTO
    dpg.add_input_text(label="string", default_value="Quick brown fox")
    # CREA UNA BARRA
    dpg.add_slider_float(label="float", default_value=0.273, max_value=1)

# LA VENTANA

dpg.create_viewport(title='Custom Title', width=1080, height=720)

# SIEMPRE COLOCAR LO SIGUIENTE

dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()

# TERMINA EL CONTEXTO

dpg.destroy_context()
