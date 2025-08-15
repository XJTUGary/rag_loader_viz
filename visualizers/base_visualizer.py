try:
    import streamlit as st
except ImportError:
    raise ImportError("请安装streamlit: pip install streamlit")

from abc import ABC, abstractmethod


class BaseVisualizer(ABC):
    """可视化器基类"""
    def __init__(self, document):
        """初始化方法"""
        self.document = document

    @abstractmethod
    def visualize(self):
        """可视化文档内容"""
        pass

    def display_metadata(self):
        if self.document and "metadata" in self.document:
            st.subheader("文档元数据")
            metadata = self.document["metadata"]
            for key, value in metadata.items():
                st.write(f"{key}: {value}")
        else:
            st.info("没有可用的文档元数据")