from PyView import *
window = Window()
window.size(600, 400)

myButton = _combobox_(window)
myButton.place(10,10)

label = Label(window, text='hello')
label.place(100, 100)

button1 = Button(window, text="do something", hover_color='red', command=lambda: label.configure(text='test'))
button1.place(200,200)

window.run()
