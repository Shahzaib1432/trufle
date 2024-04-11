import ctypes

def get_dpi():
    hdc = ctypes.windll.user32.GetDC(0)
    dpi = ctypes.windll.gdi32.GetDeviceCaps(hdc, 88)
    ctypes.windll.user32.ReleaseDC(0, hdc)
    return dpi

def inches_to_pixels(inches, return_type=int, dpi=get_dpi()):
    pixels = inches * dpi
    return return_type(pixels)
