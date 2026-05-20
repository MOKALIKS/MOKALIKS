#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import rospy
from mokaliks_service.srv import QueryCategory


def main():
    rospy.init_node('category_client')
    rospy.wait_for_service('query_category')
    query = rospy.ServiceProxy('query_category', QueryCategory)

    if len(sys.argv) > 1:
        item = sys.argv[1]
    else:
        item = input('请输入要查询的物品名称: ').strip()

    try:
        resp = query(item)
        if resp.found:
            print(f"查询成功: {item} -> {resp.category}")
        else:
            print(f"查询失败: {resp.message}")
    except rospy.ServiceException as e:
        print(f"服务调用失败: {e}")


if __name__ == '__main__':
    main()
