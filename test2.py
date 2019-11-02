# from test import pool
# from redis import StrictRedis
# r = StrictRedis(connection_pool=pool)
# r.get('name')

a = [[[23, 4]], [[23, 4]], [[23, 4]]]
# for i in a:
#     for j in i:
#         for k in j:
#             print(k)
# li = [j for i in a for j in i]
lil = [k for i in a for j in i for k in j]
print(lil)