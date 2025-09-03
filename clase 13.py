
def num_par(limit):
    for x in range(limit+1):
        if x%2==0:
            yield x
            
for x in num_par(10):
    print(x)
#print("------------------------")

def num_impar(limit2):
    for x in range(limit2+1):
        if x%2!=0:
            yield x
#print("------------------------")

def numer_par(lim):
    a=0
    while a<=lim:
        a=a+2
        yield a

for a in numer_par(10):
    print (a)
















