import hashlib
2
from cryptography.fernet import Fernet
3
 
4
print("Secure Data Transmission App")
5
 
6
message = input("Enter a message: ")
7
 
8
hash1 = hashlib.sha256(message.encode()).hexdigest()
9
 
10
key = Fernet.generate_key()
11
cipher = Fernet(key)
12
 
13
encrypted = cipher.encrypt(message.encode())
14
 
15
decrypted = cipher.decrypt(encrypted).decode()
16
 
17
hash2 = hashlib.sha256(decrypted.encode()).hexdigest()
18
 
19
print("\nResults")
20
print("Hash:", hash1)
21
print("Encrypted:", encrypted)
22
print("Decrypted:", decrypted)
23
 
24
if hash1 == hash2:
25
print("Integrity Check: Passed")
26
else:
27
print("Integrity Check: Failed")