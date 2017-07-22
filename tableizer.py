

class Tableizer(object):
    def __init__(self, columns=3, rows=3, column_width=15, row_height=1,
                 v_line_char='-', h_line_char='|',
                 intersection_char='+', filler_char=' ',
                 corner_top_left_char='+', corner_top_right_char='+',
                 corner_bottom_left_char='+', corner_bottom_right_char='+',
                 flat_borders=False):
        self.columns = columns
        self.rows = rows
        self.column_width = column_width
        self.row_height = row_height

        self.v_line_char = v_line_char
        self.h_line_char = h_line_char
        self.corner_top_left_char = corner_top_left_char
        self.corner_top_right_char = corner_top_right_char
        self.corner_bottom_left_char = corner_bottom_left_char
        self.corner_bottom_right_char = corner_bottom_right_char
        self.intersection_char = intersection_char
        self.filler_char = filler_char

        self.flat_borders = flat_borders

    def tableize(self):
        """
        Builds the actual table."""
        if (self.flat_borders):
            table = self.build_border_top()
        else:
            table = self.build_row_separator()

        for n, idx in enumerate(range(self.rows)):
            if (idx < self.rows - 1):
                table += '\n' + self.build_row()
            else:
                table += '\n' + self.build_row(True)

            # table += '\n' + self.build_row()

        return table

    def _build_border(self, location='top'):
        """
        Builds the top and bottom border."""
        border = ''

        if (self.flat_borders):
            # top left corner
            if (location == 'top'):
                border += self.corner_top_left_char
            elif (location == 'bottom'):
                border += self.corner_bottom_left_char

            for n in range(self.columns * self.column_width +
                           self.columns  - 1):
                border += self.v_line_char

            # top right corner
            if (location == 'top'):
                border += self.corner_top_right_char
            elif (location == 'bottom'):
                border += self.corner_bottom_right_char
        else:
            border += self.build_row_separator()

        return border

    def build_border_top(self):
        return self._build_border('top')

    def build_border_bottom(self):
        return self._build_border('bottom')

    def build_row(self, is_last_row=False):
        """
        Builds a single row. The height of the row is the height that is
        specified for a tableizer object."""
        row = ''

        for n in range(self.row_height):
            for cell in range(self.columns):
                row += self.h_line_char
                for n in range(self.column_width):
                    row += self.filler_char
            row += self.h_line_char
            row += '\n'

        if (is_last_row):
            row += self.build_border_bottom()
        else:
            row += self.build_row_separator()

        return row

    def build_row_separator(self):
        """"
        Builds a row separator including intersection characters."""
        if (self.flat_borders):
            row = self.h_line_char
        else:
            row = self.intersection_char

        for cell, idx in enumerate(range(self.columns)):
            for char in range(self.column_width):
                row += self.v_line_char
            # The last char should not be an intersection char
            if (idx < self.columns - 1):
                row += self.intersection_char
        if (self.flat_borders):
            row += self.h_line_char
        else:
            row += self.intersection_char

        return row




if __name__ == '__main__':
    tableizer = Tableizer(row_height=3)
    print tableizer.Tableize()

    print '\n' + '=' * 75 + '\n'

    tableizer = Tableizer(columns=5, rows=10, column_width=2)
    print tableizer.Tableize()

    print '\n' + '=' * 75 + '\n'

    tableizer = Tableizer(columns=5, rows=4, filler_char='x', column_width=3)
    print tableizer.Tableize()

    print '\n' + '=' * 75 + '\n'

    tableizer = Tableizer(columns=4, rows=4, column_width=5, flat_borders=True)
    print tableizer.Tableize()

    print '\n' + '=' * 75 + '\n'

    tableizer = Tableizer(columns=4, rows=4, column_width=5, flat_borders=True)
    print tableizer.Tableize()
