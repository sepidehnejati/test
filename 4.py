#multilevel inheritence
class subnet:
    def __init__(self,ip):
        self.ip=ip

    def fun_even(self):
        lis_evev_IP=[]
        for i in range (2,self.ip,2):
            #print('even  ip is 192.168.1.{}'.format(i))
            lis_evev_IP.append('192.168.1.{}'.format(i))
        return lis_evev_IP


    def fun_odd(self):
         
         
        lis_odd_IP=[]
        for j in range (1,self.ip,2):
            #print('odd  ip is 192.168.1.{}'.format(j))
            lis_odd_IP.append('192.168.1.{}'.format(j))
        return lis_odd_IP


class child_ip(subnet):
    def __init__(self,ip,sub):
        self.sub=sub
        super().__init__(ip)


    def final_even(self):
        listt_final_even=[]
        for t in self.fun_even():
            print(t+'/'+self.sub)
            listt_final_even.append(t+'/'+self.sub)
        return listt_final_even
        


    def final_odd(self):
        listt_final_odd=[]
        for z in self.fun_odd():
            print(z+'/'+self.sub)
            listt_final_odd.append(z+'/'+self.sub)
        return listt_final_odd


class child_file(child_ip):
    def __init__(self,ip,sub,namefile):
        self.namefile=namefile
        super().__init__(ip,sub)


    def save_to_file_evev(self):
        with open('{}.txt'.format(self.namefile),'a+') as evenf:
            for m in self.final_even():
                evenf.write(m)
                evenf.write('\n')

    def save_to_file_odd(self):
        with open('{}.txt'.format(self.namefile),'a+') as evenf:
            for n in self.final_odd():
                evenf.write(n)
                evenf.write('\n')



IP=int(input('please enter STH'))
SUB=input('please enter sub')
NAME=input('say name\n')
obj1=child_file(IP,SUB,NAME)
obj1.save_to_file_evev()

