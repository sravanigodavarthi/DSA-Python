# You have a list of list to depth n. Write a program to normalize it.

input = [1,[2,4,[5,1,[3,4],[7,8,[1,2]]]]] 
output = [1,2,4,5,1,3,4,7,8,1,2]

def normalize_data(input_data):
    out = []
    def _normalize_data(input_data):
        for i in range(len(input_data)):
            if type(input_data[i]) is list:
                _normalize_data(input_data[i])
            else:
                out.append(input_data[i])

    _normalize_data(input_data)
    return out

print(normalize_data([1,[2,4,[5,1,[3,4],[7,8,[1,2]]]]]))

# Let's assume the input data has n elements in total (including elements inside nested lists)
# The time complexity is o(n) and space complexity os o(n)
