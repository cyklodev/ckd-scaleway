#!/usr/bin/python

################################################################
###                      Imports                             ###
################################################################

#Clear screen
import os,subprocess
#Interactive shell
from cmd import Cmd	
#Color   
#pip install colorama
from colorama import Fore, Back, Style
#Http    
# pip install requests
import requests
#Json    
import json
#Pretty
#pip install pprint
import pprint
pp = pprint.PrettyPrinter(indent=4)

################################################################
###                      Functions                           ###
################################################################

def clear():
    if os.name in ('nt','dos'):
        subprocess.call("cls")
    elif os.name in ('linux','osx','posix'):
        subprocess.call("clear")
    else:
        print "\n"*120


################################################################
###                      Variables                           ###
################################################################

version = "v0.2.0"

token = ""
datacenter = ""

dct =  { "par1":"https://cp-par1.scaleway.com" , "ams1":"https://cp-ams1.scaleway.com" }
url_act = "https://account.scaleway.com"

verify_token = 0
verify_datacenter = 0

clear()
print (Fore.GREEN+'      _____     _   _       _         ')
print (Fore.GREEN+'     |     |_ _| |_| |___ _| |___ _ _ ')
print (Fore.GREEN+"     |   --| | | '_| | . | . | -_| | |")
print (Fore.GREEN+'     |_____|_  |_,_|_|___|___|___|\_/ ')
print (Fore.GREEN+'           |___|                      ')
print (Fore.GREEN+'                 Scaleway CLI '+version+'    ')

print (Style.RESET_ALL)

################################################################
###                      Class                               ###
################################################################


