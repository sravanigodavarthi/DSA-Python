# [1, 2, [3, 4, [5, 6] ], 7, 8, [9, [10] ] ]

# from functools import reduce
# my_list = [[1, 2], [3, 4], [5]]
# flat_list = reduce(lambda x, y: x + y, my_list)
# print(flat_list)  # Output: [1, 2, 3, 4, 5]



def flatten_list(obj):
    out = []
    def flatten(x):
        for item in x:
            print(item)
            if type(item) is list:
                flatten(item)
            else:
                out.append(item)
    flatten(obj)
    return out     

if __name__ == "__main__":
    nested_list = [1, 2, [3, 4, [5, 6] ], 7, 8, [9, [10] ] ]
    print(flatten_list(nested_list))