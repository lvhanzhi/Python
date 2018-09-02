# l=[1,2,3]
# res=l.__iter__()
# print(res.__next__())


# dic={
#     'name':'egon',
#     'age':18,
#     'sex':'male'
# }
# res=dic.__iter__()
# while True:
#     try:
#         print(res.__next__())
#     except StopIteration:
#         break
#
# res=iter(dic)
# while True:
#     try:
#         print(next(res))
#     except StopIteration:
#         break

# try:
#     while True:
#         print(next(res))
# except StopIteration:
#     print('')
