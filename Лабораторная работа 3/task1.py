src = not False and True or False and not True

src = not False or False and False    # результат False and True это False, not True это False
src = True or False    # результат not False это True, False and False это False
src = True

result = True

print(src == result)
