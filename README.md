# Gopher Protocol Payload Generator 🔌

**专为SSRF攻击设计的Gopher协议Payload生成工具**，支持快速生成针对Redis/MySQL/HTTP等服务的攻击命令，助你高效测试内网漏洞。

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
![Python 3.6+](https://img.shields.io/badge/Python-3.6%2B-blue.svg)

## 🚀 核心功能

- **SSRF攻击利器**  
  生成可直接用于SSRF漏洞的Gopher协议URL，绕过`file`/`http`协议限制
- **多协议支持**  
  支持Redis未授权访问、MySQL恶意查询、HTTP请求伪造等攻击场景
- **智能编码**  
  自动处理`CRLF`终止符和特殊字符编码，适配`curl`和`file_get_contents`
- **文件输入**  
  支持从`.txt`文件读取复杂TCP数据（如HTTP请求头、Redis命令流）

## 📦 快速安装

```bash
git clone https://github.com/yourrepo/gopher-ssrf-generator.git
cd gopher-ssrf-generator
pip3 install -r requirements.txt
