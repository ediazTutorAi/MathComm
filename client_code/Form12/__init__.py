# Importing required Anvil and JS libraries
from ._anvil_designer import Form12Template
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.js
from anvil.js.window import MathQuill
from anvil.js.window import jQuery

class Form12(Form12Template):

    def __init__(self, **properties):
        self.init_components(**properties)

        # Initialize MathQuill
        self.mathquill_input = None
        self.init_mathquill()
        
        # Load initial chat messages
        self.load_messages()
        
    def init_mathquill(self):
        """Initialize MathQuill for LaTeX input."""
        math_field_span = jQuery(self.math_input_box)  # self.math_input_box is a TextArea in Anvil
        MQ = MathQuill.getInterface(2)
        self.mathquill_input = MQ.MathField(math_field_span[0], {
            "spaceBehavesLikeTab": True,
            "handlers": {
                "edit": lambda: self.update_latex()
            }
        })

    def update_latex(self):
        """Update LaTeX in the input box."""
        latex = self.mathquill_input.latex()
        self.math_input_box.text = latex  # Update the TextArea with LaTeX text

    def load_messages(self):
        """Load messages from the database."""
        # Assuming there is a table 'chat_messages' with columns 'user', 'message', and 'is_latex'
        messages = app_tables.chat_messages.search()
        self.repeating_panel_1.items = messages

    def send_button_click(self, **event_args):
        """Send the message when the button is clicked."""
        user = anvil.users.get_user()
        message_text = self.math_input_box.text
        is_latex = self.latex_check_box.checked  # self.latex_check_box is a CheckBox for indicating LaTeX input

        # Save the message to the database
        app_tables.chat_messages.add_row(user=user, message=message_text, is_latex=is_latex)
        
        # Clear the input fields
        self.math_input_box.text = ""
        self.mathquill_input.latex("")
        
        # Reload messages
        self.load_messages()

    def repeating_panel_1_show(self, **event_args):
        """Format messages when the repeating panel is shown."""
        for item in self.repeating_panel_1.items:
            if item['is_latex']:
                # Render LaTeX
                latex_div = jQuery(self.repeating_panel_1.get_components()[0]['content'])
                latex_div.html(f"<span id='latex-{item['id']}'>{item['message']}</span>")
                MQ.StaticMath(latex_div[0])
            else:
                # Render plain text
                self.repeating_panel_1.get_components()[0]['content'].text = item['message']

    def math_input_box_change(self, **event_args):
        """Update MathQuill when the text area changes."""
        self.mathquill_input.latex(self.math_input_box.text)

