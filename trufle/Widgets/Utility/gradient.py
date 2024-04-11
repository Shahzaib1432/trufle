from difflib import get_close_matches

def findMatch(input_str, values):
    try:
        return get_close_matches(input_str, values, n=1)[0]
    except Exception:
        raise EnvironmentError(f'No matching direction was found.')

def Gradient(start='#FF0000', stop='#AA00FF',
             direction = 'diagonal-right',
             positions = None):
    validDirections = ['diagonal-left', 'diagonal-right', 'horizontal', 'vertical']
    if positions is None:
        match_ = findMatch(direction, validDirections)
        if match_ == 'diagonal-left': positions = [0,0, 1,1]
        if match_ == 'diagonal-right': positions = [1,0, 0,1]
        if match_ == 'horizontal': positions = [0,1.5, 0,0]
        if match_ == 'vertical': positions = [0,0,1,0]
    pos = positions

    gradientString = f'qlineargradient(x1: {pos[0]}, y1: {pos[1]}, x2: {pos[2]}, y2: {pos[3]}, stop: 0 {start}, stop: 1 {stop})'
    return gradientString
