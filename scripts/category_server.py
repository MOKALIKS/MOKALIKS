#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import rospy
import yaml
from mokaliks_service.srv import QueryCategory, QueryCategoryResponse


def load_db(db_path):
    if not os.path.exists(db_path):
        rospy.logwarn("数据库文件不存在: %s", db_path)
        return {}
    with open(db_path, 'r', encoding='utf-8') as f:
        data = yaml.safe_load(f) or {}
    return {str(k).strip(): str(v).strip() for k, v in data.items()}


class CategoryServer:
    def __init__(self):
        rospy.init_node('category_server')
        default_db = os.path.join(
            os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
            'config',
            'item_category_db.yaml'
        )
        db_path = rospy.get_param('~db_path', default_db)
        self.db = load_db(db_path)
        rospy.Service('query_category', QueryCategory, self.handle_query)
        rospy.loginfo('服务已启动，数据库条目数: %d', len(self.db))

    def handle_query(self, req):
        item = req.item.strip()
        category = self.db.get(item)
        if category is None:
            return QueryCategoryResponse(False, '', f"未找到物品: {item}")
        return QueryCategoryResponse(True, category, f"物品 {item} 的包裹类别是 {category}")


if __name__ == '__main__':
    CategoryServer()
    rospy.spin()
