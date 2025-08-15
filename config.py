# 应用配置

# 支持的文件类型
SUPPORTED_FILE_TYPES = ["txt", "pdf", "docx"]

# 临时文件目录
TEMP_DIR = "temp"

# 加载器配置
LOADER_CONFIG = {
    "text": {
        "class": "TextLoader",
        "module": "loaders.text_loader"
    },
    "pdf": {
        "class": "PDFLoader",
        "module": "loaders.pdf_loader"
    },
    "docx": {
        "class": "DocxLoader",
        "module": "loaders.docx_loader"
    }
}

# 可视化器配置
VISUALIZER_CONFIG = {
    "text": {
        "class": "TextVisualizer",
        "module": "visualizers.text_visualizer"
    },
    "table": {
        "class": "TableVisualizer",
        "module": "visualizers.table_visualizer"
    },
    "chart": {
        "class": "ChartVisualizer",
        "module": "visualizers.chart_visualizer"
    }
}