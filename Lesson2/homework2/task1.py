my_l = ['string', None, 1, 3.14]
my_k = (1, 3.14, True, 'c', None)
my_multitude = set('abra-kadabra')
my_dict = {'key1': 1, 2: "2nd key value"}
my_list = [None, False, 1, 3.14, 'word', print("funct type"), my_l, my_k, my_multitude, my_dict]

for element in my_list:
    print(type(element))
