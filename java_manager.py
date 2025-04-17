import os
import subprocess
import winreg
import requests
import zipfile
import io
import shutil
from pathlib import Path

class JavaManager:
    def __init__(self):
        self.java_installations = []
        self.java_home = os.environ.get('JAVA_HOME', '')
        self.java_versions = {
            '8': {
                'OpenJDK': 'https://github.com/adoptium/temurin8-binaries/releases/download/jdk8u412-b08/OpenJDK8U-jdk_x64_windows_hotspot_8u412b08.zip',
                'Amazon Corretto': 'https://corretto.aws/downloads/latest/amazon-corretto-8-x64-windows-jdk.zip',
                'Eclipse Temurin': 'https://github.com/adoptium/temurin8-binaries/releases/download/jdk8u412-b08/OpenJDK8U-jdk_x64_windows_hotspot_8u412b08.zip'
            },
            '11': {
                'OpenJDK': 'https://github.com/adoptium/temurin11-binaries/releases/download/jdk-11.0.21%2B9/OpenJDK11U-jdk_x64_windows_hotspot_11.0.21_9.zip',
                'Amazon Corretto': 'https://corretto.aws/downloads/latest/amazon-corretto-11-x64-windows-jdk.zip',
                'Eclipse Temurin': 'https://github.com/adoptium/temurin11-binaries/releases/download/jdk-11.0.21%2B9/OpenJDK11U-jdk_x64_windows_hotspot_11.0.21_9.zip'
            },
            '17': {
                'OpenJDK': 'https://github.com/adoptium/temurin17-binaries/releases/download/jdk-17.0.9%2B9/OpenJDK17U-jdk_x64_windows_hotspot_17.0.9_9.zip',
                'Amazon Corretto': 'https://corretto.aws/downloads/latest/amazon-corretto-17-x64-windows-jdk.zip',
                'Eclipse Temurin': 'https://github.com/adoptium/temurin17-binaries/releases/download/jdk-17.0.9%2B9/OpenJDK17U-jdk_x64_windows_hotspot_17.0.9_9.zip'
            },
            '21': {
                'OpenJDK': 'https://github.com/adoptium/temurin21-binaries/releases/download/jdk-21.0.1%2B12/OpenJDK21U-jdk_x64_windows_hotspot_21.0.1_12.zip',
                'Amazon Corretto': 'https://corretto.aws/downloads/latest/amazon-corretto-21-x64-windows-jdk.zip',
                'Eclipse Temurin': 'https://github.com/adoptium/temurin21-binaries/releases/download/jdk-21.0.1%2B12/OpenJDK21U-jdk_x64_windows_hotspot_21.0.1_12.zip'
            }
        }

    def detect_java_installations(self):
        """检测系统中已安装的Java版本"""
        self.java_installations = []
        
        # 检查JAVA_HOME
        if self.java_home and os.path.exists(self.java_home):
            version = self._get_java_version(self.java_home)
            if version:
                self.java_installations.append({
                    'path': self.java_home,
                    'version': version
                })

        # 检查Program Files中的Java安装
        program_files = os.environ.get('ProgramFiles', 'C:\\Program Files')
        java_dirs = [
            os.path.join(program_files, 'Java'),
            os.path.join(program_files, 'Eclipse Adoptium'),
            os.path.join(program_files, 'Eclipse Foundation'),
            os.path.join(program_files, 'AdoptOpenJDK'),
            os.path.join(program_files, 'Amazon Corretto'),
            os.path.join(program_files, 'Microsoft'),
        ]

        for java_dir in java_dirs:
            if os.path.exists(java_dir):
                for item in os.listdir(java_dir):
                    full_path = os.path.join(java_dir, item)
                    if os.path.isdir(full_path):
                        java_exe = os.path.join(full_path, 'bin', 'java.exe')
                        if os.path.exists(java_exe):
                            version = self._get_java_version(full_path)
                            if version:
                                self.java_installations.append({
                                    'path': full_path,
                                    'version': version
                                })

    def _get_java_version(self, java_path):
        """获取指定Java安装的版本"""
        try:
            java_exe = os.path.join(java_path, 'bin', 'java.exe')
            if not os.path.exists(java_exe):
                return None
            result = subprocess.run([java_exe, '-version'], capture_output=True, text=True)
            version_line = result.stderr.split('\n')[0]
            return version_line.split('"')[1]
        except:
            return None

    def install_java(self):
        """安装Java"""
        print("\n可用的Java版本:")
        for version in self.java_versions.keys():
            print(f"- Java {version}")
        
        version = input("\n请选择要安装的Java版本 (8/11/17/21): ")
        if version not in self.java_versions:
            print("无效的版本选择！")
            return
            
        print("\n可用的发行商:")
        vendors = list(self.java_versions[version].keys())
        for i, vendor in enumerate(vendors, 1):
            print(f"{i}. {vendor}")
            
        try:
            vendor_choice = int(input("\n请选择发行商 (1-3): ")) - 1
            if vendor_choice < 0 or vendor_choice >= len(vendors):
                print("无效的发行商选择！")
                return
                
            vendor = vendors[vendor_choice]
            download_url = self.java_versions[version][vendor]
            
            print(f"\n开始下载 Java {version} ({vendor})...")
            try:
                # 创建临时目录
                temp_dir = os.path.join(os.environ.get('TEMP', 'C:\\Windows\\Temp'), 'java_install')
                os.makedirs(temp_dir, exist_ok=True)
                
                # 显示下载进度
                print("正在下载... (这可能需要几分钟，请耐心等待)")
                response = requests.get(download_url, stream=True)
                response.raise_for_status()  # 检查HTTP错误
                
                # 获取文件大小
                total_size = int(response.headers.get('content-length', 0))
                block_size = 1024  # 1 KB
                downloaded = 0
                
                # 下载文件
                temp_file = os.path.join(temp_dir, 'java.zip')
                with open(temp_file, 'wb') as f:
                    for data in response.iter_content(block_size):
                        downloaded += len(data)
                        f.write(data)
                        # 显示下载进度
                        if total_size > 0:
                            percent = (downloaded / total_size) * 100
                            print(f"\r下载进度: {percent:.1f}% ({downloaded}/{total_size} bytes)", end='')
                
                print("\n下载完成，开始安装...")
                
                # 解压文件
                install_dir = os.path.join(os.environ.get('ProgramFiles', 'C:\\Program Files'), 'Java')
                os.makedirs(install_dir, exist_ok=True)
                
                with zipfile.ZipFile(temp_file, 'r') as zip_ref:
                    zip_ref.extractall(install_dir)
                
                # 清理临时文件
                os.remove(temp_file)
                os.rmdir(temp_dir)
                
                # 获取解压后的目录名
                extracted_dir = os.path.join(install_dir, os.listdir(install_dir)[0])
                
                # 设置环境变量
                self._set_environment_variables(extracted_dir)
                print(f"Java {version} ({vendor}) 安装完成！安装路径: {extracted_dir}")
                
            except requests.exceptions.RequestException as e:
                print(f"\n下载失败！错误信息: {str(e)}")
                print("可能的原因：")
                print("1. 网络连接问题")
                print("2. 下载链接失效")
                print("3. 服务器暂时不可用")
                print("\n请检查网络连接后重试，或选择其他版本/发行商。")
            except zipfile.BadZipFile:
                print("\n下载的文件已损坏，请重试。")
            except Exception as e:
                print(f"\n安装过程中出错: {str(e)}")
                print("请确保：")
                print("1. 以管理员身份运行此程序")
                print("2. 有足够的磁盘空间")
                print("3. 目标目录有写入权限")
        except ValueError:
            print("请输入有效的数字！")

    def _set_environment_variables(self, java_path):
        """设置Java环境变量"""
        try:
            # 设置JAVA_HOME
            with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, 
                              'SYSTEM\\CurrentControlSet\\Control\\Session Manager\\Environment',
                              0, winreg.KEY_ALL_ACCESS) as key:
                winreg.SetValueEx(key, 'JAVA_HOME', 0, winreg.REG_SZ, java_path)
            
            # 更新Path
            with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, 
                              'SYSTEM\\CurrentControlSet\\Control\\Session Manager\\Environment',
                              0, winreg.KEY_ALL_ACCESS) as key:
                path_value, _ = winreg.QueryValueEx(key, 'Path')
                new_path = f"{path_value};{os.path.join(java_path, 'bin')}"
                winreg.SetValueEx(key, 'Path', 0, winreg.REG_SZ, new_path)
            
            print("环境变量设置完成！")
        except Exception as e:
            print(f"设置环境变量时出错: {str(e)}")

    def uninstall_java(self, java_path):
        """卸载Java"""
        try:
            if not java_path:
                print("错误：未指定Java路径！")
                return
                
            if not os.path.exists(java_path):
                print(f"错误：指定的Java路径不存在: {java_path}")
                print("请检查路径是否正确，或使用选项1重新检测已安装的Java版本。")
                return
                
            # 检查是否是有效的Java安装目录
            java_exe = os.path.join(java_path, 'bin', 'java.exe')
            if not os.path.exists(java_exe):
                print(f"错误：指定的路径不是有效的Java安装目录: {java_path}")
                return
                
            # 确认卸载
            confirm = input(f"确定要卸载Java (版本: {self._get_java_version(java_path)}) 吗？(y/n): ")
            if confirm.lower() != 'y':
                print("取消卸载操作。")
                return
                
            # 在卸载前检查其他可用的Java安装
            other_java_installations = []
            for installation in self.java_installations:
                if installation['path'] != java_path and os.path.exists(installation['path']):
                    other_java_installations.append(installation)
            
            # 执行卸载
            shutil.rmtree(java_path)
            print(f"已成功卸载Java: {java_path}")
            
            # 如果卸载的是当前JAVA_HOME，尝试配置其他可用的Java
            if java_path == self.java_home:
                if other_java_installations:
                    print("\n检测到其他Java安装，正在自动配置环境变量...")
                    # 选择最新的Java版本
                    latest_java = max(other_java_installations, key=lambda x: x['version'])
                    self._set_environment_variables(latest_java['path'])
                    print(f"已自动配置环境变量到: {latest_java['path']} (版本: {latest_java['version']})")
                else:
                    print("\n警告：系统中没有其他Java安装！")
                    print("建议立即安装新的Java版本，否则Java相关程序可能无法运行。")
                    self._clear_environment_variables()
        except PermissionError:
            print("错误：没有足够的权限卸载Java。请以管理员身份运行此程序。")
        except Exception as e:
            print(f"卸载过程中出错: {str(e)}")

    def _clear_environment_variables(self):
        """清除Java环境变量"""
        try:
            with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, 
                              'SYSTEM\\CurrentControlSet\\Control\\Session Manager\\Environment',
                              0, winreg.KEY_ALL_ACCESS) as key:
                winreg.DeleteValue(key, 'JAVA_HOME')
                
                # 从Path中移除Java路径
                path_value, _ = winreg.QueryValueEx(key, 'Path')
                new_path = ';'.join([p for p in path_value.split(';') 
                                   if 'Java' not in p and 'java' not in p])
                winreg.SetValueEx(key, 'Path', 0, winreg.REG_SZ, new_path)
            
            print("环境变量已清除！")
        except Exception as e:
            print(f"清除环境变量时出错: {str(e)}")

    def switch_java_version(self):
        """切换当前使用的Java版本"""
        self.detect_java_installations()
        if not self.java_installations:
            print("未检测到Java安装！")
            return
            
        print("\n已安装的Java版本:")
        for i, java in enumerate(self.java_installations, 1):
            current = "(当前使用)" if java['path'] == self.java_home else ""
            print(f"{i}. {java['path']} (版本: {java['version']}) {current}")
            
        try:
            choice = int(input("\n请选择要使用的Java版本 (输入编号): ")) - 1
            if 0 <= choice < len(self.java_installations):
                selected_java = self.java_installations[choice]
                self._set_environment_variables(selected_java['path'])
                print(f"\n已切换到Java版本: {selected_java['version']}")
                print(f"安装路径: {selected_java['path']}")
            else:
                print("无效的选择！")
        except ValueError:
            print("请输入有效的数字！")

