from ._anvil_designer import Form2Template
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

class Form2(Form2Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # defining mq.MathQuill and mathtexto, maybe we need to change the words
    self.mq = MathQuill.getInterface(2)
    self.mathtexto=self.mq

    # Any code you write here will run before the form opens.
    

  def add_math_click(self, **event_args):
    """This method is called when the button is clicked"""
    math_label=anvil.Label(font_size=20)
    self.linear_panel_1.add_component(math_label)
    self.mq.MathField(anvil.js.get_dom_node(math_label)).focus()
    pass

  def add_text_click(self, **event_args):
    """This method is called when the button is clicked"""
    text_box = anvil.TextArea(placeholder="write text here",border=0,height=1, auto_expand=True)
    self.linear_panel_1.add_component(text_box)
    pass

  def send_click(self, **event_args):
    """This method is called when the button is clicked"""
    copia = self.linear_panel_1.get_components()
    pass

  def link_1_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form('Form1')
    pass




