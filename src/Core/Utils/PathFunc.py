# -*- coding: utf-8 -*-
# 标准库导入
import winreg
from abc import ABC
from pathlib import Path

# 第三方库导入
from loguru import logger

# 项目内模块导入
from src.Core.Utils.singleton import Singleton


class PathFunc(metaclass=Singleton):

    def __init__(self):
        """
        ## 初始化
        """
        self.qq_path = None
        self.base_path = Path.cwd()
        self.napcat_path = self.base_path / "NapCat"
        self.config_dir_path = self.base_path / "config"
        self.config_path = self.config_dir_path / "config.json"
        self.bot_config_path = self.config_dir_path / "bot.json"
        self.tmp_path = self.base_path / "tmp"

        self.log_path = self.base_path / "log"
        self.log_info_path = self.log_path / "info"
        self.log_debug_path = self.log_path / "debug"

        self.pathValidator()

    def pathValidator(self) -> None:
        """
        ## 验证一系列路径
        """
        logger.info(f"{'-' * 10}开始验证路径{'-' * 10}")

        paths_to_validate = [
            (self.config_dir_path, "Config"),
            (self.tmp_path, "Tmp"),
            (self.napcat_path, "NapCat"),
            (self.log_path, "Log"),
            (self.log_info_path, "Log Info"),
            (self.log_debug_path, "Log Debug"),
        ]

        for path, name in paths_to_validate:
            if not path.exists():
                path.mkdir(parents=True, exist_ok=True)
                logger.info(f"{name} Path 路径不存在, 已创建")
            elif not path.is_dir():
                path.mkdir(parents=True, exist_ok=True)
                logger.warning(f"存在一个名为 {name.lower()} 的文件, 请检查")
            logger.info(f"{name} Path 验证完成")

        logger.info(f"{'-' * 10}路径验证完成{'-' * 10}")

    @staticmethod
    def getQQPath() -> Path | None:
        """
        获取QQ路径
        """
        try:
            key = winreg.OpenKey(
                key=winreg.HKEY_LOCAL_MACHINE,
                sub_key=r"SOFTWARE\WOW6432Node\Tencent\QQNT",
            )
            return Path(winreg.QueryValueEx(key, "Install")[0])
        except FileNotFoundError:
            return None

    def getNapCatPath(self) -> Path:
        """
        ## 获取 NapCat 路径
        """
        return self.napcat_path
