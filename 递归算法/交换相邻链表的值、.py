i = 0
def func(i):
    print(i)
    i += 1
    func(i)


func(i)