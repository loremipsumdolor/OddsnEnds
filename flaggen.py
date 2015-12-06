##########
# Hexa-flag Generator
# Generate SVG flags based on hexadecimal strings
# Jacob Turner
# Released under the MIT license
##########

def main(colorstring, filename, w, h):
    w = str(w * 150)
    h = str(h * 150)
    colors_all = [colorstring[i:i + 6] for i in range(0, len(colorstring), \
                  6)]
    colors = [color for color in colors_all if len(color) == 6]
    line_width = str(int(w) / len(colors))
    x = 0
    with open(filename, "w") as flag:
        flag.write('<svg xmlns="http://www.w3.org/2000/svg" width="%s" height="%s">' % (w, h))
        for color in colors:
            if color == colors[0]:
                flag.write('<rect fill="#' + color + '" width="' + \
                line_width + '" height="' + h + '" />\n')
            else:
                flag.write('<rect fill="#' + color + '" width="' + \
                line_width + '" height="' + h + '" x="' + str(x) + '" />\n')
            x += int(line_width)
        flag.write('</svg>')
    if colors != colors_all:
        print "NOT USED: " + str(list(set(colors_all) - set(colors)))

if __name__ == "__main__":
    colorstring_input = raw_input("Input your hex color string here: ")
    filename_input = raw_input("Input the filename (include .svg): ")
    width_input = raw_input("Input the width in inches: ")
    height_input = raw_input("Input the height in inches: ")
    main(colorstring_input, filename_input, width_input, height_input)
