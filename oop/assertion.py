def divide_secure(number, dvisor):
    """
    The assertions can be removed from the program to allow a program to
    run in high performance mode. This will increase the performance of the program.

    """
    assert dvisor != 0, 'Divided a number by zero!'
    return number / dvisor

print(divide_secure(10,2))
