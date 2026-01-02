"""Python
modifier_utils.py
类型: 修改器实用工具
"""

from typing import List, Any


class ModifierUtils:
    """修改器实用工具类"""

    @staticmethod
    def disable_modifiers(modifiers: List[Any]) -> tuple[bool, str]:
        """
        禁用多个修改器

        Args:
            modifiers: 修改器对象列表，每个对象必须有disable方法

        Returns:
            (是否成功, 消息)
        """
        errors = []

        for i, modifier in enumerate(modifiers):
            modifier_type = (
                getattr(modifier, "__class__", {}).__name__ or f"修改器{i + 1}"
            )

            if hasattr(modifier, "disable"):
                try:
                    success, msg = modifier.disable()
                    if not success and "未启用" not in msg:
                        errors.append(f"{modifier_type}: {msg}")
                except Exception as e:
                    errors.append(f"{modifier_type}禁用异常: {e}")
            else:
                errors.append(f"{modifier_type}没有disable方法")

        if errors:
            return False, "禁用失败: " + "; ".join(errors)

        return True, "所有修改器已禁用"

    @staticmethod
    def get_combined_status(modifiers_dict: dict) -> dict:
        """
        获取多个修改器的组合状态

        Args:
            modifiers_dict: 修改器字典，格式为{名称: 修改器对象}

        Returns:
            组合状态字典
        """
        status = {}

        for name, modifier in modifiers_dict.items():
            if hasattr(modifier, "enabled"):
                status[f"{name}_enabled"] = modifier.enabled
            elif hasattr(modifier, "target_addr"):
                status[f"{name}_enabled"] = modifier.target_addr is not None
            else:
                status[f"{name}_enabled"] = False

        return status
