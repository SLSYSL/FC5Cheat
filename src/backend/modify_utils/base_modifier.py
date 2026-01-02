"""Python
base_modifier.py
类型: 基础修改器类
"""

from dataclasses import dataclass
from typing import Optional
import libmem


@dataclass
class ModifierConfig:
    """修改器配置类"""

    module_name: str
    pattern: str
    mask: str
    patch: str
    original_size: Optional[int] = None


class BaseModifier:
    """基础修改器类"""

    def __init__(self, config: ModifierConfig):
        self.config = config
        self.process = None
        self.target_addr = None
        self.original_bytes = None

    def enable(self):
        """启用修改功能"""
        if not self.process:
            return False, "未关联进程"

        try:
            # 查找目标模块
            module = self._find_module(self.config.module_name)
            if not module:
                return False, f"未找到模块 {self.config.module_name}"

            # 搜索特征码
            pattern = bytearray.fromhex(self.config.pattern.replace(" ", ""))
            target_addr = self._pattern_scan(module, pattern, self.config.mask)

            if not target_addr:
                return False, "特征码搜索失败"

            # 确定要保存的原始字节大小
            patch = bytearray.fromhex(self.config.patch.replace(" ", ""))
            read_size = (
                self.config.original_size if self.config.original_size else len(patch)
            )

            # 读取并保存原始字节
            self.original_bytes = self._read_memory(target_addr, read_size)

            # 写入修改字节
            if not self._write_memory(target_addr, patch):
                return False, "写入内存失败"

            # 验证修改
            if not self._verify_memory(target_addr, patch):
                return False, "修改验证失败"

            self.target_addr = target_addr
            return True, "修改已启用"
        except Exception as e:
            return False, f"启用失败: {e}"

    def disable(self):
        """禁用修改功能"""
        if not self.process or not self.target_addr or not self.original_bytes:
            return False, "参数不完整或未启用修改"

        try:
            if not self._write_memory(self.target_addr, self.original_bytes):
                return False, "恢复内存失败"

            # 重置状态
            self.target_addr = None
            self.original_bytes = None
            return True, "修改已禁用"
        except Exception as e:
            return False, f"禁用失败: {e}"

    def set_process(self, process):
        """设置关联的进程对象"""
        self.process = process
        self.target_addr = None
        self.original_bytes = None

    # 以下辅助方法与方案一相同
    def _find_module(self, module_name):
        if not self.process:
            return None
        return libmem.find_module_ex(self.process, module_name)

    def _pattern_scan(self, module, pattern, mask):
        if not module:
            return None
        return libmem.pattern_scan_ex(
            self.process, pattern, mask, module.base, module.size
        )

    def _read_memory(self, address, size):
        if not self.process or not address:
            return None
        return libmem.read_memory_ex(self.process, address, size)

    def _write_memory(self, address, data):
        if not self.process or not address:
            return False
        libmem.write_memory_ex(self.process, address, data)
        return True

    def _verify_memory(self, address, expected_data):
        actual_data = self._read_memory(address, len(expected_data))
        return actual_data == expected_data
