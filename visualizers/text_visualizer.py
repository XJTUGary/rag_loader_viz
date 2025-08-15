try:
    import streamlit as st
except ImportError:
    raise ImportError("请安装streamlit: pip install streamlit")

import re

from .base_visualizer import BaseVisualizer


class TextVisualizer(BaseVisualizer):
    """文本可视化器"""
    def __init__(self, document):
        super().__init__(document)

    def visualize(self):
        """可视化文本内容"""
        if not self.document or "content" not in self.document:
            st.error("没有可可视化的内容")
            return

        # 显示元数据
        self.display_metadata()

        # 显示文本内容
        st.subheader("文本内容")
        content = self.document["content"]

        # 文本搜索功能
        search_query = st.text_input("搜索文本")
        if search_query:
            # 高亮搜索结果
            highlighted_content = re.sub(
                re.escape(search_query),
                lambda m: f"<mark>{m.group(0)}</mark>",
                content,
                flags=re.IGNORECASE
            )
            st.markdown(highlighted_content, unsafe_allow_html=True)
        else:
            st.text_area("文档内容", content, height=400)

        # 文本统计信息
        st.subheader("文本统计")
        char_count = len(content)
        word_count = len(content.split())
        line_count = len(content.split('\n'))

        col1, col2, col3 = st.columns(3)
        col1.metric("字符数", char_count)
        col2.metric("单词数", word_count)
        col3.metric("行数", line_count)

        # 文本下载功能
        st.download_button(
            label="下载文本",
            data=content,
            file_name="document.txt",
            mime="text/plain"
        )