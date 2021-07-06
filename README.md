# pingdiscover.py
##### pingdiscover is simple commandline app for looking up hosts in given network 
## Installation
### Using pip
$ pip install pingdiscover
### Manual installation from Git
$ git clone https://github.com/
$ cd pingdiscover
$ python3 setup.py install

### Using Makefile
$ make install

# Usage
`$ pingdiscover [NETWORK] [CONCURRENCY] [TIMEOUT]`
- network - full network address with subnet.
- concurrency - the number of hosts are pinged at the same time.
- timeout - value in seconds of waiting time of each ping request.

Example: 

`$ pingdiscover 192.168.0.0/24 --concurrent 8 --timeout 3`

By default --timeout value is set to 5 seconds

`$ pingdiscover 192.168.0.0/24 --concurrent 10`

