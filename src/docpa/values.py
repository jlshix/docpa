"""标准值类型"""
from abc import abstractmethod
from typing import Any, Type, Literal

from pydantic import BaseModel
from typing_extensions import Self


class BaseValue(BaseModel):
    """标准值类型基类"""
    type_name: Literal[""] = ""

    @classmethod
    @abstractmethod
    def parse(cls, raw: Any) -> Self:
        """从原始值构建"""

    @classmethod
    def subclasses(cls) -> dict[str, Type[Self]]:
        """获取所有子类 type_name 与 cls 的对应关系"""
        rv = {}
        for sub in cls.__subclasses__():
            if not cls.type_name:
                raise ValueError(f"{sub.__name__} 的 type_name 为空")
            rv[sub.type_name] = sub
            if sub.__subclasses__():
                rv.update(sub.subclasses())
        return rv
