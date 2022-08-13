"""文书基类"""
from typing import Any

from pydantic import BaseModel

from .contents import Contents


class BaseDocument(BaseModel):
    """文书基类"""

    #: 文书编号
    id: str

    #: 文书名称
    name: str

    #: 文书类型
    types: set[str]


class InputDocument(BaseDocument):
    """输入文书类"""

    #: 文书内容, 可以为任何类型
    contents: Any


class Document(BaseDocument):
    """文书类"""

    #: 文书内容, 为标准化的 Content 列表
    contents: Contents
