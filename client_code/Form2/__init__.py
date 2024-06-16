from ._anvil_designer import Form2Template
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
import anvil.js
from anvil.tables import app_tables
from anvil.js.window import MathQuill
from anvil.js.window import jQuery

class Form2(Form2Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.counter=0

    # Any code you write here will run before the form opens
    self.mq = MathQuill.getInterface(2)
    self.variatita=self.mq 

  def link_1_click(self, **event_args):
    """This method is called when the link is clicked"""
    # Clear the content panel
    # open the Form2
    open_form('Form1')
    pass

  def link_2_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form('Form2')
    pass

  def form_show(self, **event_args):
    textoestatico = anvil.js.get_dom_node(self.label_3)
    variable = self.mq.StaticMath(textoestatico)
    pass

  def linear_panel_1_show(self, **event_args):
    """This method is called when the linear panel is shown on the screen"""
    pass

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    """Check the index, which should be a global counter. If the index is even insert an equation box at the next odd index"""
    if self.counter%2 == 0:
      lbl = Label(border="solid", text="")
      self.linear_panel_1.add_component(lbl)
      textito=anvil.js.get_dom_node(lbl)
      self.variatita = self.mq.MathField(textito)
      anvil.server.call("get_data",self.counter)
    else:
      textocaja=TextBox(border="solid",placeholder="Give the idea for the next step")
      self.linear_panel_1.add_component(textocaja)
      """ver que item tiene el linear panel"""
      componentes = self.linear_panel_1.get_components()[self.counter-1]
      # self.label_4.text = anvil.server.call("get_data",componentes.text) 
    
    self.counter=self.counter+1
    pass

  def button_2_click(self, **event_args):
    """This method is called when the button is clicked"""
    textocaja=TextBox(border="solid", text="")
    self.linear_panel_1.add_component(textocaja)
    self.label_4.text=self.variatita.latex()
    """app_tables.table_3.add_row(equations=self.variatita.latex(),texto="hola")"""
    pass

  def text_box_1_pressed_enter(self, **event_args):
    """This method is called when the user presses Enter in this text box"""
    pass
    
  def call_api(self,str):
    anvil.server.call("get_data",str)
    pass

  def link_3_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form('Form3')
    pass





  



  


