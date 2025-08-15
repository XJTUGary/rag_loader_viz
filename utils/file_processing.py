import os
import shutil
from config import TEMP_DIR


def clean_temp_files():
    """清理临时文件"""
    if os.path.exists(TEMP_DIR):
        try:
            shutil.rmtree(TEMP_DIR)
            os.makedirs(TEMP_DIR)
            return True
        except Exception as e:
            print(f"清理临时文件失败: {e}")
            return False
    else:
        return True


def get_file_extension(file_path):
    """获取文件扩展名"""
    return os.path.splitext(file_path)[1].lower()[1:]


def is_supported_file_type(file_path):
    """检查文件类型是否支持"""
    from config import SUPPORTED_FILE_TYPES
    ext = get_file_extension(file_path)
    return ext in SUPPORTED_FILE_TYPES


def get_file_size(file_path):
    """获取文件大小（字节）"""
    if os.path.exists(file_path):
        return os.path.getsize(file_path)
    else:
        return 0


def get_file_size_str(file_path):
    """获取文件大小的字符串表示"""
    size = get_file_size(file_path)
    for unit in ['B', 'KB', 'MB', 'GB']:
        if size < 1024.0:
            return f"{size:.2f} {unit}"
        size /= 1024.0
    return f"{size:.2f} TB"