from PyQt5.QtWidgets import QFileDialog


class FileDialog:
    def __init__(self, master):
        self._master = master._getM()

    def ask_open_file(self, title='FileDialog', filetypes='All Files (*.*)', default_filename=''):
        file_path, _ = QFileDialog.getOpenFileName(self._master, title, default_filename, filetypes.replace(';',';;'), options=QFileDialog.Options())
        return file_path





def ask_open_file(master, title='FileDialog', filetypes='All Files (*.*)', default_filename=''):
    file_dialog = FileDialog(master)
    path = file_dialog.ask_open_file(title,filetypes,default_filename)
    return path
