



"""(test1.py)
    这个create函数，可以实现参数抽取，给出函数名
"""

# test2.py 修改FuncSet为ToolSet
"""（test2.py）
    分析执行一个agent，普遍的框架应该是怎么样的。需要有prompt，llm，tool，memory，
    目前的执行过程是，
        1，调用openai的create函数，根据prompt，返回tool所需要的参数。
        2，执行tool，返回结果
    我期望的调用过程：
        1，构建一个对象
        2，调用对象的run函数。
    因此，这时需要一个agent类。
"""

# test2.py 试着写一个Agent类

# test3.py 精修Agent的逻辑
"""test3.py
    create函数里面的tools=function_description传参，要改一下，单独封装一个tool。

"""






# test2.py 试着生成一个Agent类对象


"""(test1.py)
    之所以要以对象的形式，注册函数，因为每次执行函数，都需要if-else判断，代码不灵活。
    之前无法管理函数，只能用if-else的形式去判断执行哪个函数，现在可以结合openai的function calling管理函数
    这个函数可以看做一个工具，tool
"""