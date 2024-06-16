from ._anvil_designer import Form10Template
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.js
import re
from anvil.js.window import MathQuill
from anvil.js.window import jQuery

class Form10(Form10Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    
    # defining mq.MathQuill and mathtexto, maybe we need to change the words
    self.mq = MathQuill.getInterface(2)
    self.mathtexto=self.mq

    # Any code you write here will run before the form opens.

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    mensaje = self.text_area_1.text
    self.split_text(mensaje)
    pass

  def split_text(self,message):
    pattern = r'\$\$(.*?)\$\$'
    parts = re.split(pattern, message)

    inside_double_dollars = []
    outside_double_dollars = []

    for i, part in enumerate(parts):
      if i % 2 == 0:
        outside_double_dollars.append(part)
      else:
        inside_double_dollars.append(part)

    for i in range(len(inside_double_dollars)):
      self.flow_panel_3.add_component((anvil.Label(text=outside_double_dollars[i])))

      mathLabel=anvil.Label(text=inside_double_dollars[i])
      self.flow_panel_3.add_component(mathLabel)
      self.mq.StaticMath(anvil.js.get_dom_node(mathLabel))
      

    if len(outside_double_dollars) > len(inside_double_dollars):
      self.flow_panel_3.add_component(anvil.Label(text=outside_double_dollars[-1]))


    pass

  def button_2_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.flow_panel_3.clear()
    pass






  



 


