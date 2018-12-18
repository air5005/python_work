
def fundou(val, a, b):
    val.insert(-1, b)
    return a.join(val)

strpara = "apples bananas tofu cats"
listpara = strpara.split(' ')

ret = fundou(listpara, ' ', 'and')
print(ret)
