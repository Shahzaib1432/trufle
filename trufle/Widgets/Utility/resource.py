
class Resources:
    BUTTON_ARGS       = 'text_alignment\nshortcut\ntext\ntext_color\npressed_color\nbutton_color\nhover_color\nwidth\nheight\nborder_width\nborder_color\nhover_color\ncorner_radius\nfont\nfont_size\ncommand\nstate\nimage\nimage_width\nimage_height\ncan_hover\nmaster'
    BUTTONGROUP_ARGS =  'frame_color\nbutton_color\nvalues\nbutton_selected_color\nframe_corner_radius\npadding\nwidth\nheight\nframe_border_width\nframe_border_color\ngroup_padding\ncommand'
    CANVAS_ARGS       = 'width\nheight\ncanvas_color\nborder_width\nborder_color\ncorner_radius'
    CHECKBOX_ARGS     = 'button_width\nbutton_height\nbutton_symbol_width\nbutton_symbol_height\nbutton_color\nbutton_hover_color\nbutton_border_width\nbutton_border_color\nbutton_border_hover_color\nbutton_corner_radius\nunknown_value\noff_value\non_value\nlabel_text\nlabel_text_color\nlabel_font\nlabel_font_size\nlabel_outside_color\nlabel_width\nlabel_height\npadding\ntrials'
    COMBOBOX_ARGS =     'width\nheight\nitems\nentry_text\nentry_default_text\nentry_text_color\nentry_color\nentry_border_width\nentry_border_color\nentry_corner_radius\nentry_font\nentry_font_size\nbutton_corner_radius\nbutton_border_width\nbutton_border_color\nbutton_color\nbutton_hover_color\nbutton_indicator_color\nbutton_indicator_size\nbutton_width\n_buttonEntryParts\nmenu_width\nmenu_height\nmenu_color\nmenu_border_width\nmenu_border_color\nmenu_position_x\nmenu_position_y\nmenu_items_padding\nitems_text_color\nitems_text_font\nitems_text_font_size\nitems_hover_text_color\nitems_hover_color\nitems_press_text_color\nitems_press_color'
    DATAGRID_ARGS =     'master\nwidth\nheight\ntext_color\ndata_grid_color\ndata_grid_corner_radius\ndata_grid_border_width\ndata_grid_border_color\nitems_color\nitems_pressed_text_color\nitems_corner_radius\nitems_pressed_color\nitems_border_width\nitems_border_color\ncolumns_color\ncolumns_corner_radius\nrows_color\nrows_corner_radius\nhorizontal_headers_text_color\nhorizontal_headers_color\nhorizontal_headers_pressed_color\nhorizontal_headers_border_width\nhorizontal_headers_border_color\nhorizontal_headers_corner_radius\nhorizontal_headers_padding\nhorizontal_headers_padding_color\nvertical_headers_text_color\nvertical_headers_color\nvertical_headers_pressed_color\nvertical_headers_border_width\nvertical_headers_border_color\nvertical_headers_padding\nvertical_headers_padding_color\nvertical_headers_corner_radius'
    POSITIONGRIP_ARGS = 'width\nheight\nposition_grip_color\nborder_width\nborder_color\ncorner_radius'
    ENTRY_ARGS =        'master\ntext\ndefault_text\ntext_color\nentry_color\nwidth\nheight\nborder_width\nborder_color\ncorner_radius\nfont\nfont_size\nstate'
    EXPANDER_ARGS =     'x\ny\nwidth\nheight\nborder_width\nborder_color\ncorner_radius\nexpand_vertically\nexpand_horizontally\ncontainer_color\nbutton_icon_color\nbutton_icon_size\nbutton_color\nbutton_hover_color\nbutton_pressed_color\nbutton_icon_alignment\nbutton_corner_radius\nbutton_x\nbutton_y\nbutton_width\nbutton_height\nunexpanded_height\nexpanded_height\nunexpanded_width\nexpanded_width\nanimation_duration\nanimation_power\nanimation_extra_speed\nanimation_curve\nmode\nstarts_expanded\nplacing_padding'
    FRAME_ARGS =        'master\nwidth\nheight\nframe_color\ncorner_radius\nborder_width\nborder_color'
    IMAGEDISPLAY_ARGS = 'master\nimage\nwidth\nheight'
    LABEL_ARGS =        'master\ntext\ntext_color\noutside_color\nfont\nfont_size\nwidth\nheight'

    def print_args(self, widget: str):
        match widget.upper():
            case 'BUTTON'       : print(self.BUTTON_ARGS)
            case 'BUTTONGROUP'  : print(self.BUTTONGROUP_ARGS)
            case 'CANVAS'       : print(self.CANVAS_ARGS)
            case 'CHECKBOX'     : print(self.CHECKBOX_ARGS)
            case 'COMBOBOX'     : print(self.COMBOBOX_ARGS)
            case 'DATAGRID'     : print(self.DATAGRID_ARGS)
            case 'POSITIONGRIP' : print(self.POSITIONGRIP_ARGS)
            case 'ENTRY'        : print(self.ENTRY_ARGS)
            case 'EXPANDER'     : print(self.EXPANDER_ARGS)
            case 'FRAME'        : print(self.FRAME_ARGS)
            case 'IMAGEDISPLAY' : print(self.IMAGEDISPLAY_ARGS)
            case 'LABEL'       :  print(self.LABEL_ARGS)
        return ''