input = [("1",{"name":"John","address":{"city":"Austin","zipcode":"75093"}})]
data = [input[0][0],input[0][1]['name'],input[0][1]['address']['city'],input[0][1]['address']['zipcode']]
print(data)