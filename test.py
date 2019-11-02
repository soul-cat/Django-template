# # import pymongo
# # client = pymongo.MongoClient(host='localhost', port=27017)
# # db = client.python
# # collection = db.student
# # stu = {
# #     'name': '李四',
# #     'age': 180
# # }
# # collection.insert_one(stu)
# # rs = collection.find_one({'name': '张三'})
# # print(rs)
#
#
# class BaseMongo(object):
#     @staticmethod
#     def insert_one(collection, data):
#         """直接使用insert() 可以插入一条和插入多条 不推荐 明确区分比较好"""
#         res = collection.insert_one(data)
#         return res.inserted_id
#
#     @staticmethod
#     def insert_many(collection, data_list):
#         res = collection.insert_many(data_list)
#         return res.inserted_ids
#
#     @staticmethod
#     def find_one(collection, data, data_field={}):
#         if len(data_field):
#             res = collection.find_one(data, data_field)
#         else:
#             res = collection.find_one(data)
#         return res
#
#     @staticmethod
#     def find_all(collection):
#         res = collection.find()
#         return res
#
#     @staticmethod
#     def find_many(collection, data, data_field={}):
#         """ data_field 是指输出 操作者需要的字段"""
#         if len(data_field):
#             res = collection.find(data, data_field)
#         else:
#             res = collection.find(data)
#         return res
#
#     @staticmethod
#     def update_one(collection, data_condition, data_set):
#         """修改一条数据"""
#         res = collection.update_one(data_condition, data_set)
#         return res
#
#     @staticmethod
#     def update_many(collection, data_condition, data_set):
#         """ 修改多条数据 """
#         res = collection.update_many(data_condition, data_set)
#         return res
#
#     @staticmethod
#     def delete_many(collection, data):
#         res = collection.delete_many(data)
#         return res
#
#     @staticmethod
#     def delete_one(collection, data):
#         res = collection.delete_one(data)
#         return res
#
# import pymongo
# # client = pymongo.MongoClient(host='localhost', port=27017)
# # db = client.python
# # collection = db.student
# # stu = {
# #     'name': '李四',
# #     'age': 180
# # }
# # collection.insert_one(stu)
# # rs = collection.find_one({'name': '张三'})
# # print(rs)
#
# client = pymongo.MongoClient(host='localhost', port=27017)
# db = client.python
# collection = db.student
# # stu = {
# #     'name': '赵六',
# #     'age': 180
# # }
# # print(BaseMongo.insert_one(collection, stu))
#
# # print(BaseMongo.update_one(collection, {'name': '王五'}, {'$set': {'age': 1}}))
# print(BaseMongo.find_one(collection, {'name': '王五'}))
#
# # print(BaseMongo.delete_one(collection, {'name': '王五'}))
# cur = BaseMongo.find_many(collection, {})
# print(cur)
#
# for stu in cur:
#     print(stu)
#

# radis
import redis
# r = redis.StrictRedis(host='localhost', port=6379, decode_responses=True, password=980304)
# r.set(name='name', value='lisi')
# print(r.lrange('list1', 0, -1))
# print(r.hgetall('hset1'))
# print(r.get('name'))
#
# pipe = r.pipeline()
# pipe.set('name', 'world')
# print(pipe.get('name'))
# pipe.execute()

# from datetime import datetime, date
# import json
#
# class DateToJson(json.JSONEncoder):
#     def default(self, obj):
#         if isinstance(obj, datetime):
#             return obj.strftime('%Y-%m-%d %H:%M:%S')
#         elif isinstance(obj, date):
#             return obj.strftime('%Y-%m-%d')
#         else:
#             return json.JSONEncoder.default(self, obj)
# da = datetime.now()
# dic = {'da': da}
# jsa = json.dumps(dic, cls=DateToJson)
# print(jsa)

# a = [[1, 2], [3, 4], [5, 6]]
# li = [j for i in a for j in i]
# [j i for j in i]

'''
    1,2   3,4   5,6
    

'''
# print(li)

li = [i for i in range(10)]

pool = redis.ConnectionPool(host='127.0.0.1', port=6379, password='980304', decode_responses=True)
r = redis.StrictRedis(connection_pool=pool)
r.set('name', 'hhhahahahahha')
print(r.get('name'))