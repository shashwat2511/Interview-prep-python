####### decorator functions #######
def displaydecorator(fn):
    def display_wrapper(str1, str2):
        print('Output:', end=" ")
        fn(str1, str2)

    return display_wrapper

    # print('Output:', end=" ")
    # return fn(str)


@displaydecorator
def display(str1, str2):
    print(str1, str2)


display("hello", " world")