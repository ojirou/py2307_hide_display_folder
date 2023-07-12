import os
import subprocess

def show_hidden_folders(folder_paths):
    for folder_path in folder_paths:
        # 指定されたフォルダ内のファイルを取得
        files = os.listdir(folder_path)

        # 隠しフォルダの表示設定を変更するコマンド
        command = f'attrib -h -s "{folder_path}"'
        subprocess.run(command, shell=True, capture_output=True)

        # フォルダ内の隠しフォルダを表示
        for file_name in files:
            file_path = os.path.join(folder_path, file_name)
            if os.path.isdir(file_path) and file_name.startswith('.'):
                command = f'attrib -h -s "{file_path}"'
                subprocess.run(command, shell=True, capture_output=True)

        print(f"{folder_path} 内の隠しフォルダを表示しました。")

# 指定フォルダのパスをリストで設定
folder_paths = [
    r"C:\\Users\\user\\python\\FILE",
    r"C:\\Users\\user\\python\\EXCEL",
    r"C:\\Users\\user\\python\\GUI"
]

# 複数のフォルダに対して隠しフォルダを表示する
show_hidden_folders(folder_paths)