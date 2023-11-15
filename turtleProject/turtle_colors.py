import colorgram
colors=colorgram.extract("CS139_1_771_0.jpg",30)
#print(colors)
# first_color=colors[0] #access first colour in the list
# print(first_color.rgb) # printing in rgb format
# print(first_color.rgb.r) # accessing r value
color_list=[]
for color in colors:
    r=color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color=(r,g,b)
    color_list.append(new_color) # storing r,g,b values as tuple in  a list
print(color_list)
