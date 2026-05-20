# ROS Service 通讯示例（Python）

本仓库实现了 ROS Service 机制：客户端发送物品名称，服务端返回对应包裹类别。

## 1. 服务定义

`srv/QueryCategory.srv`

- 请求：`string item`
- 响应：
  - `bool found`
  - `string category`
  - `string message`

## 2. 数据库

`config/item_category_db.yaml` 内置题目给定映射：
- 日用品：衣服、牙刷、卫生纸
- 水果：香蕉、苹果、橘子
- 家电：电视机、冰箱、空调

## 3. 编译

在 catkin 工作空间中：

```bash
catkin_make
source devel/setup.bash
```

## 4. 运行

启动 roscore 后分别运行：

```bash
rosrun mokaliks_service category_server.py
rosrun mokaliks_service category_client.py 香蕉
```

示例输出：

```text
查询成功: 香蕉 -> 水果
```

未知物品示例：

```bash
rosrun mokaliks_service category_client.py 电脑
```

输出：

```text
查询失败: 未找到物品: 电脑
```
