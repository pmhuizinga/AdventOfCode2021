with open('data/color_palettes_in_R.txt') as f:
    content = f.readlines()

data = [c.strip('\n').strip('\t') for c in content]

colordict = {}
for palette in data:
    colorlist=[]
    palette_name = palette.split(' = ')[0]
    rest = palette.split(' = ')[1].split(',')
    for color in rest:
        if '#' in color:
            loc = 0
            for char in color:
                if char == '#':
                    colorlist.append(color[loc:loc+7])
                loc += 1
    colordict[palette_name] = colorlist
