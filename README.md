# ckd-scaleway

This python application provide an interface to manage Scaleway servers in a general manner via the HTTP API.

  - Switch datacenter
  - Switch token
  - Test API access from choosen datacenter

# Why ?

> The providing SDK in python does not allow to fully
> manage the creation of a server. So I decided to write
> my own SDK as an interactive interface.

# Tech

ckd-scaleway uses a limited number of python libraries to work:

* [colorama] - set some colors in the interface!
* [requests] - allow HTTP management of Scaleway API
* [json] - basic library to treat json data.
* [pprint] - allow the PrettyPrinting

### Installation

ckd-scaleway requires [python] and [pip] to run.

Install the dependencies and start the application.

```sh
$ pip install colorama
$ pip install requests
$ pip install pprint
$ python ckd-scaleway.py
```


### Todos

 - Images listing
 - Servers type listing
 - Tokens listing
 - Create, PowerON, PowerOFF and Delete a server


License
----

/*
 * ----------------------------------------------------------------------------
 * "THE BEER-WARE LICENSE" (Revision 42):
 * <phk@FreeBSD.ORG> wrote this file. As long as you retain this notice you
 * can do whatever you want with this stuff. If we meet some day, and you think
 * this stuff is worth it, you can buy me a beer in return Poul-Henning Kamp
 * ----------------------------------------------------------------------------
 */
  

