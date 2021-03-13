# Diffie Hellman Key Exchange
P = int(input("Enter a prime number value for P:\n"))

G = int(input("Enter a prime number value for G:\n"))

a = int(input("Enter the private key for Alice:\n"))

x = int(pow(G, a, P))

b = int(input("Enter the private key for Bob:\n"))

y = int(pow(G, b, P))

ka = int(pow(y, a, P))

kb = int(pow(x, b, P))

print("Alice's Secret key  is : %d\n" % (ka))
print("Bob's Secret Key  is : %d\n" % (kb))