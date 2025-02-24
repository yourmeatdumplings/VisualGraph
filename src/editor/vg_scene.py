from PySide6.QtWidgets import QGraphicsScene
from PySide6.QtGui import QBrush, QColor, QPen
from PySide6.QtCore import Qt, QLine
from vg_config import EditorConfig
import PySide6
import math

class VisualGraphScene(QGraphicsScene):
    def __init__(self,parent=None):
        super().__init__(parent)

        self.setBackgroundBrush(QBrush(QColor("#212121")))

        self._width = EditorConfig.editor_scene_width
        self._height = EditorConfig.editor_scene_height
        self._grid_size = EditorConfig.editor_scene_grid_size
        self._chunk_size = EditorConfig.editor_scene_chunk_size

        self.setSceneRect(self._width / 2, self._height / 2, self._width, self._height)

        self._normal_line_pen = QPen(QColor(EditorConfig.editor_scene_grid_normal_line_color))
        self._normal_line_pen.setWidthF(EditorConfig.editor_scene_grid_normal_line_width)

        self._dark_line_pen = QPen(QColor(EditorConfig.editor_scene_grid_dark_line_color))
        self._dark_line_pen.setWidthF(EditorConfig.editor_scene_grid_dark_line_width)

    def drawBackground(self, painter: PySide6.QtGui.QPainter, rect):
        super().drawBackground(painter, rect)

        lines, dark_lines =  self.cal_grid_lines(rect)

        painter.setPen(self._normal_line_pen)
        painter.drawLines(lines)

        painter.setPen(self._dark_line_pen)
        painter.drawLines(dark_lines)

    def cal_grid_lines(self,rect):
        left, right, top, bottom = math.floor(rect.left()), math.floor(rect.right()), math.floor(
            rect.top()), math.floor(rect.bottom())

        first_left = left - (left % self._grid_size)
        first_top = top - (top % self._grid_size)

        lines = []
        dark_lines = []
        for v in range(first_top, bottom, self._grid_size):
            line = QLine(left, v, right, v)

            if v % (self._grid_size * self._chunk_size) == 0:
                dark_lines.append(line)
            else:
                lines.append(line)

        for h in range(first_left, right, self._grid_size):
            line = QLine(h, top, h, bottom)

            if h % (self._grid_size * self._chunk_size) == 0:
                dark_lines.append(line)
            else:
                lines.append(line)

        return lines, dark_lines