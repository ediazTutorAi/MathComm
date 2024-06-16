from ._anvil_designer import ItemTemplate1Template
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.js
from anvil.js.window import MathQuill

class ItemTemplate1(ItemTemplate1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    
    # this line calls the items from Form1, nice.
    self.label_1.text = self.item

    # Any code you write here will run when the form opens.
    self.mq = MathQuill.getInterface(2)
    self.mathtexto=self.mq
    mathtext = anvil.js.get_dom_node(self.label_1)
    self.mathtexto = self.mq.StaticMath(mathtext)