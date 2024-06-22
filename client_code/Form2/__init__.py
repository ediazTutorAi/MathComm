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
    self.load_components_from_tabe()
    

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
        # Adding information to the table
        self.adding_to_table(component,user_type)

        new_panel.add_component(component,full_width_row=True)
        # We need to find a way to align it right
      else:
        new_panel.background = '#FFFED3' # Light blue background
        component.remove_from_parent()
        component.background = '#FFFED3'
        component.border = '0px'
        new_panel.add_component(component,full_width_row=True)

        # Adding the information to the tabl
        self.adding_to_table(component,user_type)
        
      # Add the new panel to the saved_chat panel
      self.saved_chat.add_component(new_panel)
      
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
  def adding_to_table(self,component,user_type):
    component_data = self.extract_component_data(component)
    if isinstance(component, Label):
      app_tables.chat.add_row(
        type=component_data['type'],
        content=component_data['content'],
        mathquill_content=component_data['mathquill_content'],
        user=user_type
      )
    elif isinstance(component,anvil.TextArea):
      app_tables.chat.add_row(
        type=component_data['type'],
        content=component_data['content'],
        user=user_type
      )
    elif isinstance(component,anvil.TextBox):
      app_tables.chat.add_row(
        type=component_data['type'],
        content=component_data['content'],
        user=user_type
      )
  
  def link_1_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form('Form3')
    pass
    
  # I need to parse the saved data from the dataTable into the colum panel and
  # output all the information.
  # 1) search the chat data table.
  # 2) Filter for Label that contains MathQuill.
  # 3) Filter for TextArea and TextBoxes.
  # 4) I want to put the name of the user, like user_name wrote this or something like that
  # 5) Then I want to resuse the column panel to put all this information back in their 
  # 6) respective components
  def load_components_from_tabe(self):
    # Query the data table
    rows = app_tables.chat.search()
    # Iterate through the retrieved rows
    for row in rows:
      component_type = row['type']
      content = row['content']
      mathquill_content = row['mathquill_content']
      user = row['user']

      # Create and add the component based on its type
      self.create_component(component_type,content,mathquill_content,user)

  def create_component(self,component_type,content,mathquill_content,user):
    if component_type == 'Label':
      label = anvil.Label(text=content,font_size=12)
      if mathquill_content:
        # Add mathquill content as StaticMath because we don't want to edit it.
        mathquill_field = self.mq.StaticMath(anvil.js.get_dom_node(label))
        mathquill_field.latex(mathquill_content)

      self.saved_chat.add_component(label)
    elif component_type == 'TextArea':
      text_area = anvil.TextArea(text=content, border=0, height=1, auto_expand=True)
      self.linear_panel_1.add_component(text_area)
  



