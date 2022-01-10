"""
Ask the user to enter their favourite colour.
 If they enter “blue”, “BLUE” or “Blue” display the message
 “I like blue too”,
 otherwise display the message
 “I don’t like [colour],
 I prefer blue”.

"""
print(" Enter their Favourite Colour :\r")
favouriteColour = input()

if "blue" == favouriteColour or "BLUE" == favouriteColour or "Blue" == favouriteColour:
    print('I like blue too')
else:
    print("I don’t like [" +favouriteColour +"]\nI prefer blue”.")