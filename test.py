class IP_Calc(object):

    res = []

    def __init__(self,cadena):
        if len(cadena.split("/")) == 2:
            self.netmask_cidr = cadena.split("/")[1]
            self.ip_str = cadena.split("/")[0]
        else:
            self.netmask_cidr = str(self.__ip_to_bin(cadena.split(" ")[1]).find("0"))
            self.ip_str = cadena.split(" ")[0]
        self.ip_bin = self.__ip_to_bin(self.ip_str)
        self.netmask_str = ""
        self.broadcast_str = ""
        self.network_str = ""
        self.ip_min_str = ""
        self.quantity_host = 0
        self.res = self.__calc()

    def __bin_to_ip(self,bin_str):
        return str(int(bin_str[0:8],base=2))+"."+str(int(bin_str[8:16],base=2))+"."+str(int(bin_str[16:24],base=2))+"."+str(int(bin_str[24:32],base=2))

    def __bin_to_int(self,bin_str):
        return int(bin_str, base=2)

    def __ip_to_bin(self,ip):
        return ''.join([bin(int(x)+256)[3:] for x in ip.split('.')])
        self.res = self.__calc()

    def __calc(self):
        broadcast_bin = ""
        netmask_bin = ""
        network_bin = ""
        for key in range(0,32):
            if key > int(self.netmask_cidr)-1:
                netmask_bin += "0"
                broadcast_bin+= "1"
                network_bin+= "0"

            else:
                netmask_bin += "1"
                network_bin += self.ip_bin[key]
                broadcast_bin+= self.ip_bin[key]
        self.netmask_str = self.__bin_to_ip(netmask_bin)
        self.broadcast_str = self.__bin_to_ip(broadcast_bin)
        self.network_str = self.__bin_to_ip(network_bin)
        self.ip_min_str =  self.__bin_to_ip(str(bin(self.__bin_to_int(network_bin)+1))[2:])
        self.ip_max_str =  self.__bin_to_ip(str(bin(self.__bin_to_int(broadcast_bin)-1))[2:])
        self.quantity_host = self.__bin_to_int(broadcast_bin) - self.__bin_to_int(network_bin)-1
        if self.quantity_host > 1000:
            return ["Many Hosts"]
        else:
            for key in range(self.__bin_to_int(network_bin)+1,self.__bin_to_int(broadcast_bin)):
                self.res.append(self.__bin_to_ip(str(bin(key))[2:]))
            return self.res

ips = IP_Calc("192.168.1.34 255.255.255.0")
print "\n\nIP", ips.ip_str
print "Netmask", ips.netmask_str
print "Network", ips.network_str
print "Ip Minima", ips.ip_min_str
print "Ip Maxima", ips.ip_max_str
print "Broadcast", ips.broadcast_str
print "Cantidad de Host", ips.quantity_host


ips = IP_Calc("192.168.1.34/24")
print "\n\nIP", ips.ip_str
print "Netmask", ips.netmask_str
print "Network", ips.network_str
print "Ip Minima", ips.ip_min_str
print "Ip Maxima", ips.ip_max_str
print "Broadcast", ips.broadcast_str
print "Cantidad de Host", ips.quantity_host
