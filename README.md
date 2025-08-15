# RAG Loader Visualization Tool

这是一个使用Streamlit构建的文档加载器可视化工具，允许用户上传文档，选择不同的加载器，并可视化展示解析结果。

## 项目结构
```
rag_loader_viz/
├── app.py                  # 主应用入口
├── requirements.txt        # 依赖包列表
├── config.py               # 配置文件
├── loaders/                # 加载器模块
│   ├── __init__.py
│   ├── base_loader.py      # 基础加载器类
│   ├── text_loader.py      # 文本文件加载器
│   ├── pdf_loader.py       # PDF文件加载器
│   └── docx_loader.py      # Word文档加载器
├── visualizers/            # 可视化模块
│   ├── __init__.py
│   ├── base_visualizer.py  # 基础可视化类
│   ├── text_visualizer.py  # 文本可视化器
│   ├── table_visualizer.py # 表格可视化器
│   └── chart_visualizer.py # 图表可视化器
└── utils/                  # 工具函数
    ├── __init__.py
    └── file_processing.py  # 文件处理工具
```

## 功能特点
- 支持多种文档格式上传（txt, pdf, docx等）
- 提供多种加载器选择
- 可视化展示文档解析结果
- 交互式界面

## 安装说明
1. 克隆仓库
2. 安装依赖：`pip install -r requirements.txt`
3. 运行应用：`streamlit run app.py`

## 使用说明
1. 上传文档
2. 选择合适的加载器
3. 查看可视化解析结果

## 贡献指南
欢迎提交PR和issue来改进这个工具。