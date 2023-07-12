import ctypes
import os
import subprocess

def hide_folders(folder_paths):
    for folder_path in folder_paths:
        # フォルダを隠しフォルダにする
        try:
            attributes = ctypes.windll.kernel32.GetFileAttributesW(folder_path)
            ctypes.windll.kernel32.SetFileAttributesW(folder_path, attributes | 0x02)
            print(f"{folder_path} を隠しフォルダに設定しました。")
        except Exception as e:
            print(f"隠しフォルダに設定できませんでした：{e}")

        # フォルダを非表示にする
        try:
            subprocess.call(['attrib', '+H', '+S', '+R', folder_path], shell=True)
            print(f"{folder_path} を非表示に設定しました。")
        except Exception as e:
            print(f"非表示にできませんでした：{e}")

# 指定フォルダのパスをリストで設定
folder_paths = [
    r"C:\\Users\\user\\python\\FILE",
    r"C:\\Users\\user\\python\\EXCEL",
    r"C:\\Users\\user\\python\\GUI"
]

# 複数のフォルダを隠しフォルダにして非表示にする
hide_folders(folder_paths)