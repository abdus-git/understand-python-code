#WAP to print color names, if the user enters the first letter of the color
# name (RED, GREEN, YELLOW, BLUE, WHITE , BLACK)
#
# color=(input("Enter first letter of color:"))
# if color in ["R","r"]:
#     print("The color is red")
# elif color in ["G","g"]:
#     print("The color is green")
# elif color in["Y","y"]:
#     print("The color is yellow")
# elif color in ["B","b"]:
#     print("The color is blue")
# elif color in ["BL","bl"]:
#     print("The color is black")
# else:
#     print("The color is not recognized")



color=str(input("Enter first letter of color (hex):"))
if color in ["R","r"]:
    print("The color is red")
    breakpoint()
if color in ["G","g"]:
    print("The color is green")
    breakpoint()
if color in["Y","y"]:
    print("The color is yellow")
    breakpoint()
if color in ["B","b"]:
    print("The color is blue")
    breakpoint()
if color in ["BL","bl"]:
    print("The color is black")
    breakpoint()
else:
    print("The color is not recognized")
