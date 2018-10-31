import fire

def true_test():
	test_array = [False, None, 0, 0.0, '', [], (), {}, set()]
	for test in test_array:
		print('{} is {}'.format(str(test), True if test else False) )

	test_array = [True, 'abc', 1, -1, [1,2]]
	for test in test_array:
		print('{} is {}'.format(str(test), True if test else False) )


if __name__ == '__main__':
	fire.Fire()