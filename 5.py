class ip_class:
    def __init__(self,ip):
        self.ip=ip

    def print_ip(self):
        print('ip is {}'.format(self.ip))

class subnet:
    def __init__(self,sub):
        self.sub=sub
    def print_subnet(self):
        print(f'subnet is{self.sub}')


class ip_subnet(ip_class,subnet):
    def __init__(self,ip,sub,namefile):
        self.namefile=namefile
        ip_class.__init__(self,ip)
        subnet.__init__(self,sub)

    def print_result(self):
        print(self.ip,self.sub)

    def write_to_file(self):
        with open('{}.txt'.format(self.namefile),'w') as f:
            f.write(self.ip+self.sub)

object_child1=ip_subnet('192.168.1.1','/30','WRfile')
object_child1.print_result()
object_child1.write_to_file()

