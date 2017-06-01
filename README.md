# ckd-scaleway

This python application provide an interface to manage Scaleway servers in a general manner via the HTTP API.
  - Pre setting of Token and Datacenter via ENVVARS
  - Switch datacenter 
  - Set token
  - Test API access from choosen datacenter
  - List organizations
  - List images, servers, volumes and IPs from the current datacenter
  - Test Image vs Server Type
  - Create a new server


# Why ?

> The provided SDK in python does not allow to fully
> manage the creation of a server. So I decided to write
> my own SDK as an interactive interface.

# Tech

ckd-scaleway uses a limited number of well-known python libraries to work:

* [colorama] - set some colors in the interface!
* [requests] - allow HTTP management of Scaleway API
* [json] - basic library to treat json data.
* [pprint] - allow the PrettyPrinting

### Installation

ckd-scaleway requires [python] and [pip] to run.

Install the dependencies and start the application:

```sh
$ pip install colorama
$ pip install requests
$ pip install pprint
$ python ckd-scaleway.py
```

Optionnaly you can preset the datacenter and your token:
```sh
$ export SCWTOKEN=xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx
$ export SCWDATACENTER=par1
$ python ckd-scaleway.py
ckd-scaleway# status
```

### Todos

 - Servers type listing
 - Tokens listing
 - PowerON, PowerOFF and Delete a server
 - Pip file requierements


License
----
```
/*
 * ----------------------------------------------------------------------------
 * "THE BEER-WARE LICENSE" (Revision 42):
 * <phk@FreeBSD.ORG> wrote this file. As long as you retain this notice you
 * can do whatever you want with this stuff. If we meet some day, and you think
 * this stuff is worth it, you can buy me a beer in return Poul-Henning Kamp
 * ----------------------------------------------------------------------------
 */
 ```

