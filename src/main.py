"""Python
main.py
类型: 入口文件
"""

import logging
import webview

# from backend.utils import get_frontend
from backend.logger import init_logger
from backend.api import BackendAPI

if __name__ == "__main__":
    # 初始化日志并输出
    logger = init_logger()
    logging.info("程序已启动")

    # 创建窗口
    webview.create_window(
        title="Far Cry 5 Cheat Desktop",
        url="http://127.0.0.1:3000/Python/FC5 Cheat/src/frontend/index.html",
        width=1100,
        height=750,
        js_api=BackendAPI(),  # 千万千万不要丢掉括号, 否则JS无法访问PY
    )

    # 启动应用 (I/O阻塞)
    webview.start(debug=True)

    # 当 WebView 窗口消失时再次输出日志
    logging.info("程序已结束")
    logging.info("=" * 40)
