from ._anvil_designer import Form1Template
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.js
from anvil.js.window import MathQuill
from anvil.js.window import jQuery

class Form1(Form1Template):
  
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    
    # defining mq.MathQuill and mathtexto, maybe we need to change the words
    self.mq = MathQuill.getInterface(2)
    self.mathtexto=self.mq
    
    # Any code you write here will run when the form opens.
    
    # set the reapeating panel item to string ""
    self.repeating_panel_1.items=['']

  def form_show(self, **event_args):
    """This method is called when the HTML panel is shown on the screen"""
    staticLatex = anvil.js.get_dom_node(self.label_3)
    mathtext = anvil.js.get_dom_node(self.label_5)
    
    # This introduce the problem
    variable = self.mq.StaticMath(staticLatex)
    variable.latex("\int_{a}^{b}x^2 sin(x) dx")
    
    # It only needs a label to be transform into and editable math placeholder
    # since I am going to change mathtexto, I need it to be set as self.mathtexto
    
    self.mathtexto = self.mq.MathField(mathtext)
    self.mathtexto.focus()
    pass

    
  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    
    # by clicking will create a new label component
    # First I need to get the DOM of the latexSpan label...
    #latexSpan_01 = anvil.js.get_dom_node(self.label_6)
    #...in order to call the global variable mathtexto's latex
    #latexSpan_01.textContent = self.mathtexto.latex()
    # now I call StaticMath on latexSpan to transform the latex into mathtyped
    #self.mq.StaticMath(latexSpan_01)

    # I have to create a label and add it to the dom node and then show the content of of the submitted math
    new_row = self.mathtexto.latex()
    l = list(self.repeating_panel_1.items)+[new_row]
    self.repeating_panel_1.items = l
    
    # clean the math input
    self.mathtexto.latex("")
    #bring back the focus onto the math input
    self.mathtexto.focus()

  def link_1_click(self, **event_args):
    """This method is called when the link is clicked"""
    pass

  def link_2_click(self, **event_args):
    """This method is called when the link is clicked"""
    # Clear the content panel
    self.content_panel.clear()
    # open the Form2
    open_form('Form2')
    pass

  def link_3_click(self, **event_args):
    """This method is called when the link is clicked"""
    # Clear the content panel
    self.content_panel.clear()
    #open Form 3
    open_form('Form3')
    pass

  def link_4_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form("Form4")
    pass

  def link_5_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form('Form5')
    pass

  def link_6_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form('Form6')
    pass

  def link_7_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form('Form7')
    pass

  def link_8_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form('Form8')
    pass

  def link_9_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form('Form9')
    pass

  def link_10_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form('Form10')
    pass

  def link_11_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form('Form11')
    pass

  def link_12_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form('Form12')
    pass













    
    

