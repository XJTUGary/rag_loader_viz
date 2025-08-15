import streamlit as st
import os
import logging
from loaders import get_loader
from visualizers import get_visualizer

# 配置日志
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# 设置页面配置
st.set_page_config(
    page_title="文档加载器可视化工具",
    page_icon="📚",
    layout="wide"
)

# 页面标题
st.title("文档加载器可视化工具")

# 侧边栏 - 上传文件
with st.sidebar:
    st.header("上传文档")
    uploaded_file = st.file_uploader("选择文件", type=["txt", "pdf", "docx"])

    st.header("加载器设置")
    loader_type = st.selectbox(
        "选择加载器",
        ["自动检测", "文本加载器", "PDF加载器", "Word加载器"]
    )

    st.header("可视化设置")
    visualizer_type = st.selectbox(
        "选择可视化方式",
        ["自动选择", "文本视图", "表格视图", "图表视图"]
    )

# 主内容区
if uploaded_file is not None:
    # 显示文件信息
    st.subheader("文件信息")
    file_info = {
        "文件名": uploaded_file.name,
        "文件大小": f"{uploaded_file.size / 1024:.2f} KB",
        "文件类型": uploaded_file.type
    }
    st.json(file_info)

    # 保存上传的文件到临时目录
    temp_dir = "temp"
    os.makedirs(temp_dir, exist_ok=True)
    file_path = os.path.join(temp_dir, uploaded_file.name)

    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    # 选择加载器
    st.subheader("加载文档")
    if st.button("加载文档"):
        with st.spinner("正在加载文档..."):
            # 获取加载器实例
            loader = get_loader(loader_type, file_path)
            if loader:
                # 加载文档
                document = loader.load()
                logger.info(f"成功加载文档: {document}")
                st.success("文档加载成功!")

                # 选择可视化器
                st.subheader("可视化结果")
                visualizer = get_visualizer(visualizer_type, document)
                if visualizer:
                    with st.spinner("正在生成可视化..."):
                        visualizer.visualize()
                else:
                    st.error("不支持的可视化类型")
            else:
                st.error("不支持的加载器类型")
else:
    st.info("请上传一个文档开始")

# 页脚
st.markdown("---")
st.markdown("文档加载器可视化工具 © 2025")