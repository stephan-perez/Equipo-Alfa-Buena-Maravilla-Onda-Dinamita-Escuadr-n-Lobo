import dearpygui.dearpygui as dpg

# PRIMERO CREAR UN CONTEXTO

dpg.create_context()

# FUNCION PARA PERSONALIZAR
# tag LE DA COMO UN NOMBRE QUE PUEDES LLAMAR PARA EDITAR

with dpg.window(tag="Primary Window"):
    # CREA UN TEZTO CULIAO
    dpg.add_text("Hello, world")
    # CREA UN BOTON SIN FUNCION
    dpg.add_button(label="Save")
    # CREA UNA CAJA DE TEXTO
    dpg.add_input_text(label="string", default_value="Quick brown fox")
    # CREA UNA BARRA
    dpg.add_slider_float(label="float", default_value=0.273, max_value=1, tag="f")
    # CREA UN BOTON
    b0 = dpg.add_button(label="Deja ciego a alguien en el mundo")
    b1 = dpg.add_button(label="Le devuelve la vista a un ciego en el mundo")  
    # EL COMDANDO set_item LE DA PROPIEDADES A LOS OBJETOS
    dpg.set_value("f", 0.666)
    dpg.set_item_width(b0, 250)
    dpg.set_item_height(b0, 200)  
    dpg.set_item_height(b1, 200)

print(b0)
print(b1)

# LA VENTANA

dpg.create_viewport(title='Custom Title', width=1080, height=720)

# SIEMPRE COLOCAR LO SIGUIENTE

dpg.setup_dearpygui()
dpg.show_viewport()
dpg.set_primary_window("Primary Window", True)
dpg.start_dearpygui()

# TERMINA EL CONTEXTO

dpg.destroy_context()
