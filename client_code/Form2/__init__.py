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

    # Defining mq.MathQuill and mathtexto
    self.mq = MathQuill.getInterface(2)
    self.mathtexto = self.mq

    # Subscribe to updates
    anvil.server.connect('saved_chat_update', self.update_saved_chat)

    # Load components from the data table initially
    self.load_components_from_table()

  def load_components_from_table(self):
    # Query the data table
    rows = anvil.server.call('get_items')
    # Iterate through the retrieved rows
    for row in rows:
      component_type = row['type']
      content = row['content']
      mathquill_content = row.get('mathquill_content', None)
      user = row['user']
      email = row['email']

      # Create and add the component based on its type
      self.create_component(component_type, content, mathquill_content, user, email)

  def create_component(self, component_type, content, mathquill_content, user, email):
    # Create a label for the user name
    user_label = anvil.Label(text=user, font_size=12, align="center", background='#3ABEF9', spacing_above='none', spacing_below='none', border='solid 1px')
    user_email = anvil.Label(text=email, font_size=12, align="center", background='#3ABEF9', spacing_above='none', spacing_below='none', border='solid 1px')

    # Container to hold user label and the original component
    row_panel = anvil.FlowPanel(background='#A7E6FF', vertical_align='middle', spacing='tiny')

    # Add the user labels to the row panel
    row_panel.add_component(user_label)
    row_panel.add_component(user_email)

    # Add the main content based on its type
    if component_type == 'Label':
      label = anvil.Label(text=content, font_size=12)
      if mathquill_content:
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

  def update_saved_chat(self, message):
    # Clear the current saved_chat panel
    self.saved_chat.clear()
    # Load components from the update message
    for item in message:
      self.create_component(item['type'], item['content'], item.get('mathquill_content', None), item['user'], item['email'])

  def add_math_click(self, **event_args):
    """This method is called when the button is clicked"""
    math_label = anvil.Label(font_size=20)
    self.linear_panel_1.add_component(math_label)
    self.mq.MathField(anvil.js.get_dom_node(math_label)).focus()

  def add_text_click(self, **event_args):
    """This method is called when the button is clicked"""
    text_box = anvil.TextArea(placeholder="write text here", border=0, height=1, auto_expand=True)
    self.linear_panel_1.add_component(text_box)

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

      # Set the component's background color and alignment based on user type
      if user_type == "instructor":
        new_panel.background = '#BBE9FF'  # Light blue background
        component.remove_from_parent()
        component.background = '#BBE9FF'
        component.border = "0px"
        # Adding information to the table
        self.adding_to_table(component, user_type, email)

        new_panel.add_component(component, full_width_row=True)
      else:
        new_panel.background = '#FFFED3'  # Light yellow background
        component.remove_from_parent()
        component.background = '#FFFED3'
        component.border = '0px'
        new_panel.add_component(component, full_width_row=True)

        # Adding the information to the table
        self.adding_to_table(component, user_type, email)

      # Add the new panel to the saved_chat panel
      self.saved_chat.add_component(new_panel)

    # Remove original components from linear_panel_1
    self.linear_panel_1.clear()

  def check_type_of_user(self):
    user = anvil.users.get_user()
    if user and user['role'] == 'instructor':
      return 'instructor'
    else:
      return 'student'

  def extract_component_data(self, component):
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

  def adding_to_table(self, component, user_type, email):
    component_data = self.extract_component_data(component)
    component_data.update({
      'user': user_type,
      'email': email
    })
    anvil.server.call('add_chat_item', component_data)

  def link_1_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form('Form1')

  def link_2_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form('Form2')

  def link_3_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form('Form3')
