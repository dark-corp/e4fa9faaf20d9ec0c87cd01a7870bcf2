import os, sys
print("Localizador de IPs\n")
x=input("IP:")
os.system("curl http://api.db-ip.com/v2/free/" + x)
