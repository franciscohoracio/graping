import subprocess
import os
import socket
import platform
import sys

x=0
print ""
var_network = raw_input("Segmento de RED: ")
var_ipinit = input("IP inicial: ")
var_ipend = input("IP final: ")
print ""
with open(os.devnull, "wb") as limbo:


        for n in xrange(var_ipinit, var_ipend):
            try:
                ip= var_network+`n`
                result=subprocess.Popen(["ping", "-c", "1", "-t", "1", ip],
                        stdout=limbo, stderr=limbo).wait()
                if result:
                        print ip, "Inactive"
                else:
                        print ip, "Active", socket.gethostbyaddr(ip)
                        x=x+1

            except socket.error, msg:
                    print msg
print ""
print "Nodos Activos: ", x