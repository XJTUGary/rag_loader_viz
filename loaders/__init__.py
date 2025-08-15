from .base_loader import BaseLoader
from .text_loader import TextLoader
from .pdf_loader import PDFLoader
from .docx_loader import DocxLoader
from config import LOADER_CONFIG


def get_loader(loader_type, file_path):
    """根据加载器类型获取加载器实例"""
    if loader_type == "自动检测":
        # 根据文件扩展名自动选择加载器
        file_ext = file_path.split(".")[-1].lower()
        if file_ext == "txt":
            return TextLoader(file_path)
        elif file_ext == "pdf":
            return PDFLoader(file_path)
        elif file_ext == "docx":
            return DocxLoader(file_path)
        else:
            return None
    elif loader_type == "文本加载器":
        return TextLoader(file_path)
    elif loader_type == "PDF加载器":
        return PDFLoader(file_path)
    elif loader_type == "Word加载器":
        return DocxLoader(file_path)
    else:
        return None