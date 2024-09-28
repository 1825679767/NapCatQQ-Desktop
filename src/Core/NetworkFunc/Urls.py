# -*- coding: utf-8 -*-
# 标准库导入
from enum import Enum

from PySide6.QtCore import QUrl


class Urls(Enum):
    """
    ## 软件内部可能用的到的 Url
    """

    # NCD相关地址
    NCD_REPO = QUrl("https://github.com/HeartfeltJoy/NapCatQQ-Desktop")
    NCD_ISSUES = QUrl("https://github.com/HeartfeltJoy/NapCatQQ-Desktop/issues")

    # NapCat 相关地址
    NAPCATQQ_REPO = QUrl("https://github.com/NapNeko/NapCatQQ")
    NAPCATQQ_ISSUES = QUrl("https://github.com/NapNeko/NapCatQQ/issues")
    NAPCATQQ_REPO_API = QUrl("https://nclatest.znin.net")
    NAPCATQQ_DOCUMENT = QUrl("https://napneko.github.io/")

    # 直接写入下载地址, 不请求 API 获取, 期望达到节省时间的目的
    NAPCAT_DOWNLOAD = QUrl("https://github.com/NapNeko/NapCatQQ/releases/latest/download/NapCat.Shell.zip")

    # QQ 相关
    QQ_OFFICIAL_WEBSITE = QUrl("https://im.qq.com/index/")
    QQ_WIN_DOWNLOAD = QUrl("https://dldir1.qq.com/qqfile/qq/QQNT/0f14ef6e/QQ9.9.15.28131_x64.exe")
    QQ_AVATAR = QUrl("https://q.qlogo.cn/headimg_dl")
