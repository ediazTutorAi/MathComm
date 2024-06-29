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
    self.load_components_from_table()
    

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

  # This function receives the command to copy the information in the column panel, so it is saved
  # 
  def send_click(self, **event_args):
    """This method is called when the button is clicked"""
    # Get the user type
    user_type = self.check_type_of_user()
    email = anvil.users.get_user()['email'].split('@')[0]
    # Copy components from linear_panel_1
    components = self.linear_panel_1.get_components()
    
    for component in components:
      # Create a new column panel for the component
      new_panel = anvil.ColumnPanel()
      component.remove_from_parent()
      component.border = "0px"
      # Adding information to the table
      self.adding_to_table(component,user_type,email)
      new_panel.add_component(component,full_width_row=True)
      # Add the new panel to the saved_chat panel
      self.saved_chat.add_component(new_panel)      
    # Remove original components from linear_panel_1
    self.linear_panel_1.clear()
    self.load_components_from_table()
    self.send.scroll_into_view(smooth=True)
    pass

  # this function check the type of user, in this case, it assumes that if is not instructor, it is student
  def check_type_of_user(self):
    user = anvil.users.get_user()
    if user and user['role']=='instructor':
      return 'instructor'
    else:
      return 'student'
    pass   
    
  def extract_component_data(self,component):
    if isinstance(component, anvil.Label):
      mathquill_content = self.mq.MathField(anvil.js.get_dom_node(component)).latex()
      return {
        'type': 'Label',
        'content': component.text,
        'mathquill_content': mathquill_content
      }
    elif isinstance(component, anvil.TextArea):
      return {
        'type': 'TextArea',
        'content': component.text,
      }
    elif isinstance(component, anvil.TextBox):
      return {
        'type': 'TextBox',
        'content': component.text,
      }
  def adding_to_table(self,component,user_type,email):
    component_data = self.extract_component_data(component)
    if isinstance(component, Label):
      app_tables.chat.add_row(
        type=component_data['type'],
        content=component_data['content'],
        mathquill_content=component_data['mathquill_content'],
        user=user_type,
        email=email
      )
    elif isinstance(component,anvil.TextArea):
      app_tables.chat.add_row(
        type=component_data['type'],
        content=component_data['content'],
        user=user_type,
        email=email
      )
    elif isinstance(component,anvil.TextBox):
      app_tables.chat.add_row(
        type=component_data['type'],
        content=component_data['content'],
        user=user_type,
        email=email
      )
  
  def link_1_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form('Form1')
    pass
    

  def load_components_from_table(self):
    #clean the column panel first
    self.saved_chat.clear()
    # Query the data table
    rows = app_tables.chat.search()
    # Iterate through the retrieved rows
    for row in rows:
      component_type = row['type']
      content = row['content']
      mathquill_content = row['mathquill_content']
      user = row['user']
      email = row['email']

      # Create and add the component based on its type
      self.create_component(component_type,content,mathquill_content,user,email)

  def create_component(self,component_type,content,mathquill_content,user,email):
    if user=='instructor':
      # Create a label for the user name
      user_label = anvil.Label(text=user,font_size=12,align="center",background='#E9C46A',spacing_above='none',spacing_below='none',border='solid 1px')
      user_email = anvil.Label(text=email,font_size=12,align="center",background='#E9C46A',spacing_above='none',spacing_below='none',border='solid 1px')
      #Container to hold user label and the original component
      row_panel = anvil.FlowPanel(background='#A7E6FF',vertical_align='middle',spacing='tiny')
      # Here we are adding the two labels
      row_panel.add_component(user_label)
      row_panel.add_component(user_email)
    elif user == 'student':
      # Create a label for the user name
      user_label = anvil.Label(text=user,font_size=12,align="center",background='#ADD899',spacing_above='none',spacing_below='none',border='solid 1px')
      user_email = anvil.Label(text=email,font_size=12,align="center",background='#ADD899',spacing_above='none',spacing_below='none',border='solid 1px')
      #Container to hold user label and the original component
      row_panel = anvil.FlowPanel(background='#D8EFD3',vertical_align='middle',spacing='tiny')
      # Here we are adding the two labels
      row_panel.add_component(user_label)
      row_panel.add_component(user_email)

    # going through the components
    if component_type == 'Label':
      label = anvil.Label(text=content,font_size=12)
      if mathquill_content:
        # Add mathquill content as StaticMath because we don't want to edit it.
        mathquill_field = self.mq.StaticMath(anvil.js.get_dom_node(label))
        mathquill_field.latex(mathquill_content)

      row_panel.add_component(label)
      
    elif component_type == 'TextArea':
      text_area = anvil.Label(text=content, border='0px', font_size=12)
      row_panel.add_component(text_area)
    elif component_type == 'TextBox':
      text_box = anvil.Label(text=content, border='0px', font_size=12)
      row_panel.add_component(text_box)

    self.saved_chat.add_component(row_panel)

  def link_2_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form('Form2')
    pass

  def link_3_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form('Form3')
    pass

  def form_show(self, **event_args):
    """This method is called when the form is shown on the page"""
    # The next code needs to be change for better readability
    labelSum=anvil.Label(text="\\sum")
    mathquill1=self.mq.StaticMath(anvil.js.get_dom_node(labelSum))
    mathquill1.latex(labelSum.text)
    self.rt_1.add_component(labelSum,slot="label_1")
    # Next slot
    labelInt=anvil.Label(text="\\int")
    mathquill2=self.mq.StaticMath(anvil.js.get_dom_node(labelInt))
    mathquill2.latex(labelInt.text)
    self.rt_1.add_component(labelInt,slot="label_2")
    # Next slot
    labelSqrt=anvil.Label(text="\\sqrt{}")
    mathquill3=self.mq.StaticMath(anvil.js.get_dom_node(labelSqrt))
    mathquill3.latex(labelSqrt.text)
    self.rt_1.add_component(labelSqrt,slot="label_3")
    # Next slot
    labelInfty=anvil.Label(text="\\infty")
    mathquill4=self.mq.StaticMath(anvil.js.get_dom_node(labelInfty))
    mathquill4.latex(labelInfty.text)
    self.rt_1.add_component(labelInfty,slot="label_4")
    # Next slot
    labelPower=anvil.Label(text="k^6")
    mathquill5=self.mq.StaticMath(anvil.js.get_dom_node(labelPower))
    mathquill5.latex(labelPower.text)
    self.rt_1.add_component(labelPower,slot="label_5")
    #Next slot
    labelFrac=anvil.Label(text="\\frac{1}{k}")
    mathquill6=self.mq.StaticMath(anvil.js.get_dom_node(labelFrac))
    mathquill6.latex(labelFrac.text)
    self.rt_1.add_component(labelFrac,slot="label_6")

    #Scrolling smooth
    self.send.scroll_into_view(smooth=True)
    
    pass




