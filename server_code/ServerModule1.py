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
@anvil.tables.on_add('chat')
def notify_clients_on_new_message(table,row):
  anvil.server.call('refresh_chat_for_all_clients')

@anvil.server.callable
def refresh_chat_for_all_clients():
  anvil.server.call_s('refresh_chat_for_all_clients')

