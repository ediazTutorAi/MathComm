from ._anvil_designer import Form9Template
from anvil import *
import plotly.graph_objects as go
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.js
from anvil.js.window import MathQuill
from anvil.js.window import jQuery

class Form9(Form9Template):
  list_of_inputs = []
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    # Any code you write here will run before the form opens.
    self.mq = MathQuill.getInterface(2) #this will create the mathquill interface for dynamic and statics mathematics
    self.variatita=self.mq # I don't think this is a good python set up of a reusable variable but it works so far, I don't think we need it

    #iframe = jQuery("<iframe width='450px' height='300px' style='border: 1px solid #ff0000; border-radius: 4px;', 'showToolBar':false>").attr("src","https://www.geogebra.org/calculator/btqcbjyq?embed")
    #iframe.appendTo(anvil.js.get_dom_node(self.content_panel))

  ### Here is where the form shows
  def form_show(self, **event_args):
    # we are going to have to create a function that gives different problems
    # it seems that we have to write down the problem here
    math_problem = "f(x)=x^2, 0 \leq x \leq 1"
    self.num_problem.text=math_problem
    problem = anvil.js.get_dom_node(self.num_problem)
    problem_math = self.mq.StaticMath(problem)
    idea_3 = anvil.js.get_dom_node(self.label_3)
    idea_3_math = self.mq.MathField(idea_3)

    self.write_down_the_problem()
  pass
  ### we end up the form

  ### Here we define the problem
  def write_down_the_problem(self):
    problem = "Find the volume of the next function when rotating about the x-axis"
    self.label_2.text = problem
    pass
  ###

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
    # Here I will be passing the information to check if the mathematics is correct, if there is a mistake I will put a red
    # color on a label compoment, if everything is correct I will give a green color. The idea is that the student try by itself to understand what went wrong
    # I don't know how to program it, though.
    newmath = self.mq(anvil.js.get_dom_node(mathboxes[-1])).latex()
    oldmath = self.mq(anvil.js.get_dom_node(mathboxes[-2])).latex()
    anvil.server.call("check_with_sympy",oldmath,newmath)
      
    pass


  def write_new_text_and_math(self):
    linear_panel = self.linear_panel_2
    # Get all textbox and mathbox components in the linerar panel
    textboxes = self.find_textboxes_in_contatiner(linear_panel)
    mathboxes = self.find_non_textboxes_in_container(linear_panel)
    #finding the lenght of the textboxes list
    numero_de_cajas = len(textboxes)
    ordinal = self.convert_to_ordinal(numero_de_cajas+1)
    # creating the new text component
    txtbox = TextBox(align="left",border="solid 1px",placeholder=f"Write your {ordinal} step, do now write mathematics here, just the idea")
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

  # Converting a number to ordinal
  def convert_to_ordinal(self, number):
    if 10 < number % 100 < 20:
      ordinal = str(number) + "th"
    else:
      last_digit = number % 10
      if last_digit == 1:
        ordinal = str(number) + "st"
      elif last_digit == 2:
        ordinal = str(number) + "nd"
      elif last_digit == 3:
        ordinal = str(number) + "rd"
      else:
        ordinal = str(number) + "th"
    return ordinal

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







