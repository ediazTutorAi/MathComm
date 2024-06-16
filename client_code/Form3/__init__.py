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
  list_of_inputs = []
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
    self.mq = MathQuill.getInterface(2)
    self.variatita=self.mq 

  def link_1_click(self, **event_args):
    """This method is called when the link is clicked"""
    self.content_panel.clear()
    open_form('Form1')
    pass

  def link_2_click(self, **event_args):
    """This method is called when the link is clicked"""
    self.content_panel.clear()
    open_form('Form2')
    pass

  def link_3_click(self, **event_args):
    """This method is called when the link is clicked"""
    self.content_panel.clear()
    open_form('Form3')
    pass

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    txtarea=TextArea(background="lightgrey",placeholder="write your ideas",auto_expand="true")
    self.linear_panel_1.add_component(txtarea)
    self.list_of_inputs.append(txtarea)
    pass

  def button_2_click(self, **event_args):
    """This method is called when the button is clicked"""
    lbl = Label(border="1 px", text="",font_size=30,align="center")
    self.linear_panel_1.add_component(lbl)
    textito=anvil.js.get_dom_node(lbl)
    self.variatita = self.mq.MathField(textito)
    # self.list_of_inputs.append()
    pass

  def button_3_click(self, **event_args):
    """This method is called when the button is clicked"""
    # texto = self.linear_panel_1.get_components()[0].text
    # self.label_2.text = anvil.server.call("get_data",texto)
    # self.label_2.text = self.variatita.latex() # this work to get the last math text written
    # self.label_2.text = self.mq(anvil.js.get_dom_node(self.linear_panel_1.get_components()[1])).latex() # uhauuu this work
    self.label_2.text = self.linear_panel_1.get_components()
    pass








