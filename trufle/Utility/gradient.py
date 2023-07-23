from difflib import get_close_matches
from uuid import uuid4

def findMatch(input_str, values):
    try:
        return get_close_matches(input_str, values, n=1)[0]
    except Exception:
        raise EnvironmentError(f'No matching direction was found.\n{uuid4()}')

def Gradient(colors = ['#FF0000', '#AA00FF'],
             direction = 'diagonal-right',
             positions = None):
    validDirections = ['diagonal-left', 'diagonal-right', 'horizontal', 'vertical']
    if positions is None:
        match_ = findMatch(direction, validDirections)
        if match_ == 'diagonal-left': positions = [0,0, 1,1]
        if match_ == 'diagonal-right': positions = [1,0, 0,1]
        if match_ == 'horizontal': positions = [0,1.5, 0,0]
        if match_ == 'vertical': positions = [1.3,0, 0,0]

    gradientString = f'qlineargradient(x1:{positions[0]}, y1:{positions[1]}' \
                     f', x2:{positions[2]}, y2:{positions[3]},' \
                     f'stop:1 {colors[0]}, stop:0 {colors[1]})'

    return gradientString