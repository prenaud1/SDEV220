"""
does_grade_qualify.py
by Paul Renaud
March 22, 2025
for IvyTech SDEV220

Asks for last namne, first name, and GPA.
Shows if student has made Honor Roll
or Dean's List.
Variables deans_list_minimum and
honor_roll_minimum can be changed as needed.
"""

print("Does Grade Qualify?")
print("This will determine if a student is")
print("eligible for the Honor Roll or Dean's")
print("list.")
deans_list_minimum = 3.5
honor_roll_minimum = 3.25
while True:
	lname = input("\nEnter student's last name [ZZZ to quit]:")
	if lname.upper() == "ZZZ":
		break
	fname = input("Enter student's first name:")
	gpa = float(input("Enter student's GPA:"))
	if gpa >= deans_list_minimum:
		print(fname, lname, "has made the Dean's List.")
	elif gpa >= honor_roll_minimum:
		print(fname, lname, "has made the Honor Roll.")
	else:
		print(fname, lname, "is probably a fine student.")
print("Done.")
