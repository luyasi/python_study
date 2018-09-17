# python中有6个基本数据类型
# 1.number   数值类型
# int    整形
# float  浮点型
# bool   布尔型
# True   表示肯定
# False  表示否定
# complex    复数
# a = 实数+虚数(j) b=1+0j c=1+3j
# 2.string   字符类型
# 单引号    a='hello'
# 双引号    a="hello"
# 三引号    a="""hello"""
# 3.list     列表类型
# 就是一系列数据的顺序组合，并且组合之后可以修改，标识符[]
# 4.tuple    元组类型
# 就是一系列数据的顺序组合，组合之后不能修改，标识符，
# 5.dict     字典类型
# 就是一系列数据的无序组合，组合之后可以修改，标识符{}
# 6.set      集合类型
# 就是一系列数据的无序组合，所有数据不会重复，标识符无

# type()查看一个变量的数据类型
# a=1+0j
# b=3j
# print(a,type(a))
# print(b,type(b))

# str1="金星说：“人不犯我，我不犯人，\n人若犯我，忍让三分，\n人若再犯，斩草除根。”"
# print(str1,type(str1))
#
# str2='''金星说：“人不犯我，我不犯人,
#      人若犯我，忍让三分，
#      人若再犯，斩草除根。”'''
# print(str2,type(str2))

# \表示转义，把后面的字母转换成有特殊含义的
# a="a\\\\nb"
# print(a)

# r表示元字符，无特殊含义输出
# a=r"\n"
# print(a)

# list类型，列表类型
# a = [1,2,3]
# print(a,type(a))

# tuple类型，元组类型
# a=(1,2,3)
# print(a,type(a))
# b = ()
# print(b,type(b))

# a = {"a":1,"b":2,"c":3}
# print(a,type(a))
# b = {}
# print(b,type(b))

# a = {1,2,3,4,5,4,3,5}
# print(a,type(a))
# b = set()
# print(b,type(b))
