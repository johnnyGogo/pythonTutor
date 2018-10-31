"""
#轉義: \t \n ...

#Slice: [start : end : step]

#長度 len()

#分割 split()

#連結 join()

#取代 replace() : str.replace({old}, {new}, {次數})

#尋找第一個位移 str.find({word})

#字首是不是 str.startswith({word})

#字尾是不是 str.endswith({word})

#最後一次位移 str.rfind({word})

#字母出現在幾次 str.count({word})

#是不是只有字母與數字 str.isalnum()

# str.capitalize()

# str.title()

# str.upper()

# str.lower()

# str.swapcase()

# str.center({int})

# str.ljust({int})

# str.rjust({int})
"""
import fire


def common_use():
	#轉義
	print('轉義:')
	print('a\tb')
	print('a\nb')

	#slice
	# [start : end : step]
	print('Slice:')
	s = 'abcdefghijklmnopqrstuvwxyz'
	print(s[:])
	print(s[::-1])

	#len
	print('\nlen():')
	print("{} len:{}".format(s, len(s)))

	#split
	print('\nsplit()')
	s = '"a,b,c,d,e"'
	print('{}.split(",") : {}'.format(s, s.split(',') ))

	#join
	print('\njoin()')
	a = ['a', 'b', 'c']
	print('{}.join(",") : {}'.format(a, ",".join(a)))

	#replace
	print('\nstr.replace({old}, {new}, [次數])')
	s = 'this is a dog'
	print('{}.replace("is" , "", 2) : {}'.format(s, s.replace("is", "", 2	)))


def capitalize():
	print('this is a test text'.capitalize())


def title():
	print('this is a test text'.title())


if __name__ == '__main__':
    fire.Fire()
    import doctest
    doctest.testmod()