#phone_no={'ram':23456,'sham':23456,'ramu':123456}
#python convrntion
phone_no={
    'ram':[23456,2,3,4,5],
    'sham':23456,
    'ramu':123456,
    'ram':2345 #if you create duplicate it takes final on only
}# this is more readable
print(phone_no)
# #access particular value use key in []
# print(phone_no['ram'])# this is case sensitive
# #another method to create dictionaries
# phone_no=dict({
#     'ram':23456,
#     'sham':23456,
#     'ramu':123456,
#     'madhav':2345
#
# })
#
# phone_num=([('ram',23456),('sham',23456),('ramu',123456)])
# phone_no['ram']=9999
# print(phone_num)
# #values can be any data type and it may be list ,set,tuplle .....
# #keys mudst be number strings and tuple,
# # dictionary can contain list
# phone_no['madhav']={2346,6789,11111}
# print(phone_no)
# phone_no['ramu']={"ramu_home":5555,'ramu_work':4444444444}
# print(phone_no)
# print(phone_no['ramu'])
# print(phone_no['ramu']["ramu_work"])
# print(phone_no.get("ram"))
#
# data={
#     1:"hema",
#     2:"vathi",
#     0:"bhee"
# }
# print(data[0])
# #delete
# #del phone_no['ram']
# print(phone_no)
# #print(phone_no.pop("ramu"))
# print(phone_no)
# #print(phone_no.popitem())
# #phone_no.clear()
# print(phone_no)
# # we can print keys and values seperately
# print(phone_no.keys())
# print(phone_no.values())
# print(phone_no.items())#item will print dict as list in tuples
# for i in phone_no:
#     print(i)
#     print(phone_no[i])
# for i in phone_no.items():
#     print(i)
# phone_no2=phone_no.copy()
# print(phone_no2)
# print(len(phone_no2))