for num in range(1,101):
    primo = True
    for div in range(2,num):
        if num%div == 0:
            primo = False
            break
    if primo == True:
        print(f"- {num}")