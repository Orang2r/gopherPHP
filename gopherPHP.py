#!/usr/bin/env python3
import argparse
import os
from urllib.parse import quote

def read_data(input_data):
    """ 读取数据：支持直接输入或文件路径 """
    if os.path.exists(input_data):
        with open(input_data, 'r', encoding='utf-8') as f:
            return f.read()
    return input_data

def convert_to_gopher(host, port, data, encode_level=1):
    """
    转换TCP数据到Gopher协议格式
    :param host: 目标IP/域名
    :param port: 目标端口
    :param data: 原始TCP数据（支持文件路径或原始字符串）
    :param encode_level: 编码次数（1=file_get_contents，2=curl）
    :return: Gopher URL
    """
    # 读取数据（文件或直接输入）
    raw_data = read_data(data)
    
    # 标准化换行符为CRLF并强制末尾终止符
    processed_data = raw_data.replace('\n', '\r\n').replace('\r\r', '\r')
    if not processed_data.endswith('\r\n'):
        processed_data += '\r\n'
    
    # URL编码处理
    encoded_data = quote(processed_data, safe='')
    
    # 二次编码（针对curl）
    for _ in range(encode_level - 1):
        encoded_data = quote(encoded_data, safe='')
    
    # 构建完整URL
    return f"gopher://{host}:{port}/_{encoded_data}"

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Gopher协议生成工具 - 支持文件输入',
        formatter_class=argparse.RawTextHelpFormatter
    )
    parser.add_argument('--host', required=True, help='目标地址')
    parser.add_argument('--port', type=int, default=70, help='目标端口（默认70）')
    parser.add_argument('--data', required=True, help='''原始TCP数据，支持：
1. 直接输入（使用\\n换行）
2. 文件路径（如 /path/to/request.txt）''')
    parser.add_argument('--type', choices=['curl', 'file'], required=True,
                       help='生成类型：curl（二次编码）或file（一次编码）')

    args = parser.parse_args()
    
    try:
        encode_level = 2 if args.type == 'curl' else 1
        gopher_url = convert_to_gopher(
            host=args.host,
            port=args.port,
            data=args.data,
            encode_level=encode_level
        )
        
        print(f"Generated Gopher URL ({args.type} compatible):")
        print(gopher_url)
    except Exception as e:
        print(f"Error: {str(e)}")
        exit(1)
