class subnet:
    def __init__(self,ip):
        self.ip=ip

    def fun_even(self):
        lis_evev_IP=[]
        for i in range (2,self.ip,2):
            print('even  ip is 192.168.1.{}'.format(i))
            lis_evev_IP.append('192.168.1.{}'.format(i))
        return lis_evev_IP


    def fun_odd(self):
         
         
        lis_odd_IP=[]
        for j in range (1,self.ip,2):
            print('odd  ip is 192.168.1.{}'.format(j))
            lis_odd_IP.append('192.168.1.{}'.format(j))
        return lis_odd_IP


class child_ip(subnet):
    def __init__(self,ip,sub):
        self.sub=sub
        super().__init__(ip)


    def final_even(self):
        for t in self.fun_even():
            print(t+'/'+self.sub)


    def final_odd(self):
        for z in self.fun_odd():
            print(z+'/'+self.sub)



IP=int(input('please enter STH'))
SUB=input('please enter sub')
obj1=child_ip(IP,SUB)
obj1.final_even()

