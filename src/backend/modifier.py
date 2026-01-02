"""Python
modifier.py
类型: 修改器函数
"""

import libmem
from .utils import log_and_return
from .modify_utils.modify import (
    StealthManager,
    OxygenManager,
    StaminaManager,
    NoClipManager,
)
from .modifier_utils import ModifierUtils


class Modifier:
    """修改器所有调用函数"""

    def __init__(self):
        self.process = None
        self.stealth_manager = StealthManager()
        self.oxygen_manager = OxygenManager()
        self.stamina_manager = StaminaManager()
        self.noclip_manager = NoClipManager()
        self.modifier_utils = ModifierUtils()

        # 初始化时关联进程（如果有）
        self.process_association()

    def process_association(self):
        """同步进程到所有管理器"""
        if self.process:
            self.stealth_manager.set_process(self.process)
            self.oxygen_manager.set_process(self.process)
            self.stamina_manager.set_process(self.process)
            self.noclip_manager.set_process(self.process)
        else:
            # 如果进程为空，也同步到管理器
            self.stealth_manager.set_process(None)
            self.oxygen_manager.set_process(None)
            self.stamina_manager.set_process(None)
            self.noclip_manager.set_process(None)

    def connect_game(self):
        """连接到游戏主进程"""
        try:
            # 连接进程
            self.process = libmem.find_process("FarCry5.exe")

            # 如果找不到进程则报错
            if not self.process:
                self.process = None
                self.process_association()  # 同步空进程状态
                return log_and_return("未找到进程", "error")

            # 将进程关联到所有管理器
            self.process_association()
            return log_and_return("已连接到主进程", "success")
        except Exception as e:
            self.process = None
            self.process_association()  # 同步空进程状态
            return log_and_return(f"连接失败: {e}", "error")

    def disable_all_modifiers(self):
        """禁用所有修改器"""
        modifiers = [
            self.stealth_manager,
            self.oxygen_manager,
            self.stamina_manager,
            self.noclip_manager,
        ]
        return self.modifier_utils.disable_modifiers(modifiers)

    def disconnect_game(self):
        """断开连接游戏主进程"""
        try:
            if not self.process:
                return log_and_return("未连接到主进程", "error")

            # 禁用所有修改器
            success, msg = self.disable_all_modifiers()
            if not success:
                return log_and_return(msg, "error")

            # 重置进程状态
            self.process = None
            self.process_association()
            return log_and_return("已取消锁定", "success")
        except OSError as e:
            self.process = None
            self.process_association()
            return log_and_return(f"无法取消锁定: 系统资源错误 - {e}", "error")
        except Exception as e:
            return log_and_return(f"无法取消锁定: {e}", "error")

    def stealth_mode(self, is_enabled):
        """隐身模式"""
        if not self.process:
            return log_and_return("未连接到游戏进程", "error")

        if is_enabled:
            success, msg = self.stealth_manager.enable()
        else:
            success, msg = self.stealth_manager.disable()

        return log_and_return(msg, "success" if success else "error")

    def oxygen_mode(self, is_enabled):
        """无限氧气"""
        if not self.process:
            return log_and_return("未连接到游戏进程", "error")

        if is_enabled:
            success, msg = self.oxygen_manager.enable()
        else:
            success, msg = self.oxygen_manager.disable()

        return log_and_return(msg, "success" if success else "error")

    def stamina_mode(self, is_enabled):
        """无限氧气"""
        if not self.process:
            return log_and_return("未连接到游戏进程", "error")

        if is_enabled:
            success, msg = self.stamina_manager.enable()
        else:
            success, msg = self.stamina_manager.disable()

        return log_and_return(msg, "success" if success else "error")

    def noclip_mode(self, is_enabled):
        """穿墙"""
        if not self.process:
            return log_and_return("未连接到游戏进程", "error")

        if is_enabled:
            success, msg = self.noclip_manager.enable()
        else:
            success, msg = self.noclip_manager.disable()

        return log_and_return(msg, "success" if success else "error")

    def get_status(self):
        """获取修改器状态"""
        status = {
            "connected": self.process is not None,
            "process_name": self.process.name if self.process else None,
        }

        # 获取修改器状态
        modifiers_dict = {
            "stealth": self.stealth_manager,
            "oxygen": self.oxygen_manager,
            "stamina": self.stamina_manager,
        }

        # 合并状态
        status.update(self.modifier_utils.get_combined_status(modifiers_dict))

        return status
