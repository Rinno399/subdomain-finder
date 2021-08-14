import requests
print("""\033[1;36m┍━━━━━━━━━━━━━━━━━━━━━★━━━━━━━━━━━━━━━━━━━━┑\033[0m""")
print("""\033[1;36m|     \033[1;34m Creator>>   BR1N@n0\033[1;36m                 |\033[0m""")
print("""\033[1;36m|     \033[1;33m             RINNO  \033[1;36m                 |\033[0m""")
print("""\033[1;36m┕━━━━━━━━━━━━━━━━━━━━━★━━━━━━━━━━━━━━━━━━━━┙\033[0m""")

print("\033[1;31m<<<<<Ener domain without protocol and www.>>>>>\033[0m")
domain=input("\033[1;32m  Domain>>>")
print ("\033[1;36mWhat is your Protocol\n Choice 1 or 2")
print("""<<[1] https://""")
print("""<<[2] http://""")
P_T=input("Enter your protocol,[1]or[2]\n>>")
print("[+]Finding,Please wait[+]")
file=open("wordlist.txt","r")
data=file.read()
subs=data.splitlines()

if P_T == "1" :
     for subdomain in subs:
         R_url="https://"+subdomain+"."+domain
         try:
             requests.get(R_url)
         except requests.ConnectionError:

             pass
         else:
             print("\033[1;32mFound>>",R_url,"\033[0m")

else :
     for subdomain in subs:
         R_url="http://"+subdomain+"."+domain
         try:
             requests.get(R_url)
         except requests.ConnectionError:

             pass
         else:
             print("\033[1;32mFound>>",R_url,"\033[0m")
