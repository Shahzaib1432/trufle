# Trufle Documentation
# Importing
```python
import trufle
```

# MainWindow
```python
window = trufle.Window(title, width, height, x, y)
```
All of these parameters are optional.

To change the width, height, x, y using a method:
```python
window.size(width, height, x, y)
```
The x and y parameters are optional.

Alternatively you can use the geometry method:
```python
window.geometry('{width}x{height}+{x}+{y}')
```
Again the x and y parameters in the geometry method are optional

To change the title:
```python
window.title('My Window')
```

To run the window:
```python
window.run()
```

To stop the window:
```python
window.close()
```

To change the icon:
```python
window.icon(path_to_icon)
```
Supported file types are .png .ico .svg

# This documentation isnt finished yet.
