import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
import time
import anvil.email

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

# 1. I need to query the Users table about the date and time of last login of the user
# 2. Then I need to see if there are entries in the chat table that are newer than the last login
# 3. I need to save those entries in a dict to further use them
# 4. I want to receive an email every time a new message arrived

@anvil.server.callable
def send_email():
  anvil.email.send(to="esteban.diaz@uta.edu",from_address='anvil_support',subject='new chat messages')
  pass