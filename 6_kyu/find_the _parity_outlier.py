def find_outlier(integers):
    if len(integers)>=3:
        mods = [n%2 for n in integers]
        return integers[mods.index(0)] if sum(mods[:3]) > 1 else integers[mods.index(1)]





# def find_outlier(integers):
#     if len(integers)>=3:
#         for i in integers:
#             if i % 2 != 0:
#                 print(i)
           

# find_outlier([2,4,6,8,10,3,5])
