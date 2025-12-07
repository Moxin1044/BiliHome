#!/usr/bin/env python3
"""
测试BiliHome包的功能
"""

import sys
import os

# 添加当前目录到Python路径，以便导入BiliHome包
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from BiliHome import Bili

def test_bili_fans():
    """测试获取粉丝数量的功能"""
    print("测试BiliHome包...")
    
    # 使用示例中的vmid
    vmid = "8047632"
    
    # 创建Bili实例
    bili_user = Bili(vmid)
    
    # 获取粉丝数量
    fans_count = bili_user.fans()
    
    if fans_count is not None:
        print(f"用户 {vmid} 的粉丝数量: {fans_count}")
        print("测试成功！")
    else:
        print("获取粉丝数量失败，请检查网络连接或vmid是否正确")
    
    # 测试关注数量
    follows_count = bili_user.follows()
    if follows_count is not None:
        print(f"用户 {vmid} 的关注数量: {follows_count}")
        print("测试成功！")
    else:
        print("获取关注数量失败，请检查网络连接或vmid是否正确")

    # 测试用户名
    username = bili_user.name()
    if username is not None:
        print(f"用户 {vmid} 的用户名: {username}")
        print("测试成功！")
    else:
        print("获取用户名失败，请检查网络连接或vmid是否正确")

if __name__ == "__main__":
    test_bili_fans()