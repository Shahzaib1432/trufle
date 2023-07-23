from functools import lru_cache

class Rainbow:
    def __init__(self,
                 gradients = None,
                 minNum = 0,
                 maxNum = 100,
                 colours = ['ff0000', '0000ff']):
        self.gradients = gradients
        self.minNum = minNum
        self.maxNum = maxNum
        self.colours = colours
        self.set_colours(self.colours)

    def set_colours(self, spectrum):
        if len(spectrum) < 2:
            raise ValueError('Rainbow must have two or more colours.')
        else:
            increment = (self.maxNum - self.minNum) / (len(spectrum) - 1)
            first_gradient = ColourGradient()
            first_gradient.set_gradient(spectrum[0], spectrum[1])
            first_gradient.set_number_range(self.minNum, self.minNum + increment)
            self.gradients = [first_gradient]

            for i in range(1, len(spectrum) - 1):
                colour_gradient = ColourGradient()
                colour_gradient.set_gradient(spectrum[i], spectrum[i + 1])
                colour_gradient.set_number_range(self.minNum + increment * i, self.minNum + increment * (i + 1))
                self.gradients.append(colour_gradient)

            self.colours = spectrum

    def set_spectrum(self, *args):
        self.set_colours(args)

    def set_spectrum_by_array(self, array):
        self.set_colours(array)

    @lru_cache(10)
    def colour_at(self, number):
        if not isinstance(number, (int, float)):
            raise TypeError(str(number) + ' is not a number')
        elif len(self.gradients) == 1:
            return self.gradients[0].colour_at(number)
        else:
            segment = (self.maxNum - self.minNum) / (len(self.gradients))
            index = min(int((max(number, self.minNum) - self.minNum) / segment), len(self.gradients) - 1)
            return self.gradients[index].colour_at(number)

    def color_at(self, number):
        return self.colour_at(number)

    def set_number_range(self, min_number, max_number):
        if max_number > min_number:
            self.minNum = min_number
            self.maxNum = max_number
            self.set_colours(self.colours)
        else:
            raise ValueError('max_number (' + str(max_number) + ') is not greater than min_number (' + str(min_number) + ')')


