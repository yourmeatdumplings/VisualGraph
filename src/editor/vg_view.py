from PySide6.QtWidgets import QGraphicsView

class VisualGraphView(QGraphicsView):
    def __init__(self, scene, parent=None):
        super().__init__(parent)

        self._scene = scene
        self.setScene(self._scene)