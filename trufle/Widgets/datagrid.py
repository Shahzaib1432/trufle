import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QAbstractItemView
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont

class DataGrid:
    def __init__(self,
                 master,
                 width=400,
                 height=200,
                 text_color='white',

                 data_grid_color='#000000',
                 data_grid_corner_radius = [0,10,10,0],
                 data_grid_border_width = 2,
                 data_grid_border_color = '#FFFFFF',

                 items_color='transparent',
                 items_pressed_text_color='white',
                 items_corner_radius = 0,
                 items_pressed_color='transparent',
                 items_border_width = 0,
                 items_border_color = 'black',

                 columns_color = 'red',
                 columns_corner_radius=[0,5,0,0],
                 rows_color='red',
                 rows_corner_radius=[0,0,5,0],

                 horizontal_headers_text_color = '#FFFFFF',
                 horizontal_headers_color='transparent',
                 horizontal_headers_pressed_color = '#DDDDDD',
                 horizontal_headers_border_width = 0,
                 horizontal_headers_border_color = '#1e1e1e',
                 horizontal_headers_corner_radius = 0,
                 horizontal_headers_padding = 1,
                 horizontal_headers_padding_color='#1e1e1e',

                 vertical_headers_text_color='#FFFFFF',
                 vertical_headers_color='transparent',
                 vertical_headers_pressed_color='#DDDDDD',
                 vertical_headers_border_width=0,
                 vertical_headers_border_color='#1e1e1e',
                 vertical_headers_padding = 1,
                 vertical_headers_padding_color='#1e1e1e',
                 vertical_headers_corner_radius = 0):
        horizontal_headers_corner_radius = self._bwCheck(horizontal_headers_corner_radius)
        vertical_headers_corner_radius = self._bwCheck(vertical_headers_corner_radius)
        data_grid_corner_radius = self._bwCheck(data_grid_corner_radius)
        items_corner_radius = self._bwCheck(items_corner_radius)
        columns_corner_radius = self._bwCheck(columns_corner_radius)
        rows_corner_radius = self._bwCheck(rows_corner_radius)
        # Init
        self._t = QTableWidget(master._getM() )
        self._t.setFixedSize(width, height)

        # Attributes
        self.attributes_width = width
        self.attributes_height = height
        self.attributes_text_color = text_color
        self.attributes_data_grid_color = data_grid_color
        self.attributes_items_color = items_color
        self.attributes_items_pressed_text_color = items_pressed_text_color
        self.attributes_items_pressed_color = items_pressed_color
        # /Attributes

        # remove scrollbar
        self._t.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        # Rows, Col Handling
        self._headerList = []
        self._header_ids = []
        self._t.setHorizontalHeaderLabels(self._headerList)
        self._row_ids = []
        self._headerIndexes = {}
        self._hIndex = 0

        # Styling

        self._t.setStyleSheet(f'''
            QTableWidget {{
                background-color: {data_grid_color};
                color: {text_color};
                border: {data_grid_border_width}px solid {data_grid_border_color};
                
                border-top-left-radius: {data_grid_corner_radius[0]};
                border-top-right-radius: {data_grid_corner_radius[1]};
                border-bottom-left-radius: {data_grid_corner_radius[2]};
                border-bottom-right-radius: {data_grid_corner_radius[3]};
            }}
            
            QTableWidget::item {{
                background-color: {items_color};
                border: {items_border_width}px solid {items_border_color};
                
                border-top-left-radius: {items_corner_radius[0]};
                border-top-right-radius: {items_corner_radius[1]};
                border-bottom-left-radius: {items_corner_radius[2]};
                border-bottom-right-radius: {items_corner_radius[3]};
            }}
            QTableWidget::item:selected {{
                background-color: {items_pressed_color};
                color: {items_pressed_text_color};
            }} ''')
        headers = self._t.horizontalHeader()
        headers.setStyleSheet(f'''
        QHeaderView {{
            background-color: {columns_color};

            border-top-left-radius: {columns_corner_radius[0]};
            border-top-right-radius: {columns_corner_radius[1]};
            border-bottom-left-radius: {columns_corner_radius[2]};
            border-bottom-right-radius: {columns_corner_radius[3]};
        }}
        
        QHeaderView::section {{
            background-color: {horizontal_headers_color};
            color: {horizontal_headers_text_color};
            
            border: {horizontal_headers_border_width}px solid {horizontal_headers_border_color};
            border-right: {horizontal_headers_padding}px solid {horizontal_headers_padding_color};
            
            border-top-left-radius: {horizontal_headers_corner_radius[0]};
            border-top-right-radius: {horizontal_headers_corner_radius[1]};
            border-bottom-left-radius: {horizontal_headers_corner_radius[2]};
            border-bottom-right-radius: {horizontal_headers_corner_radius[3]};
        }} ''')

        rows = self._t.verticalHeader()
        rows.setStyleSheet(f'''
        
        QHeaderView {{
            background-color: {rows_color};

            border-top-left-radius: {rows_corner_radius[0]};
            border-top-right-radius: {rows_corner_radius[1]};
            border-bottom-left-radius: {rows_corner_radius[2]};
            border-bottom-right-radius: {rows_corner_radius[3]};
        }}

        QHeaderView::section {{
            background-color: {vertical_headers_color};
            color: {vertical_headers_text_color};
            border: {vertical_headers_border_width}px solid {horizontal_headers_border_color};
            border-bottom: {vertical_headers_padding}px solid {vertical_headers_padding_color};

            border-top-left-radius: {vertical_headers_corner_radius[0]};
            border-top-right-radius: {vertical_headers_corner_radius[1]};
            border-bottom-left-radius: {vertical_headers_corner_radius[2]};
            border-bottom-right-radius: {vertical_headers_corner_radius[3]}; 
        }} ''')

        tblCorner = self._t.setCornerButtonEnabled(True)

        self._t.hide()

    def place(self, x,y):
        self._t.move(x,y)
        self._t.show()

    """
    Configure Methods
    """

    def reload(self):
        self._t.setStyleSheet(f'''
            QTableWidget {{
                background-color: {data_grid_color};
                color: {text_color};
            }}
            QTableWidget::item {{
                background-color: {items_color};
            }}
            QTableWidget::item:selected {{
                background-color: {items_pressed_color};
                color: {items_pressed_text_color};
            }} ''')

    def _bwCheck(self, bw):
        if type(bw) == int:
            bw = [bw,bw,bw,bw]
        return bw

    def configure(self,
               width=None,
               height=None,
               text_color=None,

               data_grid_color=None,
               items_color=None,
               items_pressed_text_color=None,
               items_pressed_color=None):
        if width is not None:                    self.attributes_width                    = width
        if height is not None:                   self.attributes_height                   = height
        if text_color is not None:               self.attributes_text_color               = text_color
        if data_grid_color is not None:          self.attributes_data_grid_color          = data_grid_color
        if items_color is not None:              self.attributes_items_color              = items_color
        if items_pressed_text_color is not None: self.attributes_items_pressed_text_color = items_pressed_text_color
        if items_pressed_color is not None:      self.attributes_items_pressed_color      = items_pressed_color
        self.reload()

    """
    Headers, Rows Methods
    """

    def add_header(self, header_id, text):
        if header_id in self._header_ids:
            raise ValueError("Header ID already exists.")

        self._header_ids.append(header_id)
        self._headerList.append(text)
        self._t.setColumnCount(len(self._headerList))
        self._t.setHorizontalHeaderLabels(self._headerList)

        self._headerIndexes[header_id] = self._hIndex
        self._hIndex += 1

    def edit_header(self, header_id, new_text):
        if header_id not in self._header_ids:
            raise ValueError("Header ID does not exist.")

        header_index = self._header_ids.index(header_id)
        self._headerList[header_index] = new_text
        self._t.setHorizontalHeaderLabels(self._headerList)

    def delete_header(self, header_id):
        if header_id not in self._header_ids:
            raise ValueError("Header ID does not exist.")

        index = self._headerIndexes.get(header_id)
        self._t.removeColumn(index)

    def add_row(self, row_id, data):
        if row_id in self._row_ids:
            raise ValueError("Row ID already exists.")

        self._row_ids.append(row_id)
        row_index = self._t.rowCount()
        self._t.setRowCount(row_index + 1)

        for col_index, item_text in enumerate(data):
            item = QTableWidgetItem(item_text)
            self._t.setItem(row_index, col_index, item)

    def edit_row(self, row_id, new_data):
        if row_id not in self._row_ids:
            raise ValueError("Row ID does not exist.")

        row_index = self._row_ids.index(row_id)
        for col_index, item_text in enumerate(new_data):
            item = QTableWidgetItem(item_text)
            self._t.setItem(row_index, col_index, item)

    def delete_row(self, row_id):
        if row_id not in self._row_ids:
            raise ValueError("Row ID does not exist.")

        row_index = self._row_ids.index(row_id)
        self._t.removeRow(row_index)
        self._row_ids.remove(row_id)

    def hide(self):
        self._t.hide()
    def show(self):
        self._t.show()