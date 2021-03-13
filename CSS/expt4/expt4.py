import hashlib

string=input('Enter string : ')
encoded=string.encode()
md5Result = hashlib.md5(encoded) 
print('------MD5------')
print("String : ",end="")
print(string)
print("Unicode String : ",end="")
print(encoded)
print("Hash Value : ",end="")
print(md5Result)
print("Equivalent Byte : ",end="")
print(md5Result.digest()) 
print("Hexadecimal Equivalent : ",end="")
print(md5Result.hexdigest()) 
print('\n\n\n')
shaResult = hashlib.sha1(encoded) 
print('------SHA1------')
print("String : ",end="")
print(string)
print("Unicode String : ",end="")
print(encoded)
print("Hash Value : ",end="")
print(shaResult)
print("Equivalent Byte : ",end="")
print(shaResult.digest()) 
print("Hexadecimal Equivalent : ",end="")
print(shaResult.hexdigest()) 