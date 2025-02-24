from PySide6.QtWidgets import QWidget, QBoxLayout
from vg_view import VisualGraphView
from vg_scene import VisualGraphScene

class VisualGraphEditor(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.view = None
        self.scene = None
        self.layout = None

        self.setup_editor()

    def setup_editor(self):
        self.setGeometry(100,100,1280,720)

        self.setWindowTitle("Visual Graph")

        self.layout = QBoxLayout(QBoxLayout.LeftToRight, self)
        self.layout.setContentsMargins(0,0,0,0)
        
        self.scene = VisualGraphScene()
        self.view = VisualGraphView(self.scene, self)
        self.layout.addWidget(self.view)

        self.show()