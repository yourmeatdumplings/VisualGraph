from PySide6.QtWidgets import QGraphicsScene
from PySide6.QtGui import QBrush, QColor
from vg_config import EditorConfig

class VisualGraphScene(QGraphicsScene):
    def __init__(self,parent=None):
        super().__init__(parent)

        self.setBackgroundBrush(QBrush(QColor("#212121")))

        self._width = EditorConfig.editor_scene_width
        self._height = EditorConfig.editor_scene_height

        self.setSceneRect(self._width / 2, self._height / 2, self._width, self._height)