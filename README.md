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
```

## 📌 核心参数说明

### 必选参数
| 参数       | 必选   | 默认值 | 详细说明                                                                 |
|------------|--------|--------|--------------------------------------------------------------------------|
| `--host`   | ✅ 是  | 无     | 目标服务器地址（支持IPv4/IPv6/域名格式）                                 |
| `--data`   | ✅ 是  | 无     | 支持两种输入方式：<br>• 直接输入原始TCP字符串<br>• 指定包含协议数据的文本文件路径 |
| `--type`   | ✅ 是  | 无     | 编码模式选择：<br>• `curl`：双重URL编码<br>• `file`：单层URL编码          |

### 可选参数
| 参数       | 必选   | 默认值 | 扩展说明                                                                 |
|------------|--------|--------|--------------------------------------------------------------------------|
| `--port`   | ❌ 否  | 70     | 根据目标服务指定端口（常用：<br>HTTP-80, Redis-6379, MySQL-3309）        |

---

## 🛠️ 典型使用场景示例

### 案例：CTFHub SSRF POST请求
#### 操作流程
1. **捕获POST请求**
   - 使用Burp Suite拦截POST请求
   - 复制完整TCP数据流（包含Header和Body）保存为`request.txt`
     
![image](https://github.com/user-attachments/assets/614dbfcc-19b4-4c31-9d4e-9f22d6f7d4de)

2. **生成攻击Payload**
   ```bash
   python3 gopher_gen.py \
       --host 127.0.0.1 \
       --port 80 \
       --data request.txt \
       --type curl

![image](https://github.com/user-attachments/assets/66cfc71e-190e-4624-8d4b-af819f106891)

3. **得到flag**
   
![image](https://github.com/user-attachments/assets/56ed43cd-5476-4c33-b180-0aa33d0472ec)