class ColourGradient:
    def __init__(self):
        self.start_colour = 'ff0000'
        self.end_colour = '0000ff'
        self.minNum = 0
        self.maxNum = 100

    def set_gradient(self, colour_start, colour_end):
        self.start_colour = self.get_hex_colour(colour_start)
        self.end_colour = self.get_hex_colour(colour_end)

    def set_number_range(self, min_number, max_number):
        if max_number > min_number:
            self.minNum = min_number
            self.maxNum = max_number
        else:
            raise ValueError('max_number (' + str(max_number) + ') is not greater than min_number (' + str(min_number) + ')')

    def colour_at(self, number):
        return (self.calc_hex(number, self.start_colour[0:2], self.end_colour[0:2])
                + self.calc_hex(number, self.start_colour[2:4], self.end_colour[2:4])
                + self.calc_hex(number, self.start_colour[4:6], self.end_colour[4:6]))

    def calc_hex(self, number, channel_start_base16, channel_end_base16):
        num = min(max(number, self.minNum), self.maxNum)
        num_range = self.maxNum - self.minNum
        c_start_base10 = int(channel_start_base16, 16)
        c_end_base10 = int(channel_end_base16, 16)
        c_per_unit = (c_end_base10 - c_start_base10) / num_range
        c_base10 = round(c_per_unit * (num - self.minNum) + c_start_base10)
        return ColourGradient.format_hex(hex(c_base10)[2:])

    @staticmethod
    def format_hex(hex_str):
        return '0' + hex_str if len(hex_str) == 1 else hex_str

    @staticmethod
    def is_hex_colour(string):
        return len(string) == 6 and all(c in '0123456789ABCDEF' for c in string.upper())

    @staticmethod
    def get_hex_colour(string):
        if ColourGradient.is_hex_colour(string):
            return string[-6:]
        else:
            name = string.lower()
            colour_names = {
                'aliceblue': "F0F8FF", 'antiquewhite': "FAEBD7", 'aqua': "00FFFF", 'aquamarine': "7FFFD4",
                'azure': "F0FFFF", 'beige': "F5F5DC", 'bisque': "FFE4C4", 'black': "000000", 'blanchedalmond': "FFEBCD",
                'blue': "0000FF", 'blueviolet': "8A2BE2", 'brown': "A52A2A", 'burlywood': "DEB887",
                'cadetblue': "5F9EA0", 'chartreuse': "7FFF00", 'chocolate': "D2691E", 'coral': "FF7F50",
                'cornflowerblue': "6495ED", 'cornsilk': "FFF8DC", 'crimson': "DC143C", 'cyan': "00FFFF",
                'darkblue': "00008B", 'darkcyan': "008B8B", 'darkgoldenrod': "B8860B", 'darkgray': "A9A9A9",
                'darkgreen': "006400", 'darkgrey': "A9A9A9", 'darkkhaki': "BDB76B", 'darkmagenta': "8B008B",
                'darkolivegreen': "556B2F", 'darkorange': "FF8C00", 'darkorchid': "9932CC", 'darkred': "8B0000",
                'darksalmon': "E9967A", 'darkseagreen': "8FBC8F", 'darkslateblue': "483D8B",
                'darkslategray': "2F4F4F", 'darkslategrey': "2F4F4F", 'darkturquoise': "00CED1",
                'darkviolet': "9400D3", 'deeppink': "FF1493", 'deepskyblue': "00BFFF", 'dimgray': "696969",
                'dimgrey': "696969", 'dodgerblue': "1E90FF", 'firebrick': "B22222", 'floralwhite': "FFFAF0",
                'forestgreen': "228B22", 'fuchsia': "FF00FF", 'gainsboro': "DCDCDC", 'ghostwhite': "F8F8FF",
                'gold': "FFD700", 'goldenrod': "DAA520", 'gray': "808080", 'green': "008000",
                'greenyellow': "ADFF2F", 'grey': "808080", 'honeydew': "F0FFF0", 'hotpink': "FF69B4",
                'indianred': "CD5C5C", 'indigo': "4B0082", 'ivory': "FFFFF0", 'khaki': "F0E68C",
                'lavender': "E6E6FA", 'lavenderblush': "FFF0F5", 'lawngreen': "7CFC00", 'lemonchiffon': "FFFACD",
                'lightblue': "ADD8E6", 'lightcoral': "F08080", 'lightcyan': "E0FFFF",
                'lightgoldenrodyellow': "FAFAD2", 'lightgray': "D3D3D3", 'lightgreen': "90EE90",
                'lightgrey': "D3D3D3", 'lightpink': "FFB6C1", 'lightsalmon': "FFA07A",
                'lightseagreen': "20B2AA", 'lightskyblue': "87CEFA", 'lightslategray': "778899",
                'lightslategrey': "778899", 'lightsteelblue': "B0C4DE", 'lightyellow': "FFFFE0",
                'lime': "00FF00", 'limegreen': "32CD32", 'linen': "FAF0E6", 'magenta': "FF00FF",
                'maroon': "800000", 'mediumaquamarine': "66CDAA", 'mediumblue': "0000CD",
                'mediumorchid': "BA55D3", 'mediumpurple': "9370DB", 'mediumseagreen': "3CB371",
                'mediumslateblue': "7B68EE", 'mediumspringgreen': "00FA9A", 'mediumturquoise': "48D1CC",
                'mediumvioletred': "C71585", 'midnightblue': "191970", 'mintcream': "F5FFFA",
                'mistyrose': "FFE4E1", 'moccasin': "FFE4B5", 'navajowhite': "FFDEAD",
                'navy': "000080", 'oldlace': "FDF5E6", 'olive': "808000", 'olivedrab': "6B8E23",
                'orange': "FFA500", 'orangered': "FF4500", 'orchid': "DA70D6",
                'palegoldenrod': "EEE8AA", 'palegreen': "98FB98", 'paleturquoise': "AFEEEE",
                'palevioletred': "DB7093", 'papayawhip': "FFEFD5", 'peachpuff': "FFDAB9",
                'peru': "CD853F", 'pink': "FFC0CB", 'plum': "DDA0DD", 'powderblue': "B0E0E6",
                'purple': "800080", 'red': "FF0000", 'rosybrown': "BC8F8F", 'royalblue': "4169E1",
                'saddlebrown': "8B4513", 'salmon': "FA8072", 'sandybrown': "F4A460",
                'seagreen': "2E8B57", 'seashell': "FFF5EE", 'sienna': "A0522D", 'silver': "C0C0C0",
                'skyblue': "87CEEB", 'slateblue': "6A5ACD", 'slategray': "708090",
                'slategrey': "708090", 'snow': "FFFAFA", 'springgreen': "00FF7F",
                'steelblue': "4682B4", 'tan': "D2B48C", 'teal': "008080", 'thistle': "D8BFD8",
                'tomato': "FF6347", 'turquoise': "40E0D0", 'violet': "EE82EE", 'wheat': "F5DEB3",
                'white': "FFFFFF", 'whitesmoke': "F5F5F5", 'yellow': "FFFF00",
                'yellowgreen': "9ACD32"
            }
            if name in colour_names:
                return colour_names[name]
            raise ValueError(string + ' is not a valid colour.')


def GenerateGradient(gradient=None, colours = ['#FF0000', '#0000FF'], minVal = 0, maxVal = 100 ):
    for i, color in enumerate(colours): colours[i] = color.removeprefix('#').lower()
    rainbow = Rainbow(gradients=gradient, colours=colours, minNum=minVal, maxNum=maxVal)
    lst = []
    for i in range(minVal, maxVal + 1):
        lst.append(f'#{rainbow.colour_at(i).upper()}')

    return lst

