# -*- coding: utf-8 -*-
from typing import TYPE_CHECKING

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget
from qfluentwidgets import ExpandLayout, FluentIcon, ScrollArea

from src.Ui.AddPage.Card import (
    ComboBoxConfigCard,
    LineEditConfigCard,
    SwitchConfigCard,
)
from src.Ui.Icon import NapCatDesktopIcon

if TYPE_CHECKING:
    from src.Ui.AddPage.Add.AddWidget import AddWidget


class BotWidget(ScrollArea):
    """
    ## Bot Item 项对应的 QWidget
    """

    def __init__(self, parent: "AddWidget") -> None:
        super().__init__(parent=parent)
        self.setObjectName("BotWidget")
        self.view = QWidget()
        self.cardLayout = ExpandLayout(self)

        # 设置 ScrollArea
        self.setWidget(self.view)
        self.setWidgetResizable(True)
        self.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.view.setObjectName("BotWidgetView")

        # 调用方法
        self._initWidget()
        self._setLayout()

    def _initWidget(self):
        """
        ## 初始化 QWidget 所需要的控件并配置
        创建 Card
        """
        self.botNameCard = LineEditConfigCard(
            icon=FluentIcon.ROBOT,
            title=self.tr("Bot name"),
            content=self.tr("Set your bot name"),
            placeholder_text=self.tr("Bot 1"),
            parent=self.view,
        )
        self.botQQIdCard = LineEditConfigCard(
            icon=NapCatDesktopIcon.QQ,
            title=self.tr("Bot QQ"),
            content=self.tr("Set your bot QQ"),
            placeholder_text=self.tr("123456"),
            parent=self.view,
        )
        self.messageFormatCard = ComboBoxConfigCard(
            icon=FluentIcon.MESSAGE,
            title=self.tr("Message format"),
            content=self.tr("Array is the message group, and string is the cq code string"),
            texts=["array", "string"],
            parent=self.view,
        )
        self.reportSelfMessageCard = SwitchConfigCard(
            icon=FluentIcon.ROBOT,
            title=self.tr("Report self message"),
            content=self.tr("Whether to report the bot's own message"),
            parent=self.view,
        )
        self.heartIntervalCard = LineEditConfigCard(
            icon=FluentIcon.HEART,
            title=self.tr("Heart interval"),
            content=self.tr("WebSocket heartbeat interval, in milliseconds"),
            placeholder_text="30000",
            parent=self.view,
        )
        self.accessTokenCard = LineEditConfigCard(
            icon=FluentIcon.CERTIFICATE,
            title=self.tr("Access Token"),
            content=self.tr("Access Token, can be empty"),
            parent=self.view,
        )

        self.cards = [
            self.botNameCard,
            self.botQQIdCard,
            self.messageFormatCard,
            self.reportSelfMessageCard,
            self.heartIntervalCard,
            self.accessTokenCard,
        ]

    def _setLayout(self):
        """
        ## 将 QWidget 内部的 Card 添加到布局中
        """
        self.cardLayout.setContentsMargins(0, 0, 0, 0)
        self.cardLayout.setSpacing(2)
        for card in self.cards:
            self.cardLayout.addWidget(card)
            self.adjustSize()

        self.view.setLayout(self.cardLayout)

    def getValue(self) -> dict:
        """
        ## 返回内部卡片的配置结果
        """
        return {
            "name": self.botNameCard.getValue(),
            "QQID": self.botQQIdCard.getValue(),
            "msgFormat": self.messageFormatCard.getValue(),
            "reportSelfMsg": self.reportSelfMessageCard.getValue(),
            "heartInterval": self.heartIntervalCard.getValue(),
            "accessToken": self.accessTokenCard.getValue(),
        }

    def clearValues(self) -> None:
        """
        ## 清空(还原)内部卡片的配置
        """
        for card in self.cards:
            card.clear()

    def adjustSize(self):
        h = self.cardLayout.heightForWidth(self.width()) + 46
        return self.resize(self.width(), h)
