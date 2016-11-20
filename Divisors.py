
def main():
    while True:
        user_input = raw_input('Enter number:')
        if user_input.isdigit() and int(user_input) > 0:
            int_input = int(user_input)
            available_numbers = range(1, int_input + 1)
            divisors = []
            for number in available_numbers:
                if int_input % number == 0:
                    divisors.append(number)
            print "Divisors: "
            print divisors

        else:
            print 'Please enter valid number'

main()

