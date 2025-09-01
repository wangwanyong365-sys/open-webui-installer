# Open WebUI 安装工具

一个用于简化 Open WebUI 安装和管理的自动化脚本工具。

## 功能特性

- 🚀 多种安装方式：pip、Docker、Docker with GPU、Docker with Ollama
- 🔄 一键更新功能
- 📝 自动错误日志记录
- 🖥️ 跨平台支持 (Windows/Linux/macOS)
- ⚡ 快速启动和配置

## 安装方式

### 方法一：使用安装脚本 (推荐)

运行 `install.bat` (Windows) 或直接执行：
```bash
python install_openwebui.py
```

### 方法二：手动安装

1. **pip 安装** (推荐):
   ```bash
   pip install open-webui
   ```

2. **Docker 安装**:
   ```bash
   docker run -d -p 3000:8080 --add-host=host.docker.internal:host-gateway -v open-webui:/app/backend/data --name open-webui --restart always ghcr.io/open-webui/open-webui:main
   ```

## 启动方式

### 使用启动脚本
运行 `run server.bat` 启动服务，然后运行 `start open webui.bat` 打开浏览器。

### 手动启动
```bash
# 启动服务
open-webui serve

# 访问地址
http://localhost:8080
```

## 系统要求

- Python 3.11+ (推荐)
- Docker (用于Docker安装方式)
- 支持CUDA的GPU (用于GPU加速)

## 支持的安装选项

1. **Pip安装** - 标准Python包安装
2. **Docker标准版** - 使用官方Docker镜像
3. **Docker GPU版** - 支持NVIDIA GPU加速
4. **Docker + Ollama (CPU)** - 包含Ollama本地模型
5. **Docker + Ollama (GPU)** - Ollama + GPU加速

## 更新方法

运行安装脚本并选择"更新Open WebUI"选项，或手动执行：
```bash
pip install --upgrade open-webui
```

## 故障排除

- 安装失败时会在当前目录生成 `openwebui_install.log` 日志文件
- 确保网络连接正常
- Docker安装需要先安装Docker Desktop

## 访问地址

- Pip安装: http://localhost:8080
- Docker安装: http://localhost:3000

## 许可证

MIT License