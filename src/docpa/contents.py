"""解析值类型"""

from typing import Any, Optional, TypeAlias

from pydantic import BaseModel


class Content(BaseModel):
    """解析值类型"""

    #: 字段名
    key: str

    #: 字段值
    value: Any

    #: 原始值
    raw: Any

    #: 附加属性
    extra: Optional[dict]


Contents: TypeAlias = list[Content]
