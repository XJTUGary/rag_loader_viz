from .base_visualizer import BaseVisualizer
from .text_visualizer import TextVisualizer
from .table_visualizer import TableVisualizer
from .chart_visualizer import ChartVisualizer


def get_visualizer(visualizer_type, document):
    """根据可视化器类型获取可视化器实例"""
    if visualizer_type == "文本视图":
        return TextVisualizer(document)
    elif visualizer_type == "表格视图":
        return TableVisualizer(document)
    elif visualizer_type == "图表视图":
        return ChartVisualizer(document)
    else:
        return None