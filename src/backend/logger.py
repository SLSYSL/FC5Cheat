"""Python
logger.py
类型: 日志工具
"""

import os
import logging
from logging.handlers import TimedRotatingFileHandler
from datetime import datetime
from .utils import get_cache_name


def init_logger():
    """
    设置应用程序的日志记录器\n
    返回值: 配置完成的 logger 对象
    """
    # 获取本程序缓存路径
    path = get_cache_name()

    # 构建日志目录路径
    log_dir = os.path.join(path, "Logs")
    date = datetime.now().strftime("%Y%m%d")
    log_file = os.path.join(log_dir, f"FC5Cheat_{date}.log")

    # 创建日志目录
    try:
        os.makedirs(log_dir, exist_ok=True)
    except OSError as e:
        print(f"创建日志目录失败: {e}")
        raise

    # 配置根日志记录器
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)

    # 创建文件处理器
    try:
        file_handler = TimedRotatingFileHandler(
            filename=log_file,
            when="midnight",
            interval=1,
            backupCount=30,
            encoding="utf-8",
        )
    except (OSError, IOError) as e:
        print(f"无法创建或写入日志文件 {log_file}: {e}")
        raise

    # 设置文件日志的格式和级别
    file_format = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - [%(filename)s:%(lineno)d] - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )
    file_handler.setFormatter(file_format)
    file_handler.setLevel(logging.INFO)  # 文件里记录INFO及以上级别的日志

    # 将处理器添加到日志记录器
    logger.handlers.clear()  # 清除可能存在的旧处理器，避免重复
    logger.addHandler(file_handler)

    # 记录一条初始化成功的日志
    logging.info("日志系统初始化完成, 日志文件位于: %s", log_file)
    return logger
