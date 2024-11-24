i=0
while True:
    a="file"+str(i)+".txt"
    f=open("C:\\Users\\Administrator\\OneDrive\\Desktop\\Worm\\Test folder\\"+a,'a+')      #Please enter the right path of your test folder
    f.write('random_text')
    f.close()
    i=i+1

    
