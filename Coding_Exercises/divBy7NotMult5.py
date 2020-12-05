"""
This Python script returns all numbers divisible by 7 that
are not multiples of 5 between an upper and lower integer limit

The user is prompted to define those limits that get code enforced
to be numeric with the upper limit greater in value from the
lower one
"""

# User Input Validation Function
def limits_inp_validation():

    # expects integer user responses for Upper and Lower limits, otherwise it prints an exception error and warns user
    while True:
        try:
            lower_limit = int(input("Enter a numeric value for LOWER limit: "))
            upper_limit = int(input("Enter a numeric value for UPPER limit: "))

            # breaks While loop and returns limits only when Upper limit > Lower limit
            if upper_limit > lower_limit:
                break
            else:
                print('Lower limit: {} must be lower than the Upper limit: {}'.format(lower_limit, upper_limit))

        except Exception as e:
            print(" Upper and lower limits must be integers, please try again ")
            print(e)
            print()

    return lower_limit, upper_limit


def main():
    l, u = limits_inp_validation()

    result = False
    for i in range(l, u):

        if (i % 7 == 0) and (i % 5 != 0):
            print(' {} '.format(i),  end=" ")
            result = True

    if not result:
            print("no numbers found")


if __name__ == "__main__":
    main()
