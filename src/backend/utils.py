"""Python
utils.py
类型: 工具集
"""

import os
import logging


def get_frontend():
    """
    获取前端入口绝对路径\n
    返回值: 前端入口文件 file 协议
    """
    # 获取绝对路径
    path = os.path.join("frontend", "index.html")
    abs_path = os.path.abspath(path)

    # 转换 file 协议
    file_url = f"file:///{abs_path.replace('\\', '/')}"

    return file_url


def get_cache_name():
    """
    获取本程序缓存路径\n
    返回值: 返回 "%AppData%\\FC5CheatCache" 路径 (如果无法访问则返回 "C:\\FC5CheatCache" )
    """
    # 定义程序缓存文件夹名称
    cache_name = "FC5CheatCache"

    # 访问 %AppData% 并拼接程序缓存文件夹名称
    path = os.path.join(os.getenv("APPDATA"), cache_name)
    if not path:
        return f"C:\\{cache_name}"
    else:
        return path


def log_and_return(content, level):
    """
    输出到日志并返回\n
    传入参数: 内容 | 等级 (success/error)\n
    返回值: 前端 json
    """

    # 等级映射
    level_map = {
        "success": {"logger": logging.info, "code": 0},
        "error": {"logger": logging.error, "code": -1},
    }

    # 打印日志
    if level in level_map:
        level_map[level]["logger"](content)
    else:
        logging.warning("传达信息: “%s”不支持传入类型 “%s”", content, level)
        print(f"不支持传入类型 “{level}”")

    # 返回前端 json
    if level in level_map:
        return {"code": level_map[level]["code"], "msg": content, "data": None}
    else:
        return {
            "code": -1,
            "msg": f"操作异常：不支持的日志等级「{level}」",
            "data": None,
        }
