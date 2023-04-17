from ._anvil_designer import Form1Template
from anvil import *
import anvil.server

class Form1(Form1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
  
    # Any code you write here will run before the form opens.


  def get_tree_image(self, **event_args):
    """This method is called when the button is clicked"""
    # Llamar a la función `plot_trees()` para generar la imagen
    tree_image = anvil.server.call('plot_trees')
    self.lexical_analyzer_label.text = anvil.server.call('lexical_analyzer')
    # Mostrar la imagen en el componente de imagen
    self.image_tree.source = tree_image

    

    
    


