class subnet:
    def __init__(self,ip):
        self.ip=ip
    def fun_even(self):
        for i in range (2,self.ip,2):
            print('even  ip is 192.168.1.{}'.format(i))
    def fun_odd(self):
        for j in range (1,self.ip,2):
            print('odd  ip is 192.168.1.{}'.format(j))

class child_ip(subnet):
    pass
IP=int(input('please enter STH'))
obj1=child_ip(IP)
obj1.fun_even()
