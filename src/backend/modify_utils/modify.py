"""Python
modify.py
类型: 修改器
"""

from .base_modifier import BaseModifier, ModifierConfig


class StealthManager(BaseModifier):
    """隐身模式管理器"""

    def __init__(self):
        config = ModifierConfig(
            module_name="FC_m64.dll",
            pattern="0F84 0000 0000 498B 0048 895C 24",
            mask="xx????xxxxxxx",
            patch="90E9",
            original_size=2,
        )
        super().__init__(config)


class OxygenManager(BaseModifier):
    """无限氧气管理器"""

    def __init__(self):
        config = ModifierConfig(
            module_name="FC_m64.dll",
            pattern="40 57 48 83 EC 70 48 8B 01",
            mask="xxxxxxxxx",
            patch="C3 90",
            original_size=2,
        )
        super().__init__(config)


class StaminaManager(BaseModifier):
    """无限体力管理器"""

    def __init__(self):
        config = ModifierConfig(
            module_name="FC_m64.dll",
            pattern="40 53 48 83 EC 40 48 8B 01 48 8B D9 0F",
            mask="xxxxxxxxxxxxx",  # 13个x对应13个字节
            patch="C3 90",  # 将前两个字节修改为 C3 90 (ret; nop)
            original_size=2,  # 只需要保存和恢复前2个字节
        )
        super().__init__(config)


class NoClipManager(BaseModifier):
    """人物穿墙"""

    def __init__(self):
        config = ModifierConfig(
            module_name="FC_m64.dll",
            pattern="43 FF 94 D3 60 0C 00 00 48 8B 07",
            mask="xxxxxxxxxxx",
            patch="90 90 90 90 90 90 90 90",
            original_size=8,
        )
        super().__init__(config)
