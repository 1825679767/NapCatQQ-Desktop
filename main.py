# -*- coding: utf-8 -*-
# 标准库导入
import sys
import ctypes

# 第三方库导入
from loguru import logger

# 项目内模块导入
from src.Core.Utils.mutex import SingleInstanceApplication
from src.Core.Utils.logger import Logger

NAPCATQQ_DESKTOP_LOGO = r"""

 +-+-+-+-+-+-+ +-+-+-+-+-+-+-+
 |N|a|p|C|a|t| |D|e|s|k|t|o|p|
 +-+-+-+-+-+-+ +-+-+-+-+-+-+-+
"""


if __name__ == "__main__":

    # 调整程序 log 输出
    Logger()

    # 实现单实例应用程序检查
    single_app_checker = SingleInstanceApplication()
    if single_app_checker.is_running():
        logger.error("检测到已经有 NapCat Desktop 正在运行, 取消运行")
        sys.exit()

    # 检查是否以管理员模式启动, 非管理员模式尝试获取管理员权限
    # 获取管理员权限成功后退出原有进程
    if not ctypes.windll.shell32.IsUserAnAdmin():
        logger.warning("非管理员模式启动, 尝试获取管理员权限")
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
        sys.exit()

    # 启动主程序
    # 第三方库导入
    from qfluentwidgets import FluentTranslator
    from PySide6.QtCore import QLocale
    from PySide6.QtWidgets import QApplication

    # 项目内模块导入
    from src.Core.Config import cfg
    from src.Ui.MainWindow import MainWindow

    logger.opt(colors=True).info(f"<blue>{NAPCATQQ_DESKTOP_LOGO}</>")
    # 创建app实例
    app = QApplication(sys.argv)

    # 加载翻译文件
    locale: QLocale = cfg.get(cfg.Language).value
    app.installTranslator(FluentTranslator(locale))

    # 显示窗体
    MainWindow().initialize()

    # 进入循环
    sys.exit(app.exec())
