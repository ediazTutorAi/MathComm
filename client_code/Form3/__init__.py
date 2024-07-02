from ._anvil_designer import Form3Template
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.js
from anvil.js.window import MathQuill
from anvil.js.window import jQuery


class Form3(Form3Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    # defining mq.MathQuill and mathtexto, maybe we need to change the words
    self.mq = MathQuill.getInterface(2)
    self.mathtexto=self.mq

    self.write_math()

    # Any code you write here will run before the form opens.
  def write_math(self):
    mathquill_field1 = self.mq.StaticMath(anvil.js.get_dom_node(self.label_2))
    # In order for this to render properly I had to use double \\ in front of the fraction frac command
    # I didn't need to use it in other places, weird.
    mathquill_field1.latex('\sum')
    mathquill_field2 = self.mq.StaticMath(anvil.js.get_dom_node(self.label_4))
    # In order for this to render properly I had to use double \\ in front of the fraction frac command
    # I didn't need to use it in other places, weird.
    mathquill_field2.latex('\infty')
    mathquill_field3 = self.mq.StaticMath(anvil.js.get_dom_node(self.label_6))
    # In order for this to render properly I had to use double \\ in front of the fraction frac command
    # I didn't need to use it in other places, weird.
    mathquill_field3.latex('\int')
    mathquill_field4 = self.mq.StaticMath(anvil.js.get_dom_node(self.label_8))
    # In order for this to render properly I had to use double \\ in front of the fraction frac command
    # I didn't need to use it in other places, weird.
    mathquill_field4.latex('k^6')
    mathquill_field5 = self.mq.StaticMath(anvil.js.get_dom_node(self.label_10))
    # In order for this to render properly I had to use double \\ in front of the fraction frac command
    # I didn't need to use it in other places, weird.
    mathquill_field5.latex('\\sqrt{}')
    mathquill_field6 = self.mq.StaticMath(anvil.js.get_dom_node(self.label_12))
    # In order for this to render properly I had to use double \\ in front of the fraction frac command
    # I didn't need to use it in other places, weird.
    mathquill_field6.latex('\\frac{}{}')
    mathquill_field7 = self.mq.StaticMath(anvil.js.get_dom_node(self.label_14))
    # In order for this to render properly I had to use double \\ in front of the fraction frac command
    # I didn't need to use it in other places, weird.
    mathquill_field7.latex('\\theta')
    
    pass

  def link_1_click(self, **event_args):
    """This method is called when the link is clicked"""
    anvil.open_form('Form1')
    pass

  def link_2_click(self, **event_args):
    """This method is called when the link is clicked"""
    anvil.open_form('Form2')
    pass
