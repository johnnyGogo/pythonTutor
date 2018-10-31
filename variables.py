"""
內建資料類型:
- boolean : True / False
- int : e.g. 42, 100000
- float : e.g. 3.14159, 1.0e8
- string : 'abc'  多行字串\"\"\" \"\"\"

get variable type
- type()

convert type
- int({str})
- str({})
"""
import fire


def type_test():
    print("True:{}".format(type(True)))
    print("False:{}".format(type(False)))
    print("10:{}".format(type(10)))
    print("9.87e5:{}".format(type(9.87e5)))
    print("10.0:{}".format(type(10.0)))
    print("0b10:{}".format(type(0b10)))
    print("0o10:{}".format(type(0o10)))
    print("0x10:{}".format(type(0x10)))
    print("str:{}".format(type("str")))
    print("a:{}".format(type('a')))
    print("{{}}:{}".format(type({})))
    print("[]:{}".format(type([])))
    print("():{}".format(type(())))


if __name__ == '__main__':
    fire.Fire()
