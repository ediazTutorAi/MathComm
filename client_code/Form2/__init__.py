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

  # This function receives the command to copy the information in the column panel, so it is saved
  # 
  def send_click(self, **event_args):
    """This method is called when the button is clicked"""
    # Get the user type
    user_type = self.check_type_of_user()
    # Copy components from linear_panel_1
    components = self.linear_panel_1.get_components()
    
    for component in components:
      # Create a new column panel for the component
      new_panel = anvil.ColumnPanel()

      # Set the component's background color and alignment based on user type
      if user_type == "instructor":
        new_panel.background = '#BBE9FF' # Light blue background
        component.remove_from_parent()
        component.background = '#BBE9FF'
        component.border = "0px"

        component_data = self.extract_component_data(component)
        if isinstance(component, Label):
          app_tables.chat.add_row(
            type=component_data['type'],
            content=component_data['content'],
            mathquill_content=component_data['mathquill_content']
          )
          
        new_panel.add_component(component,full_width_row=True)
        # We need to find a way to align it right
      else:
        new_panel.background = '#FFFED3' # Light blue background
        component.remove_from_parent()
        component.background = '#FFFED3'
        component.border = '0px'
        new_panel.add_component(component,full_width_row=True)
        # Align left by default

      # Add the new panel to the saved_chat panel
      self.saved_chat.add_component(new_panel)
      #component.remove_from_parent()
      #self.saved_chat.add_component(component)

    # Remove original components from linear_panel_1
    self.linear_panel_1.clear()
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
      mathquill_content = component.MathQuill.latext()
      return {
        'type': 'Label',
        'content': component.text,
        'mathquill_content': mathquill_content
      }
  
  def link_1_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form('Form3')
    pass




