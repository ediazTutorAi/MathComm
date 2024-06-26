import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server

# This is a server module. It runs on the Anvil server,
# rather than in the user's browser.
#
# To allow anvil.server.call() to call functions here, we mark
# them with @anvil.server.callable.
# Here is an example - you can replace it with your own:
#
# @anvil.server.callable
# def say_hello(name):
#   print("Hello, " + name + "!")
#   return 42
#
import anvil.server
from anvil import app_tables

@anvil.server.callable
def get_items():
    return app_tables.chat.search()
    

@anvil.server.callable
def push_update():
    items = list(app_tables.chat.search())
    anvil.server.publish('saved_chat_update', items)

@anvil.server.callable
def add_chat_item(component_data):
    app_tables.chat.add_row(**component_data)
    push_update()  # Push update after adding a new item
