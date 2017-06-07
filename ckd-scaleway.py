#!/usr/bin/python

################################################################
###                      Imports                             ###
################################################################

#Clear screen
import os,subprocess

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
#Arguements parsing
import argparse
from optparse import OptionParser
#Time for countdown
import time

from CkdPrompt import CkdPrompt


################################################################
###                      Variables                           ###
################################################################


global token
global sID
global datacenter
global prompt
global clear

version = "v0.3.1"

token = ""
datacenter = ""

verify_token = 0
verify_datacenter = 0

dct =  { 
    "par1":"https://cp-par1.scaleway.com",
    "ams1":"https://cp-ams1.scaleway.com" 
}
stype = { 
    "arm": ["ARM64-2G","ARM64-4G","ARM64-8G"],
    "x86_64": ["VC1S","VC1M","VC1L"]
}
url_act = "https://account.scaleway.com"


os.system('cls' if os.name=='nt' else 'clear')
print (Fore.GREEN+'      _____     _   _       _         ')
print (Fore.GREEN+'     |     |_ _| |_| |___ _| |___ _ _ ')
print (Fore.GREEN+"     |   --| | | '_| | . | . | -_| | |")
print (Fore.GREEN+'     |_____|_  |_,_|_|___|___|___|\_/ ')
print (Fore.GREEN+'           |___|                      ')
print (Fore.GREEN+'                 Scaleway CLI '+version+'    ')

print (Style.RESET_ALL)

def get_envvars():
    if os.environ.get('SCWTOKEN') is not None:
        print ( "Token detected as envvar")
        token = os.environ['SCWTOKEN']
        prompt.do_set_token(token)
    if os.environ.get('SCWDATACENTER') is not None:
        print ("Datacenter detected as envvar")
        datacenter = os.environ['SCWDATACENTER']
        prompt.do_set_datacenter(datacenter)
    prompt.do_set_options(options)




if __name__ == '__main__':
    sID=""

    ##PARSE ARGS
    parser = OptionParser()
    parser.add_option("-t", "--type", dest="commtype",
                  help="Command type [interactive|script]", metavar="COMMTYPE")
    parser.add_option("-c", "--create", dest="creastring",
                  help="Creation string Server", metavar="CREASTRING")
    parser.add_option("-l", "--list", action="store_true" , help="Get server list")
    parser.add_option("-q", "--quiet",
                  action="store_false", dest="verbose", default=True,
                  help="don't print status messages to stdout")

    (options, args) = parser.parse_args()

    global prompt

    if options.commtype is not None:
        if options.commtype == 'interactive' or options.commtype == 'i':
            prompt = CkdPrompt()
            get_envvars()
            prompt.prompt = Fore.BLUE+'ckd-scaleway# '+Style.RESET_ALL
            prompt.cmdloop('Loading Interactive Shell ....\n Type help to get commands')
        elif options.commtype == 'script' or options.commtype == 's':
            print ("Get in script mode but need to specify more option")
            print ("ENVVAR[TOKEN] = need to be set")
            print ("ENVVAR[DATACENTER] = need to be set")
            prompt = CkdPrompt()
            get_envvars()
            prompt.do_clear('')
            prompt.do_status('')
            if prompt.do_test_datacenter('') is not True:
                print ("Datacenter KO")
                exit
            if prompt.do_test_token('') is not True:
                print ("Token KO")
                exit
            if options.creastring is not None:
                print ( "List servers" )
                prompt.do_get_servers('')
                sID = prompt.do_create_server(options.creastring)
                print ("!!!!!!!!!!!!!!!!!!!"+sID)
                prompt.do_get_servers('')
                if sID is not None:
                    print ("Put "+sID+" server to poweron ["+sID +' poweron]')
                    prompt.do_set_server_action(sID +' poweron')
                    print ("sID value is known start to watch ["+sID+"]")
                    prompt.do_watchdog_server_poweron(sID)     
            elif options.list is True:
                print ("List from script call")
                prompt.do_get_servers('')
                exit
            else:
                 exit     
        else:
            print ("Invocation type not correct")
    else:
        prompt = CkdPrompt()
        get_envvars()
        prompt.prompt = Fore.BLUE+'ckd-scaleway# '+Style.RESET_ALL
        prompt.cmdloop('Loading Interactive Shell ....\n Type help to get commands')
