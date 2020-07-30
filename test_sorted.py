from functools import cmp_to_key

# sort 与 sorted 区别：
# sort 是应用在 list 上的方法，sorted 可以对所有可迭代的对象进行排序操作。
# list 的 sort 方法返回的是对已经存在的列表进行操作，而内建函数 sorted 方法返回的是一个新的 list，而不是在原来的基础上进行的操作。
#
# 语法
# sorted(iterable, key=None, reverse=False)
# iterable -- 可迭代对象。
# key -- 主要是用来进行比较的元素，只有一个参数，具体的函数的参数就是取自于可迭代对象中，指定可迭代对象中的一个元素来进行排序。
# reverse -- 排序规则，reverse = True 降序 ， reverse = False 升序（默认）。


def test_normal():
"""
排序，难度简单
"""
  example1 = sorted([5, 2, 3, 1, 4])
  example2 = sorted([5, 2, 3, 1, 4], reverse=True)
  # 预期
  # example1 = [1, 2, 3, 4, 5]
  # example2 = [5, 4, 3, 2, 1]
  
  example3 = [{"age":20,"name":"a"},{"age":25,"name":"b"},{"age":10,"name":"c"}]
  example3_sorted = sorted(array,key=lambda x:x["age"])
  # 预期
  # example3_sorted = [{'age': 10, 'name': 'c'}, {'age': 20, 'name': 'a'}, {'age': 25, 'name': 'b'}]
  
  example_double = [
    {'index':1, 'score':38, 'name'='李雷'},
    {'index':2, 'score':18, 'name'='韩梅梅'},
    {'index':6, 'score':28, 'name'='张三'},
    {'index':5, 'score':28, 'name'='张三疯'},
    {'index':9, 'score':58, 'name'='张伟'}
  ]
  example_double_sort = sorted(example_double, key=lambda x:(-x['score'], x['index']))
  # 预期
  # example_double_sort = [
  #   {'index':9, 'score':58, 'name'='张伟'},
  #   {'index':1, 'score':38, 'name'='李雷'},
  #   {'index':5, 'score':28, 'name'='张三疯'},
  #   {'index':6, 'score':28, 'name'='张三'},
  #   {'index':2, 'score':18, 'name'='韩梅梅'},
  # ]


def test_cmp_to_key_one():
"""
自定义排序，难度简单
python3中cmp已经被移除，可以用functools.cmp_to_key来替代
"""
  nums = [4, 8, 2, 1]
  xx = sorted(nums, key=cmp_to_key(lambda a, b: a - b))
  yy = sorted(nums, key=lambda a: a)
  zz = sorted(nums, key=lambda a: a*-1)
  # 预期
  # xx = [1, 2, 4, 8]
  # yy = [1, 2, 4, 8]
  # zz = [8, 4, 2, 1]


def test_cmp_to_key_two():
"""
根据数据中index排序,规则 2 > 1 >3
自定义排序，难度复杂
python3中cmp已经被移除，可以用functools.cmp_to_key来替代
"""
  def custom_sort(x, y):
    if x['index'] == y['index']:
        return 0
    elif x['index'] == 2:
        return 1
    elif x['index'] != 2 and y['index'] != 2 and x['index'] == 1:
        return 1
    else:
        return -1
  test1 = dict(id='1', name='未开始', index=1)
  test2 = dict(id='2', name='进行中', index=2)
  test3 = dict(id='3', name='已结束', index=3)
  test4 = dict(id='4', name='进行中', index=2)
  test5 = dict(id='5', name='进行中', index=2)
  test6 = dict(id='6', name='未开始', index=1)
  test7 = dict(id='7', name='已结束', index=3)
  test8 = dict(id='8', name='未开始', index=1)
  test_list = []
  test_list.append(test1)
  test_list.append(test2)
  test_list.append(test3)
  test_list.append(test4)
  test_list.append(test5)
  test_list.append(test6)
  test_list.append(test7)
  test_list.append(test8)

  result = sorted(test_list, key=cmp_to_key(custom_sort), reverse=True)
  
  # 预期
  # result = [
  #   {'id'='2', 'name'='进行中', 'index'=2},
  #   {'id'='4', 'name'='进行中', 'index'=2},
  #   {'id'='5', 'name'='进行中', 'index'=2},
  #   {'id'='1', 'name'='未开始', 'index'=1},
  #   {'id'='6', 'name'='未开始', 'index'=1},
  #   {'id'='8', 'name'='未开始', 'index'=1},
  #   {'id'='3', 'name'='已结束', 'index'=3},
  #   {'id'='7', 'name'='已结束', 'index'=3},
  # ]
      
      
