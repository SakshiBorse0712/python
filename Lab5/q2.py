test = ["String" , (1,2,3) , [1,2,3] , {"a" : 1 , "b" : 2}]

for key in test:
    try:
        test_dict = {key: "value"}
        print("Works")
    except:
        print("Error")
    