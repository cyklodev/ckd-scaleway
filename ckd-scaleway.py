################################################################
###                      Imports                             ###
################################################################


#Class
from cmd import Cmd	
#Color   # pip install colorama
from colorama import Fore, Back, Style
#Http    # pip install requests
import requests
#Json    
import json
#Pretty
import pprint
pp = pprint.PrettyPrinter(indent=4)

################################################################
###                      Variables                           ###
################################################################

version = "v0.1"
token = ""
datacenter = ""

dct =  { "par1":"https://cp-par1.scaleway.com" , "ams1":"https://cp-ams1.scaleway.com" }

print (Fore.GREEN+' _____     _   _       _         ')
print (Fore.GREEN+'|     |_ _| |_| |___ _| |___ _ _ ')
print (Fore.GREEN+"|   --| | | '_| | . | . | -_| | |")
print (Fore.GREEN+'|_____|_  |_,_|_|___|___|___|\_/ ')
print (Fore.GREEN+'      |___|                      ')
print (Fore.GREEN+'            Scaleway CLI '+version+'    ')

print (Style.RESET_ALL)

################################################################
###                      Class                               ###
################################################################


class CkdPrompt(Cmd):


    def headers(self,args):
        print (' _____     _   _       _         ')
        print ('|     |_ _| |_| |___ _| |___ _ _ ')
        print ("|   --| | | '_| | . | . | -_| | |")
        print ('|_____|_  |_,_|_|___|___|___|\_/ ')
        print ('      |___|                      ')
        print ('            Scaleway CLI v0.1    ')

    def do_quit(self, args):
        """Quits the program."""
        print Fore.BLUE+"Quitting prompt . thx for using :)"+Style.RESET_ALL
        raise SystemExit

    def do_status(self,args):
        """Check the status of settings"""
        print Fore.YELLOW+"Test requierments"
        global token
        if token == "":
            print Fore.RED+"Token not set"
            print "Use command settoken"+Style.RESET_ALL
        else:
            print Fore.GREEN+"Token = "+token+Style.RESET_ALL

        global datacenter 
        if datacenter == "":
            print Fore.YELLOW+"Datacenter not set [Loading default : par1]"
            print "Use command setdatacenter to change"
            datacenter="par1"
            print Fore.GREEN+"Datacenter = "+datacenter+Style.RESET_ALL
        else:
            print Fore.GREEN+"Datacenter = "+datacenter+Style.RESET_ALL

    def do_settoken(self,args):
        """Set the value of token"""
        global token
        token=args
        print "Token = "+token

    def do_setdatacenter(self,args):
        """Set the value of datacenter"""
        global datacenter
        datacenter=args
        print "Datacenter = "+datacenter

    def do_testdatacenter(self,args):
        """Test if the datacenter choosed is working properly via a request HTTP"""
        global datacenter
        global dct
        print "Datacenter = "+datacenter 
        print "URL = "+dct[datacenter]
        r = requests.get(dct[datacenter])

        if r.status_code == 200:
            print Fore.GREEN+"Link to datacenter OK"+Style.RESET_ALL
        else:
            print Fore.RED+"Link to datacenter KO"+Style.RESET_ALL        


if __name__ == '__main__':
    prompt = CkdPrompt()
    prompt.prompt = Fore.GREEN+'>>Ckd-Scw-Cli>> '+Style.RESET_ALL
    prompt.cmdloop('Loading ....')
