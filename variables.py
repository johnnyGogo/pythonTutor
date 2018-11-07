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
import enum

class InputType(enum.Enum):
    TRACK = 'track'
    ALBUM = 'album'
    ARTIST = 'atrist'
    PLAYLIST = 'playlist'


class Shape(enum.Enum):
    SQUARE = 1
    CIRCLE = 2


class Response(enum.Enum):
    OK = 1
    BAD = 2


class Mac(enum.IntEnum):
    AIR = 1
    PRO = 2
    PRO_PLUS = 4


class Android(enum.IntEnum):
    MARSHMALLOW = 1
    NOUGAT = 2
    PRO_PLUS = 4


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


def enum_test():
    TestEnum = enum.Enum('TestEnum', 'CAT DOG PANDA')
    print("Get enum name")
    print("InputType.PLAYLIST.name : {}".format(InputType.PLAYLIST.name))
    print("Get enum value")
    print("InputType.PLAYLIST.value : {}".format(InputType.PLAYLIST.value))
    print("Shape.SQUARE == Response.OK : {}".format(Shape.SQUARE == Response.OK))
    print("InputType.TRACK == 'track' : {}".format(InputType.TRACK == 'track'))
    print("Shape.SQUARE == 1 : {}".format(Shape.SQUARE == 1))
    print("Mac.AIR == 1 : {}".format(Mac.AIR == 1))
    print("Mac.AIR == Android.MARSHMALLOW : {}".format(Mac.AIR == Android.MARSHMALLOW))
    print("Mac.AIR | Android.NOUGAT : {}".format(Mac.AIR | Android.NOUGAT))

    print()
    print(TestEnum)
    print(TestEnum.CAT.name)
    print(TestEnum.CAT.value)



if __name__ == '__main__':
    fire.Fire()
