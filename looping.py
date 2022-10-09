#!/usr/bin/env python3.7
colors = ['GREEN','RED','YELLOW','BLUE']
for color in colors:
    if color == 'GREEN':
        print(f"The color {color} chosen is in the list provided")
        break
else:
        print(f'The color {color}  provided is not in the list')
