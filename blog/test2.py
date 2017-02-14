def fn(self, name='world'): # 先定义函数
    print('Hello, %s.' % name)

Hello = type('Hello',(object,),dict(hello=fn))

h = Hello()
print(h.hello())
print(type(Hello))
print(type(h))