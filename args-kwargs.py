####### *args and **kwargs #######
def myFun(*argument, **keywordArguments):
    print("args: ", argument)
    print("kwargs: ", keywordArguments)


myFun('geeks', 'for', 'geeks', first="Geeks", mid="for", last="Geeks")

# gives error as args is after kwargs
# myFun('geeks', 'for', 'geeks', first="Geeks", mid="for", last="Geeks", 'geeks')