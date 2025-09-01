#!/usr/bin/env python3
"""
Open WebUI 自动安装脚本
支持多种安装方式：pip安装、Docker安装、Docker with GPU支持等
"""

import os
import sys
import subprocess
import platform
from pathlib import Path

def run_command(command, check=True, capture_output=False):
    """运行系统命令"""
    try:
        result = subprocess.run(command, shell=True, check=check, 
                              capture_output=capture_output, text=True)
        if capture_output:
            return result.stdout.strip()
        return True
    except subprocess.CalledProcessError as e:
        print(f"命令执行失败: {e}")
        return False

def check_docker():
    """检查Docker是否安装"""
    try:
        subprocess.run("docker --version", shell=True, check=True, 
                      capture_output=True)
        return True
    except subprocess.CalledProcessError:
        return False

def check_python_version():
    """检查Python版本是否为3.11"""
    return sys.version_info.major == 3 and sys.version_info.minor == 11

def install_via_pip():
    """通过pip安装Open WebUI"""
    print("正在通过pip安装Open WebUI...")
    
    if not check_python_version():
        print("警告: 推荐使用Python 3.11以避免兼容性问题")
        
    if run_command("pip install open-webui"):
        print("✓ Open WebUI 安装成功!")
        print("\n启动命令:")
        print("  open-webui serve")
        print("\n访问地址: http://localhost:8080")
        return True
    return False

def install_via_docker(option):
    """通过Docker安装Open WebUI"""
    if not check_docker():
        print("错误: 未找到Docker, 请先安装Docker")
        return False
    
    commands = {
        1: "docker run -d -p 3000:8080 --add-host=host.docker.internal:host-gateway -v open-webui:/app/backend/data --name open-webui --restart always ghcr.io/open-webui/open-webui:main",
        2: "docker run -d -p 3000:8080 --gpus all --add-host=host.docker.internal:host-gateway -v open-webui:/app/backend/data --name open-webui --restart always ghcr.io/open-webui/open-webui:cuda",
        3: "docker run -d -p 3000:8080 -v ollama:/root/.ollama -v open-webui:/app/backend/data --name open-webui --restart always ghcr.io/open-webui/open-webui:ollama",
        4: "docker run -d -p 3000:8080 --gpus=all -v ollama:/root/.ollama -v open-webui:/app/backend/data --name open-webui --restart always ghcr.io/open-webui/open-webui:ollama"
    }
    
    command = commands.get(option)
    if command:
        print(f"正在执行Docker命令: {command}")
        if run_command(command):
            print("✓ Open WebUI Docker容器启动成功!")
            print("\n访问地址: http://localhost:3000")
            return True
    return False

def update_openwebui():
    """更新Open WebUI"""
    print("正在更新Open WebUI...")
    
    if run_command("pip install --upgrade open-webui"):
        print("✓ Open WebUI 更新成功!")
        return True
    return False

def save_log(error_message):
    """保存错误日志"""
    log_file = "openwebui_install.log"
    with open(log_file, "a", encoding="utf-8") as f:
        f.write(f"错误时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write(f"错误信息: {error_message}\n")
        f.write("-" * 50 + "\n")
    return log_file

def main():
    """主函数"""
    from datetime import datetime
    
    while True:
        print("=" * 50)
        print("Open WebUI 自动安装脚本")
        print("=" * 50)
        
        print("\n请选择操作:")
        print("1. Pip安装 (推荐)")
        print("2. Docker安装 (标准)")
        print("3. Docker安装 (GPU支持)")
        print("4. Docker安装 (包含Ollama - CPU)")
        print("5. Docker安装 (包含Ollama - GPU)")
        print("6. 更新Open WebUI")
        print("0. 退出")
        
        try:
            choice = int(input("\n请输入选项 (0-6): "))
        except ValueError:
            print("输入无效!")
            continue
        
        if choice == 0:
            print("已退出程序")
            break
        elif choice == 1:
            success = install_via_pip()
        elif choice in [2, 3, 4, 5]:
            success = install_via_docker(choice - 1)
        elif choice == 6:
            success = update_openwebui()
        else:
            print("无效选项!")
            continue
        
        if success:
            print("\n" + "=" * 50)
            print("操作成功!")
            print("=" * 50)
        else:
            error_msg = "操作执行失败"
            log_file = save_log(error_msg)
            print(f"\n操作失败! 错误日志已保存到: {log_file}")
        
        if choice != 0:
            print("\n请选择后续操作:")
            print("1. 返回主菜单")
            print("2. 退出程序")
            
            try:
                next_action = int(input("\n请输入选项 (1-2): "))
                if next_action == 2:
                    print("已退出程序")
                    break
            except ValueError:
                print("输入无效，返回主菜单")
                continue

if __name__ == "__main__":
    main()