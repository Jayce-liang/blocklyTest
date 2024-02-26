from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtCore import QUrl
from PySide6.QtWidgets import (
    QApplication,
    QWidget,
    QVBoxLayout,
    QMainWindow,
)
import os,sys


class BlocklyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Blockly")
        self.resize(1024, 600)

        # 创建一个 central widget 作为布局容器
        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)

        self.webview = QWebEngineView(self.central_widget)

        # 添加权限 ==============================================================================
        self.webview.settings().setAttribute(
            self.webview.settings().WebAttribute.AllowRunningInsecureContent, True)
        self.webview.settings().setAttribute(
            self.webview.settings().WebAttribute.LocalContentCanAccessRemoteUrls, True)
        self.webview.settings().setAttribute(
            self.webview.settings().WebAttribute.PlaybackRequiresUserGesture, True)

        self.webview.settings().setAttribute(
            self.webview.settings().WebAttribute.WebGLEnabled, True)
        self.webview.settings().setAttribute(
            self.webview.settings().WebAttribute.Accelerated2dCanvasEnabled, True)
        self.webview.settings().setAttribute(
            self.webview.settings().WebAttribute.ScrollAnimatorEnabled, True)


        def handleFeaturePermissionRequested(url, feature):
            self.webview.page().setFeaturePermission(
                url, feature, QWebEnginePage.PermissionGrantedByUser)

        self.webview.page().featurePermissionRequested.connect(
            handleFeaturePermissionRequested)

        self.webview.settings().setAttribute(
            self.webview.settings().WebAttribute.AllowRunningInsecureContent, True)
        self.webview.settings().setAttribute(
            self.webview.settings().WebAttribute.LocalContentCanAccessRemoteUrls, True)
        # 添加权限 ==============================================================================



        current_path = (
            os.path.dirname(os.path.abspath(__file__)) +
            "/index.html"
        )




        self.webview.setUrl(QUrl.fromLocalFile(current_path))

        # self.webview.setUrl("http://127.0.0.1:5500/index.html")

        main_layout = QVBoxLayout(self.central_widget)
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(0)
        main_layout.addWidget(self.webview)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = BlocklyWidget()
    widget.show()
    ret = app.exec()
    if ret:
        sys.exit(ret)