def main():
    manager = JavaManager()
    while True:
        print("\nJava环境管理工具")
        print("1. 检测已安装的Java")
        print("2. 安装Java")
        print("3. 卸载Java")
        print("4. 切换Java版本")
        print("5. 退出")
        
        choice = input("请选择操作 (1-5): ")
        
        if choice == '1':
            manager.detect_java_installations()
            if manager.java_installations:
                print("\n已安装的Java版本:")
                for i, java in enumerate(manager.java_installations, 1):
                    current = "(当前使用)" if java['path'] == manager.java_home else ""
                    print(f"{i}. 路径: {java['path']}")
                    print(f"   版本: {java['version']} {current}")
            else:
                print("未检测到Java安装！")
                
        elif choice == '2':
            manager.install_java()
            
        elif choice == '3':
            manager.detect_java_installations()
            if manager.java_installations:
                print("\n请选择要卸载的Java版本:")
                for i, java in enumerate(manager.java_installations, 1):
                    current = "(当前使用)" if java['path'] == manager.java_home else ""
                    print(f"{i}. {java['path']} (版本: {java['version']}) {current}")
                try:
                    uninstall_choice = int(input("请输入要卸载的Java编号: ")) - 1
                    if 0 <= uninstall_choice < len(manager.java_installations):
                        manager.uninstall_java(manager.java_installations[uninstall_choice]['path'])
                    else:
                        print("无效的选择！")
                except ValueError:
                    print("请输入有效的数字！")
            else:
                print("未检测到Java安装！")
                
        elif choice == '4':
            manager.switch_java_version()
                
        elif choice == '5':
            print("感谢使用！")
            break
            
        else:
            print("无效的选择，请重试！")

if __name__ == "__main__":
    main() 