"""Python
api.py
类型: 调用修改器API
"""

from .modifier import Modifier


class BackendAPI:
    """
    修改器API (前端调用)
    """

    def __init__(self):
        self.modify = Modifier()

    def handle_connect_game(self, is_enabled):
        """连接到游戏进程"""
        if is_enabled:
            return self.modify.connect_game()
        else:
            return self.modify.disconnect_game()

    def handle_stealth_mode(self, is_enabled):
        """隐身模式"""
        return self.modify.stealth_mode(is_enabled)

    def handle_oxygen_mode(self, is_enabled):
        """无限氧气"""
        return self.modify.oxygen_mode(is_enabled)

    def handle_stamina_mode(self, is_enabled):
        """无限体力"""
        return self.modify.stamina_mode(is_enabled)

    def handle_noclip_mode(self, is_enabled):
        """穿墙"""
        return self.modify.noclip_mode(is_enabled)
