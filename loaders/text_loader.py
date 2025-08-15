from .base_loader import BaseLoader
import os

class TextLoader(BaseLoader):
    """文本文件加载器"""
    def load(self):
        """加载文本文件"""
        try:
            with open(self.file_path, 'r', encoding='utf-8') as f:
                content = f.read()

            self.document = {
                "content": content,
                "metadata": self.get_metadata(),
                "type": "text"
            }
            return self.document
        except Exception as e:
            print(f"加载文本文件失败: {e}")
            return None