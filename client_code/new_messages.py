import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
# This is a module.
# You can define variables and functions here, and use them from any form. For example, in a top-level form:
#
#    from . import Module1
#
#    Module1.say_hello()
#

# 1. I need to query the Users table about the date and time of last login of the user
# 2. Then I need to see if there are entries in the chat table that are newer than the last login
# 3. I need to save those entries in a dict to further use them

def new_messages_since_last_user_login():
  print("Hello, world")
