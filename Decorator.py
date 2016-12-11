def logger(function):
    def wrapped(*args, **kwargs):
        print "Function args: " + str(args)
        print "Function kwargs: " + str(kwargs)
        function(*args, **kwargs)

    return wrapped


@logger
def func(number1, number2, list_string, kwa_pls='kwa'):
    print "Numbers {} and {} with strings {}. Kwa? - {}" \
        .format(str(number1), str(number2), str(list_string), str(kwa_pls))


list_string = {'string1': 'qwert', 'string2': 'asdfg'}
func(2, 6, list_string, kwa_pls='kwa')
