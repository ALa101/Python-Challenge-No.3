"""
        5.length name
Ask the user to enter their
 first name and then ask them toenter their surname.
  Join them together with a space betweenand
  display the name and the length of whole name.

"""
fname = input("Enter the First name :")
lname = input("Enter the surname :")
name = " ".join([fname,lname])
print("\tJoin names Use Join fun ->"+name)
name = fname + " " + lname
print("\tJoin names Use + operator  ->"+name)
name = ("%s %s" %(fname ,lname))
print("\tJoin names Use % operator  ->"+name)
name = "{} {}".format(fname,lname)
print("\tJoin names Use format()  ->"+name)

print("\tthe length of name is : (" + str(len(name)) + ")")