try:
    import streamlit as st
except ImportError:
    raise ImportError("请安装streamlit: pip install streamlit")

try:
    import pandas as pd
except ImportError:
    raise ImportError("请安装pandas: pip install pandas")

from .base_visualizer import BaseVisualizer


class TableVisualizer(BaseVisualizer):
    """表格可视化器"""
    def __init__(self, document):
        super().__init__(document)
        
    def visualize(self):
        """可视化表格数据"""
        if not self.document or "tables" not in self.document:
            st.error("没有可可视化的表格数据")
            return

        # 显示元数据
        self.display_metadata()

        # 显示表格数据
        st.subheader("表格数据")
        tables = self.document["tables"]

        if not tables:
            st.info("文档中未找到表格")
            return

        # 选择要显示的表格
        table_index = st.selectbox(
            "选择表格",
            range(len(tables)),
            format_func=lambda i: f"表格 {i+1}"
        )

        selected_table = tables[table_index]
        if not selected_table or len(selected_table) <= 1:
            st.info("选中的表格为空")
            return

        try:
            # 转换为DataFrame
            df = pd.DataFrame(selected_table[1:], columns=selected_table[0])
            st.dataframe(df)

            # 表格统计信息
            st.subheader("表格统计")
            st.write(f"行数: {len(df)}")
            st.write(f"列数: {len(df.columns)}")

            # 下载表格数据
            csv = df.to_csv(index=False)
            st.download_button(
                label="下载表格数据(csv)",
                data=csv,
                file_name=f"table_{table_index+1}.csv",
                mime="text/csv"
            )

            # 简单的数据筛选功能
            st.subheader("数据筛选")
            if len(df.columns) > 0:
                filter_col = st.selectbox("选择筛选列", df.columns)
                if df[filter_col].dtype.kind in 'ifc':  # 数字类型
                    min_val = float(df[filter_col].min())
                    max_val = float(df[filter_col].max())
                    selected_range = st.slider(
                        f"筛选 {filter_col}",
                        min_val, max_val, (min_val, max_val)
                    )
                    filtered_df = df[
                        (df[filter_col] >= selected_range[0]) & 
                        (df[filter_col] <= selected_range[1])
                    ]
                else:  # 非数字类型
                    unique_vals = df[filter_col].unique()
                    selected_vals = st.multiselect(
                        f"筛选 {filter_col}",
                        unique_vals, unique_vals
                    )
                    filtered_df = df[df[filter_col].isin(selected_vals)]

                st.dataframe(filtered_df)
        except Exception as e:
            st.error(f"处理表格数据时出错: {e}")