from ._anvil_designer import Form1Template
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

class Form1(Form1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    # defining mq.MathQuill and mathtexto, maybe we need to change the words
    self.mq = MathQuill.getInterface(2)
    self.mathtexto=self.mq

    self.write_math()
    # Any code you write here will run before the form opens.
    anvil.users.login_with_form()

  def write_math(self):
    mathquill_field = self.mq.StaticMath(anvil.js.get_dom_node(self.label_4))
    mathquill_field.latex('\sum_{k=1}^{\infty}')
    pass
    
  def link_2_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form('Form2')
    pass

  def link_1_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form('Form1')
    pass
