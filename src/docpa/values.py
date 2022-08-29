"""标准值类型"""

from __future__ import annotations
from typing import Any, Type, Literal, Callable, ClassVar

from pydantic import BaseModel
from typing_extensions import Self


class AnyValue(BaseModel):
    """任意值类型, 为标准值类型基类"""
    _f: ClassVar[Callable[[Any], Any]] = lambda x: x
    type_name: Literal["any"] = "any"
    value: Any

    @classmethod
    def parse(cls, raw: Any) -> Self:
        """从原始值构建"""
        return cls(value=cls._f(raw))

    @classmethod
    def subclasses(cls) -> dict[str, Type[AnyValue]]:
        """获取所有子类 type_name 与 cls 的对应关系"""
        rv = {}
        for sub in cls.__subclasses__():
            if not sub.type_name:
                raise ValueError(f"{sub.__name__} 的 type_name 为空")
            if sub.type_name in rv:
                raise KeyError(f"{sub.__name__} 的 type_name 有重复")
            rv[sub.type_name] = sub
            if sub.__subclasses__():
                rv.update(sub.subclasses())     # noqa
        return rv


class StrValue(AnyValue):
    """字符串值类型"""
    _f: ClassVar[Callable[[Any, ], str]] = str
    type_name: Literal["str"] = "str"
    value: str


class IntValue(AnyValue):
    """整数值类型"""
    _f: ClassVar[Callable[[Any, ], int]] = int
    type_name: Literal["int"] = int


class WrongValue(AnyValue):
    """错误值类型, 当解析发生错误时以此值代替"""
    type_name: Literal["wrong_value"] = "wrong_value"

    def as_value_error_and_raise(self):
        """转为 :exec:`ValueError` 然后抛出"""
        raise ValueError(self.value)
