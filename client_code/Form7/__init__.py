from ._anvil_designer import Form7Template
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.js
from anvil.js.window import MathQuill
from anvil.js.window import jQuery

class Form7(Form7Template):
  list_of_inputs = []
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    # Any code you write here will run before the form opens.
    self.mq = MathQuill.getInterface(2) #this will create the mathquill interface for dynamic and statics mathematics
    self.variatita=self.mq # I don't think this is a good python set up of a reusable variable but it works so far, I don't think we need it

  ### Just the navigation panel
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
    
  ### End of navigation panels

  ### Here is where the form shows
  def form_show(self, **event_args):
    # we are going to have to create a function that gives different problems
    problem = anvil.js.get_dom_node(self.num_problem)
    problem_math = self.mq.StaticMath(problem)
    idea_3 = anvil.js.get_dom_node(self.label_3)
    idea_3_math = self.mq.MathField(idea_3)
  pass
  ### we end up the form

  ### Here we defined the logic for showing the box that ask for ideas and then the math box where the student write down the ideas
  
  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    math_equation = self.mq(anvil.js.get_dom_node(self.label_3)).latex()
    answer_from_chatgpt = anvil.server.call("check_math", math_equation)
    # will create the holder for the gpt answer and add it to linear panel 2
    lbl = Label(border="solid 1px", text="",font_size=16,align="left")
    self.linear_panel_2.add_component(lbl)
    
    # add the answer from chat gpt
    lbl.text=answer_from_chatgpt
    pass
    
  def button_3_click(self, **event_args):
    """This method is called when the button is clicked"""
    math_phrase = self.text_box_1.text
    math_mensaje = self.mq(anvil.js.get_dom_node(self.label_3)).latex()
    answer_from_chatgpt = anvil.server.call("check_idea", math_phrase)
    # will create the holder for the gpt answer and add it to linear panel 2
    lbl = Label(border="solid 1px", text="",font_size=16,align="left")
    self.linear_panel_2.add_component(lbl)
    # add the answer from chat gpt
    lbl.text=answer_from_chatgpt
    pass

  # when the next button is clicked we need to add a new text and a new line for the equations
  def button_2_click(self, **event_args):
    """This method is called when the button is clicked"""
    # we need to call a subroutine that adds the next text line and the next math line
    self.write_new_text_and_math()
    pass
    
  def button_4_click(self, **event_args):
    """This method is called when the button is clicked"""
        # find the textboxes in the linear panels
    linear_panel = self.linear_panel_2
    # Get all textbox and mathbox components in the linerar panel
    textboxes = self.find_textboxes_in_contatiner(linear_panel)
    mathboxes = self.find_non_textboxes_in_container(linear_panel)
    for textbox, mathbox in zip(textboxes, mathboxes):
      # change the color and set enabled to false so the user cannot write in that textbox anymore
      textbox.background = "#eeeeee"
      textbox.enabled = False
      # we need to get the latex from the math boxes
      mate = self.mq(anvil.js.get_dom_node(mathbox)).latex()
      # here we are printing to the console, but it is not necessary, we could actually send this information to chatgpt if need it.
      print(f"{textbox.text},{mate};")
    pass

  
  def write_new_text_and_math(self):
    # creating the new text component
    txtbox = TextBox(align="left",border="solid 1px")
    self.linear_panel_2.add_component(txtbox)
    
    #creating and adding the new math component
    lbl_m = Label(align="center",font_size=20, border="solid 1px")
    self.linear_panel_2.add_component(lbl_m)
    nodo = anvil.js.get_dom_node(lbl_m)
    self.mq.MathField(nodo)
    
    pass

  # this functions really gets the textbox containers and their text within.
  def find_textboxes_in_contatiner(self, container):
    textboxes=[]
    for component in container.get_components():
      if isinstance(component,TextBox):
        textboxes.append(component)
      if isinstance(component,Container):
        textboxes.extend(find_textboxes_in_container(component))
    return textboxes
    
  # This function gets the math containers
  def find_non_textboxes_in_container(self, container):
    mathboxes = []
    for component in container.get_components():
      if not isinstance(component, TextBox):
        mathboxes.append(component)
      if isinstance(component, Container):
        mathboxes.extend(self.find_non_textboxes_in_container(component))
    return mathboxes






### This is snipt to remeber some ideas in case i need them.
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

 

 



    

