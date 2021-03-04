import math
print("RSA ENCRYPTION/DECRYPTION")
print("*****************************************************")
 
p = int(input("Enter a prime number for p: "))
q = int(input("Enter a prime number for q: "))
print("*****************************************************")
 
def prime_check(a):
    if(a==2):
        return True
    elif((a<2) or ((a%2)==0)):
        return False
    elif(a>2):
        for i in range(2,a):
            if not(a%i):
                return false
    return True
 
check_p = prime_check(p)
check_q = prime_check(q)
while(((check_p==False)or(check_q==False))):
    p = int(input("Enter a prime number for p: "))
    q = int(input("Enter a prime number for q: "))
    check_p = prime_check(p)
    check_q = prime_check(q)
 
#RSA Modulus
n = p * q
 
#Eulers Toitent

r= (p-1)*(q-1)
 
#GCD
def egcd(e,r):
    while(r!=0):
        e,r=r,e%r
    return e
 
#Euclid's Algorithm
def eugcd(e,r):
    for i in range(1,r):
        while(e!=0):
            a,b=r//e,r%e
            if(b!=0):
                (r,a,e,b)
            r=e
            e=b
 
#Extended Euclidean Algorithm
def eea(a,b):
    if(a%b==0):
        return(b,0,1)
    else:
        gcd,s,t = eea(b,a%b)
        s = s-((a//b) * t)
        (gcd,a,t,s,b)
        return(gcd,t,s)
 
#Multiplicative Inverse
def mult_inv(e,r):
    gcd,s,_=eea(e,r)
    if(gcd!=1):
        return None
    else:
        if(s<0):
            (s,s,s%r)
        elif(s>0):
            (s)
        return s%r
 
#e Value Calculation

for i in range(1,1000):
    if(egcd(i,r)==1):
        e=i

eugcd(e,r)

d = mult_inv(e,r)

public = (e,n)
private = (d,n)
print("Private Key is:",private)
print("Public Key is:",public)
print("*****************************************************")
 
#Encryption

def encrypt(pub_key,n_text):
    e,n=pub_key
    x=[]
    m=0
    for i in n_text:
        if(i.isupper()):
            m = ord(i)-65
            c=(m**e)%n
            x.append(c)
        elif(i.islower()):               
            m= ord(i)-97
            c=(m**e)%n
            x.append(c)
        elif(i.isspace()):
            spc=400
            x.append(400)
    return x
     
 
#Decryption
def decrypt(priv_key,c_text):
    d,n=priv_key
    txt=c_text.split(',')
    x=''
    m=0
    for i in txt:
        if(i=='400'):
            x+=' '
        else:
            m=(int(i)**d)%n
            m+=65
            c=chr(m)
            x+=c
    return x
 
#Message
message = input("Enter the Message to Encrypt or Decrypt:\n")
print("Your message is:",message)
 
#Choose Encrypt or Decrypt and Print
choose = input("Enter '1' for encryption and '2' for decrytion.\n")
if(choose=='1'):
    enc_msg=encrypt(public,message)
    print("Your encrypted message is:",enc_msg)

elif(choose=='2'):
    print("Your decrypted message is:",decrypt(private,message))
else:
    print("You entered the wrong option.")
