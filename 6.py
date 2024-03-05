with open('fee.txt','a+') as f:
    f.write('\n')
    f.write('salam')
    f.seek(0)
    print(f.read())
   
    
   