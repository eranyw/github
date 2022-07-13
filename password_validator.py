import sys
import os



def main():
 print("please enter a password length at least 10 charcters \n also contain alphabet and number \n include small and capital letter\n")
 os.system("")
os.system('color FF')


def In():
    password =input()
    sys.argv=password
    condition(sys.argv)

def len_size(password):

 if  len(password) >= 10 :
    return True
 else :
  return False


def is_lower(password):
 low = any(i.islower() for i in password)
 return low


def is_Capital_Letter(password):
 up = any(i.isupper() for i in password)
 return up


#def prRed(skk): print("\033[91m {}\033[00m".format(skk))
def prRed(prt):
   print(f"\033[91m{prt}\033[00m")

def prGreen(skk): print("\033[92m {}\033[00m".format(skk))


def condition(password):
 if not ( len_size(password)== True and \
  is_lower(password)== True and\
  is_Capital_Letter(password)== True):
   # print(Fore.RED + 'you have enter a not valid password')
   prRed("you have enter a not valid password")
  # print(Fore.RED + 'you have enter a not valid password')
   #print(Style.RESET_ALL)

   exit(1)
 else:
# print(Fore.GREEN + 'you have enter a not valid password')
   prGreen("you have enter a  valid password")

   exit(0)

main()
In()


















