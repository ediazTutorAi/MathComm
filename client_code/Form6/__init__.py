from ._anvil_designer import Form6Template
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.js
from anvil.js.window import MathQuill
from anvil.js.window import jQuery

class Form6(Form6Template):
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

  # def send_to_chat_gpt(self, **event_args):
    # """This method is called when the button is clicked"""
    # texto = self.linear_panel_1.get_components()[0].text
    # self.label_2.text = anvil.server.call("get_data",texto)
    # self.label_2.text = self.variatita.latex() # this work to get the last math text written
    # self.label_2.text = self.mq(anvil.js.get_dom_node(self.linear_panel_1.get_components()[1])).latex() # uhauuu this work
    # self.label_2.text = self.linear_panel_1.get_components()
    # print("hola")
    # mensaje = self.text_area_1.text
    # self.label_2.text = "hola"
    # pass

  def form_show(self, **event_args):
    """This method is called when the HTML panel is shown on the screen"""
    problem = anvil.js.get_dom_node(self.num_problem)
    problem_math = self.mq.StaticMath(problem)
    # set up the dynamic mathematical inputs
    idea_3 = anvil.js.get_dom_node(self.label_3)
    idea_3_math = self.mq.MathField(idea_3)

    idea_4 = anvil.js.get_dom_node(self.label_4)
    idea_4_math = self.mq.MathField(idea_4)

    idea_5 = anvil.js.get_dom_node(self.label_5)
    idea_5_math = self.mq.MathField(idea_5)

    idea_6 = anvil.js.get_dom_node(self.label_6)
    idea_6_math = self.mq.MathField(idea_6)

    idea_7 = anvil.js.get_dom_node(self.label_7)
    idea_7_math = self.mq.MathField(idea_7)

    idea_8 = anvil.js.get_dom_node(self.label_8)
    idea_8_math = self.mq.MathField(idea_8)
    
    pass

  def button_3_click(self, **event_args):
    """This method is called when the button is clicked"""
    mensaje = self.text_box_1.text
    math_mensaje = self.mq(anvil.js.get_dom_node(self.label_3)).latex()
    self.text_box_1.text = anvil.server.call("get_data", mensaje, math_mensaje)
    pass

  def button_4_click(self, **event_args):
    """This method is called when the button is clicked"""
    mensaje = self.text_box_2.text
    self.label_5.text = anvil.server.call("get_data", mensaje)
    pass
