import quantumrandom


def few_numbers():
    return quantumrandom.get_data(data_type='uint16', array_length=5)


print('число от 0 до 9          = ', quantumrandom.randint(0, 9))
print('целое число от 0 до 9    = ', int(quantumrandom.randint(0, 9)))
random_list = few_numbers()
print('лист из нескольких чисел = ', random_list, )
