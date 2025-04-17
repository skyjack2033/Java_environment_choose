# Java环境管理工具

这是一个用于管理Windows系统上Java环境的工具，可以自动检测、安装、卸载和切换Java版本。

## 功能特点

- 自动检测系统中已安装的Java版本
- 支持安装多个Java版本（8/11/17/21）
- 支持多个Java发行商（OpenJDK/Amazon Corretto/Eclipse Temurin）
- 自动配置环境变量
- 支持卸载Java
- 支持切换当前使用的Java版本

## 使用方法

1. 下载并运行 `Java环境管理工具.exe`
2. 在菜单中选择需要的操作：
   - 1: 检测已安装的Java
   - 2: 安装新的Java版本
   - 3: 卸载Java
   - 4: 切换Java版本
   - 5: 退出程序

## 注意事项

1. 请以管理员身份运行程序
2. 安装或卸载Java时需要管理员权限
3. 切换Java版本后需要重新打开命令行窗口
4. 建议在安装新版本前先检测当前安装的Java

## 系统要求

- Windows 10 或更高版本
- 管理员权限
- 至少2GB可用磁盘空间

## 开发者信息

如需修改或重新打包程序：

1. 安装依赖：
```bash
pip install -r requirements.txt
```

2. 运行打包脚本：
```bash
python build.py
```

打包后的程序将位于 `dist` 目录中。

## 许可证

本项目采用 GNU General Public License v3.0 (GPL-3.0) 许可证。

完整许可证文本请参见 [LICENSE](LICENSE) 文件。

### 许可证摘要

- 您可以自由地运行、复制、分发、研究、修改和改进本软件
- 您必须保留原始版权声明和许可证
- 如果您分发修改后的版本，必须使用相同的许可证
- 本软件按"原样"提供，不提供任何形式的担保

更多信息请访问 [GNU GPL v3 官方网站](https://www.gnu.org/licenses/gpl-3.0.html) 