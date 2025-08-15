import os
import tempfile

def save_uploaded_file(uploaded_file):
    """将 Streamlit 上传的文件保存到临时目录，返回文件路径"""
    if uploaded_file is None:
        return None
    temp_dir = tempfile.mkdtemp()
    file_path = os.path.join(temp_dir, uploaded_file.name)
    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())
    return file_path