class CkdPrompt(Cmd):

    ####  Inner functions

    def emptyline(self):
        pass

    def updateprompt(self, int):
        global prompt
        """Change the interactive prompt"""
	if int == 1:
            prompt.prompt = Fore.BLUE+'ckd-scaleway ['+Fore.RED+datacenter+Fore.BLUE+']# '+Style.RESET_ALL
        elif int == 0:
            prompt.prompt = Fore.BLUE+'ckd-scaleway ['+Fore.GREEN+datacenter+Fore.BLUE+']# '+Style.RESET_ALL
        else:
            prompt.prompt = Fore.BLUE+'ckd-scaleway ['+Fore.YELLOW+datacenter+Fore.BLUE+']# '+Style.RESET_ALL

    def do_clear(self,args):
        """Clear the screen"""
        clear()
        print (Fore.GREEN+'      _____     _   _       _         ')
        print (Fore.GREEN+'     |     |_ _| |_| |___ _| |___ _ _ ')
        print (Fore.GREEN+"     |   --| | | '_| | . | . | -_| | |")
        print (Fore.GREEN+'     |_____|_  |_,_|_|___|___|___|\_/ ')
        print (Fore.GREEN+'           |___|                      ')
        print (Fore.GREEN+'                 Scaleway CLI '+version+'    ')

    def do_quit(self, args):
        """Quits the program."""
        print (Fore.GREEN+'       _____     __    __        __        ')
        print (Fore.GREEN+'      / ___/_ __/ /__ / /__  ___/ /__ _  __')
        print (Fore.GREEN+"     / /__/ // /  '_// / _ \/ _  / -_) |/ /")
        print (Fore.GREEN+'     \___/\_, /_/\_\/_/\___/\_,_/\__/|___/ ')
        print (Fore.GREEN+'         /___/                             ')
        print (Fore.GREEN+'                  Scaleway CLI '+version+' ')
        print (Fore.GREEN+'')
        print Fore.BLUE+"Support: https://github.com/cyklodev/ckd-scaleway/issues "
        print Fore.BLUE+"Thanks for using :)"+Style.RESET_ALL 
        raise SystemExit

    ####  Status functions

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
            self.updateprompt(2)
        else:
            print Fore.GREEN+"Datacenter = "+datacenter+Style.RESET_ALL

    ####  organizations functions

    def do_get_organizations(self,args):
        """List organizations from current datacenter"""
        global token
        global pp
        headers = { "Region": datacenter, "X-Auth-Token": token }
        custom_url = url_act+'/organizations'
        r = requests.get(custom_url, headers=headers)
        if r.status_code == 200:
            global pp
            jso = r.json()
            for i in jso['organizations']:
                print ("Name: "+i['name'])
                print ("Oraganization ID: "+i['id'])
        else:
            print Fore.RED+"Something wrong cannot access to organizations list"
            print "Launch test_datacenter to see if link access is available"+Style.RESET_ALL 

    ####  Tokens functions

    def do_set_token(self,args):
        """Set the value of token"""
        global token
        token=args
        print "Token = "+token

    def do_test_token(self,args):
        """Set the value of token"""
        global token
        headers = { "Content-Type": "application/json", "X-Auth-Token": token }
        custom_url = url_act+'/tokens/'+token
        r = requests.get(custom_url, headers=headers)
        if r.status_code == 200:
            global pp
            pp.pprint( r.json() )
        else:
            print Fore.RED+"Something wrong cannot verify actual token"
            print "Launch test_datacenter to see if link access is available"+Style.RESET_ALL 


    ####  Datacenter functions

    def do_set_datacenter(self,args):
        """Set the value of datacenter"""
        global datacenter
        datacenter=args
        print "Datacenter = "+datacenter

    def do_test_datacenter(self,args):
        """Test if the datacenter choosed is working properly via a request HTTP"""
        global datacenter
        global dct
        print "Datacenter = "+datacenter 
        print "URL = "+dct[datacenter]
        r = requests.get(dct[datacenter])

        if r.status_code == 200:
            print Fore.GREEN+"Link to datacenter OK"+Style.RESET_ALL
            self.updateprompt(0)
        else:
            print Fore.RED+"Link to datacenter KO"+Style.RESET_ALL        
            self.updateprompt(1)

    ####  Images functions

    def do_get_images(self,args):
        """List all available images"""
        global token
        headers = { "Content-Type": "application/json", "X-Auth-Token": token }
        custom_url = dct[datacenter]+'/images'
        r = requests.get(custom_url, headers=headers)
        #r = requests.get(custom_url, headers=({"X-Auth-Token": token}))
        if r.status_code == 200:
            global pp
            #pp.pprint(r.json())
            jso = r.json()
            for i in jso["images"]:
                print (i['id']+"\t\t"+i['arch']+"\t\t"+i['name'])
        else:
            print Fore.RED+"Something wrong cannot access to images list"
            print "Launch test_datacenter to see if link access is available"+Style.RESET_ALL 

    ####  Servers functions


    def do_get_servers(self,args):
        """List servers from current datacenter"""
        global token
        global pp
        headers = { "Region": datacenter, "X-Auth-Token": token }
        custom_url = dct[datacenter]+'/servers'
        r = requests.get(custom_url, headers=headers)
        if r.status_code == 200:
            global pp
            #pp.pprint(r.json())
            print "Number of servers = "+str(len(r.json()['servers']))
            jso = r.json()
            for i in jso["servers"]:
                print (i['hostname']+" "+i['id']+" "+i['public_ip']['address'])
        else:
            print Fore.RED+"Something wrong cannot access to servers list"
            print "Launch test_datacenter to see if link access is available"+Style.RESET_ALL 

    ####  Volumes functions


    def do_get_volumes(self,args):
        """List volumes from current datacenter """
        global token
        global pp
        headers = { "Region": datacenter, "X-Auth-Token": token }
        custom_url = dct[datacenter]+'/volumes'
        r = requests.get(custom_url, headers=headers)
        if r.status_code == 200:
            global pp
            pp.pprint(r.json())
            print "Number of volumes = "+str(len(r.json()['volumes']))
            #jso = r.json()
            #for i in jso["servers"]:
            #    print (i['hostname']+" "+i['id']+" "+i['public_ip']['address'])
        else:
            print Fore.RED+"Something wrong cannot access to volumes list"
            print "Launch test_datacenter to see if link access is available"+Style.RESET_ALL 

    ####  IPs functions


    def do_get_ips(self,args):
        """List IPs from current datacenter """
        global token
        global pp
        headers = { "Region": datacenter, "X-Auth-Token": token }
        custom_url = dct[datacenter]+'/ips'
        r = requests.get(custom_url, headers=headers)
        if r.status_code == 200:
            global pp
            pp.pprint(r.json())
            print "Number of IPs = "+str(len(r.json()['ips']))
            #jso = r.json()
            #for i in jso["servers"]:
            #    print (i['hostname']+" "+i['id']+" "+i['public_ip']['address'])
        else:
            print Fore.RED+"Something wrong cannot access to IPs list"
            print "Launch test_datacenter to see if link access is available"+Style.RESET_ALL 




if __name__ == '__main__':
    prompt = CkdPrompt()
    prompt.prompt = Fore.BLUE+'ckd-scaleway# '+Style.RESET_ALL
    prompt.cmdloop('Loading ....')
