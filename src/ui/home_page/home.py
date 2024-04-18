# -*- coding: utf-8 -*-

"""
主页
"""

from abc import ABC
from loguru import logger
from typing import TYPE_CHECKING, Self

from PySide6.QtCore import Qt, QRectF
from PySide6.QtGui import QPixmap, QPainter, QColor, QBrush, QPainterPath
from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QSizePolicy
from qfluentwidgets.components import ScrollArea
from qfluentwidgets.common import Theme, isDarkTheme
from creart import add_creator, exists_module, create
from creart.creator import AbstractCreator, CreateTargetInfo

from src.ui.style_sheet import StyleSheet
from src.ui.home_page.display_view import DisplayViewWidget
from src.ui.home_page.content_view import ContentViewWidget
from src.core.config import cfg

if TYPE_CHECKING:
    from src.ui.main_window import MainWindow


class HomeWidget(ScrollArea):

    def __init__(self):
        super().__init__()

    def initialize(self, parent: "MainWindow") -> Self:
        """
        初始化
        """
        # 创建显示控件
        self.view = self.judge_view()

        # 设置 ScrollArea
        self.setParent(parent)
        self.setObjectName("HomePage")
        self.setWidgetResizable(True)
        self.setWidget(self.view)

        # 调用方法
        self.update_bg_image()

        # 应用样式表
        StyleSheet.HOME_WIDGET.apply(self)

        return self

    @staticmethod
    def judge_view():
        """
        用于判断加载哪个 Widget
        """
        if cfg.get(cfg.start_open_display_view):
            return DisplayViewWidget()
        else:
            return ContentViewWidget()

    def update_bg_image(self) -> None:
        """
        用于更新图片大小
        """
        # 重新加载图片保证缩放后清晰
        if not isDarkTheme():
            self.bg_pixmap = QPixmap(":Global/image/Global/page_bg_light.png")
        else:
            self.bg_pixmap = QPixmap(":Global/image/Global/page_bg_dark.png")

        self.bg_pixmap = self.bg_pixmap.scaled(
            self.size(),
            aspectMode=Qt.AspectRatioMode.KeepAspectRatioByExpanding,  # 等比缩放
            mode=Qt.TransformationMode.SmoothTransformation  # 平滑效果
        )
        self.update()

    def paintEvent(self, event) -> None:
        """
        重写绘制事件绘制背景图片
        """
        painter = QPainter(self.viewport())
        painter.drawPixmap(self.rect(), self.bg_pixmap)
        super().paintEvent(event)

    def resizeEvent(self, event) -> None:
        """
        重写缩放事件
        """
        self.update_bg_image()
        super().resizeEvent(event)


class HomeWidgetClassCreator(AbstractCreator, ABC):
    # 定义类方法targets，该方法返回一个元组，元组中包含了一个CreateTargetInfo对象，
    # 该对象描述了创建目标的相关信息，包括应用程序名称和类名。
    targets = (CreateTargetInfo("src.ui.home_page.home", "HomeWidget"),)

    # 静态方法available()，用于检查模块"HomeWidget"是否存在，返回值为布尔型。
    @staticmethod
    def available() -> bool:
        return exists_module("src.ui.home_page.home")

    # 静态方法create()，用于创建HomeWidget类的实例，返回值为HomeWidget对象。
    @staticmethod
    def create(create_type: [HomeWidget]) -> HomeWidget:
        return HomeWidget()


add_creator(HomeWidgetClassCreator)
