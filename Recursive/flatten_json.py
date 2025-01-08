# Flatten a nested JSON object without using the ready-made JSON function flatten.
# Test Case #1
# Input: {"a": 1, "b": {"c": 2, "d": {"e": 3}}}
# Output: {"a": 1, "b_c": 2, "b_d_e": 3}
# Description: This test case assesses the algorithm""s capability to handle multiple levels of nested dictionaries while ensuring the keys are flattened correctly.
# Test Case #2
# Input: {"w": 3, "x": [{"y": 1}, {"z": 2}]}
# Output: {"w": 3, "x_0_y": 1, "x_1_z": 2}
# Description: This test case evaluates the function"s ability to manage lists containing dictionaries and ensuring the keys are appropriately indexed and flattened.
# Test Case #3
# Input: {"m": {"n": [{"o": {"p": 4}}, {"q": 5}], "r": 6}}
# Output: {"m_r": 6, "m_n_1_q": 5, "m_n_0_o_p": 4} reverse order of the final output
# Description: This case examines the algorithm on handling deeply nested structures including a mix of dictionaries and lists with further nesting, testing its ability to correctly flatten the structure.
# for key,value in obj.items():
#         if type(value) is dict:
#             print(key,value)
#             for key2,value2 in value.items():
#                 print(key2,value2)
#                 if type(value2) is dict:
#                     for key3,value3 in value2.items():
#                         print(key3,value3)
#                     out_key = key_key2_key3
#                     out[out_key] = value3
#                 out_key = key_key2
#                 out[out_key] = value2
#         else:
#             print(key,value)
#             out[key] = value
#     print(out)

def flatten_json(obj):
    out = {}
    def flatten(x, parent_key = '', sep = '_'):
        for key,value in x.items():
            new_key = f"{parent_key}{sep}{key}" if parent_key else key
            if type(value) is dict:
                flatten(value, parent_key = new_key)
            
            elif type(value) is list:
                for index,item in enumerate(value):
                    flatten(item, parent_key = f"{new_key}_{index}")
            else:
                out[new_key] = value
    flatten(obj)
    return out
if __name__ == "__main__":
    nested_obj = {"m": {"n": [{"o": {"p": 4}}, {"q": 5}], "r": 6}}
    print(flatten_json(nested_obj))
    
    
