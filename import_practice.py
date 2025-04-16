"""
import_practice.py
by Paul Renaud
April 16, 2025
IvyTech SDEV220
Module 4, import practice. I could not figure out how to do this in jupyter notebook, so
this is in VS Code.
"""
# 11.1 Create a file called zoo.py.
# In it, define a function called hours() that prints the string 'Open 9-5 daily'.
# Then, use the interactive interpreter to import the zoo module and call its hours() function.
import zoo
zoo.hours()

print()
# 11.2 In the interactive interpreter, import the zoo module as menagerie
# and call its hours() function.
import zoo as menagerie
menagerie.hours()
