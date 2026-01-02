<h1 align="center">开发文档</h1>

## 环境要求
- Python 3.8+

## 准备环境
1. 安装 [Python](https://www.python.org/) 环境
2. 克隆本仓库

## 依赖安装
1. 在当前目录执行命令: `pip install -r requirements.txt`

## 前端热更新
1. 可以将 `main.py` 入口文件的 `url` 替换成 Live Server/Live Preview 地址

## 前端全局可用自定义 API 调用
- `callCheatAPI(id, api, is_read)`: 向后端发送请求
  - id: 给后端发送 Bool 
    - 一般情况: 前端 Switch DOM ID
    - is_connect 为 True: Bool
  - api: 后端 API 名称
    - String
  - is_read: 是否读取前端 Switch DOM ID (可选参数, 默认 False)
    - Bool
- `SimpleToast.makeText(info, {type, duration})`: 显示 Toasts 弹窗
  - info: 显示的内容
    - String
  - type: 弹窗类型 (default/success/error) (可选参数, 默认 default)
    - String
  - duration: 弹窗时长 (单位: ms) (传入<=0 则一直显示) (可选参数, 默认3000) 
    - Number

## 后端可以自定义 API 调用 (需要先导入 backend.utils 模块)
- `get_frontend()`: 获取前端入口绝对路径
  - 返回值: 前端入口绝对路径
    - String
- `get_cache_name()`: 获取本程序缓存路径
  - 返回值: 返回 "%AppData%\\FC5CheatCache" 路径 (如果无法访问则返回 "C:\\FC5CheatCache" )
    - String
- `log_and_return(content, level)`: 输出到日志并返回
  - content: 内容
    - String
  - level: 等级类型 (success/error)
    - String
  - 返回值: 前端 json
    - json