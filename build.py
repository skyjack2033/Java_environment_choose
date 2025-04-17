import PyInstaller.__main__
import os
import shutil

def build():
    # 确保输出目录存在
    if os.path.exists('dist'):
        shutil.rmtree('dist')
    if os.path.exists('build'):
        shutil.rmtree('build')

    # 打包参数
    params = [
        'java_manager.py',  # 主程序
        '--name=Java环境管理工具',  # 程序名称
        '--onefile',  # 打包成单个文件
        '--windowed',  # 使用控制台窗口
        '--add-data=requirements.txt;.',  # 添加依赖文件
        '--clean',  # 清理临时文件
    ]

    # 执行打包
    PyInstaller.__main__.run(params)

    print("\n打包完成！")
    print("可执行文件位于 dist 目录中")

if __name__ == '__main__':
    build() 