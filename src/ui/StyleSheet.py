# -*- coding: utf-8 -*-
from enum import Enum
from pathlib import Path

from qfluentwidgets import StyleSheetBase, Theme, qconfig


class StyleSheet(StyleSheetBase, Enum):
    """样式表"""
    HOME_WIDGET = "home_widget"

    def path(self, theme=Theme.AUTO):
        theme = qconfig.theme if theme == Theme.AUTO else theme
        return f":QSS/qss/{theme.value.lower()}/{self.value}.qss"