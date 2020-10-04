'''
7.用两个栈实现队列
（1）stack2是空的时候才可以往里倒
（2）一旦从stack1开始往外倒，就必须进行到底，让stack1变空为止
'''
class StackToQueue:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []
    def pop(self):
        if self.stack2 == []:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        return self.stack2.pop()
