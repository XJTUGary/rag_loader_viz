from .base_loader import BaseLoader

try:
    from PyPDF2 import PdfReader
except ImportError:
    raise ImportError("请安装PyPDF2: pip install PyPDF2")

import os

class PDFLoader(BaseLoader):
    """PDF文件加载器"""
    def load(self):
        """加载PDF文件"""
        try:
            reader = PdfReader(self.file_path)
            text = ""
            for page in reader.pages:
                text += page.extract_text() or ""

            self.document = {
                "content": text,
                "metadata": {
                    **self.get_metadata(),
                    "pages": len(reader.pages)
                },
                "type": "pdf"
            }
            return self.document
        except Exception as e:
            print(f"加载PDF文件失败: {e}")
            return None