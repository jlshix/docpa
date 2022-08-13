"""解析器"""

from abc import abstractmethod

from .documents import InputDocument, Document


class BaseParser:
    """解析器基类"""
    type_name: str = ""

    @abstractmethod
    def parse(self, input_document: InputDocument) -> Document:
        """实现解析方法"""
