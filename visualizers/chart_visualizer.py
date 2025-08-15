try:
    import streamlit as st
except ImportError:
    raise ImportError("请安装streamlit: pip install streamlit")

try:
    import matplotlib.pyplot as plt
except ImportError:
    raise ImportError("请安装matplotlib: pip install matplotlib")

try:
    import seaborn as sns
except ImportError:
    raise ImportError("请安装seaborn: pip install seaborn")

try:
    import pandas as pd
except ImportError:
    raise ImportError("请安装pandas: pip install pandas")

try:
    import numpy as np
except ImportError:
    raise ImportError("请安装numpy: pip install numpy")

import re

from visualizers.base_visualizer import BaseVisualizer


class ChartVisualizer(BaseVisualizer):
    """图表可视化器"""
    def __init__(self, document):
        super().__init__(document)
        
    def visualize(self):
        """可视化图表数据"""
        if not self.document or "content" not in self.document:
            st.error("没有可可视化的内容")
            return

        # 显示元数据
        self.display_metadata()

        # 准备数据
        content = self.document["content"]

        st.subheader("图表可视化")

        # 选择图表类型
        chart_type = st.selectbox(
            "选择图表类型",
            ["词频分布", "文本长度分布", "自定义数据可视化"]
        )

        if chart_type == "词频分布":
            # 词频分布图表
            words = re.findall(r'\b\w+\b', content.lower())
            stop_words = set(["the", "and", "is", "in", "to", "of", "for", "with", "on", "at", "by", "from", "up", "about", "like", "that", "this", "but", "or", "as", "what", "when", "where", "how", "who", "which", "it", "we", "you", "they", "he", "she", "i", "me", "my", "your", "his", "her", "its", "our", "their", "a", "an", "the"])
            filtered_words = [word for word in words if word not in stop_words and len(word) > 3]
            word_freq = {}
            for word in filtered_words:
                if word in word_freq:
                    word_freq[word] += 1
                else:
                    word_freq[word] = 1
            sorted_words = sorted(word_freq.items(), key=lambda x: x[1], reverse=True)[:20]

            if sorted_words:
                words, freqs = zip(*sorted_words)
                plt.figure(figsize=(12, 8))
                sns.barplot(x=list(freqs), y=list(words))
                plt.title("词频分布")
                plt.xlabel("频率")
                plt.ylabel("单词")
                st.pyplot(plt.gcf())
                plt.close()
            else:
                st.info("未能提取到足够的单词进行词频分析")

        elif chart_type == "文本长度分布":
            # 文本长度分布图表
            lines = content.split('\n')
            lines = [line for line in lines if line.strip()]
            line_lengths = [len(line) for line in lines]

            if line_lengths:
                plt.figure(figsize=(10, 6))
                sns.histplot(line_lengths, kde=True)
                plt.title("文本行长度分布")
                plt.xlabel("行长度")
                plt.ylabel("频率")
                st.pyplot(plt.gcf())
                plt.close()
            else:
                st.info("文本内容为空或只有空行")

        elif chart_type == "自定义数据可视化":
            st.info("此功能允许您从文本中提取数据并创建自定义图表")

            if "tables" in self.document and self.document["tables"]:
                table_index = st.selectbox(
                    "选择要可视化的表格",
                    range(len(self.document["tables"])),
                    format_func=lambda i: f"表格 {i+1}"
                )
                selected_table = self.document["tables"][table_index]
                if selected_table and len(selected_table) > 1:
                    try:
                        df = pd.DataFrame(selected_table[1:], columns=selected_table[0])
                        st.dataframe(df)

                        # 选择X和Y轴
                        numeric_cols = []
                        for col in df.columns:
                            try:
                                df[col] = pd.to_numeric(df[col])
                                numeric_cols.append(col)
                            except:
                                pass

                        if len(numeric_cols) >= 2:
                            x_col = st.selectbox("选择X轴数据", numeric_cols)
                            y_col = st.selectbox("选择Y轴数据", [col for col in numeric_cols if col != x_col])

                            # 选择图表类型
                            plot_type = st.selectbox(
                                "选择图表类型",
                                ["散点图", "折线图", "柱状图"]
                            )

                            plt.figure(figsize=(10, 6))
                            if plot_type == "散点图":
                                sns.scatterplot(data=df, x=x_col, y=y_col)
                            elif plot_type == "折线图":
                                sns.lineplot(data=df, x=x_col, y=y_col)
                            elif plot_type == "柱状图":
                                sns.barplot(data=df, x=x_col, y=y_col)
                            plt.title(f"{plot_type}: {x_col} vs {y_col}")
                            st.pyplot(plt.gcf())
                            plt.close()
                        else:
                            st.info("表格中至少需要两列数值数据才能创建图表")
                    except Exception as e:
                        st.error(f"处理表格数据失败: {e}")
                else:
                    st.info("选中的表格为空或只有表头")
            else:
                st.info("文档中没有表格数据可供可视化")