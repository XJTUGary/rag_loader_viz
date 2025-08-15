class BaseLoader:
    """加载器基类"""
    def __init__(self, file_path):
        self.file_path = file_path
        self.document = None

    def load(self):
        """加载文档，返回解析后的内容"""
        raise NotImplementedError("子类必须实现load方法")

    def get_metadata(self):
        """获取文档元数据"""
        return {
            "file_path": self.file_path,
            "loader_type": self.__class__.__name__
        }