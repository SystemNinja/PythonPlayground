for i in range(1,100+1):
    if i%3==0 and i%5==0:
        print("Site")
    elif i%3==0:
        print("Host")
    elif i%5==0:
        print("SiteHost")
    else:
        print(i)