# Java环境管理工具 v1.0.0

这是Java环境管理工具的首个正式版本，提供了完整的Java环境管理功能。

## 使用限制声明

### 使用范围
- 本工具仅供个人学习交流使用
- 禁止用于商业用途
- 禁止用于生产环境
- 禁止用于任何可能造成系统风险的环境

### 法律风险提示
- 使用本工具可能涉及系统环境变量的修改，存在系统稳定性风险
- 安装第三方 Java 发行版可能涉及许可协议合规性问题
- 在非个人学习环境使用可能违反相关许可协议
- 因使用本工具导致的任何法律纠纷由使用者自行承担

## 法律声明

### 商标声明
- Java 是 Oracle 和/或其附属公司的注册商标
- OpenJDK 是 Oracle 和/或其附属公司的商标
- Amazon Corretto 是 Amazon.com, Inc. 或其附属公司的商标
- Eclipse Temurin 是 Eclipse Foundation 的商标
- Windows 是 Microsoft Corporation 的注册商标

### 许可证说明
- 本工具本身采用 GNU General Public License v3.0 (GPL-3.0) 许可证发布
- 通过本工具安装的 Java 发行版受各自供应商的许可条款约束
- 如果您修改了本工具的源代码并分发，必须：
  - 使用相同的 GPL v3 许可证
  - 提供修改后的源代码
  - 保留原始版权声明

### 第三方软件许可
本工具使用以下第三方库：
- PyInstaller: GPL v2
- requests: Apache License 2.0
- 其他依赖项请参见 requirements.txt

### 隐私政策
- 本工具不会收集、存储或传输任何用户数据
- 网络连接仅用于下载 Java 安装包和验证版本信息
- 所有下载操作都直接连接到官方源，不经过中间服务器
- 不会记录用户的操作日志或系统信息

### 免责声明
- 本工具仅作为 Java 环境管理工具提供
- 不对通过本工具安装的 Java 发行版的功能、安全性或兼容性提供任何保证
- 建议用户直接从官方渠道下载 Java 发行版
- 使用本工具的风险由用户自行承担
- 不对因使用本工具导致的系统问题、数据丢失或业务中断负责
- 不保证与所有 Windows 版本完全兼容
- 保留随时修改或终止服务的权利

## 主要功能

- ✨ 自动检测系统中已安装的Java版本
- 📥 支持安装多个Java版本（8/11/17/21）
- 🔄 支持多个Java发行商（OpenJDK/Amazon Corretto/Eclipse Temurin）
- ⚙️ 自动配置环境变量
- 🗑️ 支持卸载Java
- 🔄 支持切换当前使用的Java版本

## 系统要求

- Windows 10 或更高版本
- 管理员权限
- 至少2GB可用磁盘空间
- 稳定的网络连接（用于下载Java安装包）

## 安装说明

1. 下载 `Java环境管理工具.exe`
2. 以管理员身份运行程序
3. 根据菜单提示进行操作

## 使用指南

### 检测Java版本
1. 运行程序
2. 选择选项 1
3. 程序将显示所有已安装的Java版本

### 安装新版本
1. 运行程序
2. 选择选项 2
3. 选择要安装的Java版本
4. 选择发行商
5. 等待下载和安装完成

### 切换Java版本
1. 运行程序
2. 选择选项 4
3. 选择要使用的Java版本
4. 重新打开命令行窗口使更改生效

### 卸载Java
1. 运行程序
2. 选择选项 3
3. 选择要卸载的Java版本
4. 确认卸载

## 常见问题

### 程序无法运行
- 确保以管理员身份运行
- 检查系统是否满足最低要求
- 确保网络连接正常

### 安装失败
- 检查磁盘空间是否充足
- 确保网络连接稳定
- 尝试重新运行安装程序

### 环境变量未更新
- 重新打开命令行窗口
- 检查系统环境变量设置
- 重启计算机

## 注意事项

- 首次运行时请以管理员身份运行
- 安装或卸载Java时需要管理员权限
- 切换Java版本后需要重新打开命令行窗口
- 建议在安装新版本前先检测当前安装的Java
- 建议定期检查更新以获取最新功能

## 许可证

本软件采用 GNU General Public License v3.0 (GPL-3.0) 许可证发布。

## 反馈与支持

如果您在使用过程中遇到任何问题，或有改进建议，请通过以下方式联系我们：
- 在 GitHub 仓库提交 Issue
- 提交 Pull Request 贡献代码
- 查看项目文档获取更多信息 