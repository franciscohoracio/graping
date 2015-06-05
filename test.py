class IP_Calc(object):
    """Esta clase recibe un string con una cadena y resuelve IPs validas"""
    res = []

    def __init__(self,cadena):
        self.cadena = cadena
        self.network_parts = self.cadena.split("/")
        self.ip_str = self.network_parts[0]
        self.ip_bin = self.ip_to_bin(self.ip_str)
        self.netmask_cdr = self.network_parts[1]
        self.netmask_bin = self.create_netmask_in_bin()
        self.netmask_str = self.bin_to_ip(self.netmask_bin)
        self.network_str = self.dir_network()
        self.network_bin = self.ip_to_bin(self.network_str)
        self.broadcast_str = self.broadcast()
        self.ip_min_str = self.ip_minima()
        self.ip_max_str = self.ip_maxima()
        self.int_host_min = int(self.bin_to_int(self.ip_to_bin(self.ip_min_str)))
        self.int_host_max = int(self.bin_to_int(self.ip_to_bin(self.ip_max_str)))
        self.cantidad_host = self.int_host_max-self.int_host_min +1
        self.res = self.result()

    def ip_to_bin(self,ip):
        return ''.join([bin(int(x)+256)[3:] for x in ip.split('.')])

    def bin_to_ip(self,bin_str):
        ip = ""
        ip_int = self.bin_to_ip_int(bin_str)
        return str(ip_int[0])+"."+str(ip_int[1])+"."+str(ip_int[2])+"."+str(ip_int[3])

    def bin_to_ip_int(self,bin_str):
        ip = []
        num = [bin_str[0:8],bin_str[8:16],bin_str[16:24],bin_str[24:32]]
        for i in num:
            ip.append(int(self.bin_to_octet(i)))
        return ip

    def bin_to_int(self,bin_str):
        ip = ""
        bandera = 2147483648
        octeto = 0
        for i in range(0,len(bin_str)):
            if bin_str[i] == "1":
                octeto +=bandera
            bandera = bandera/2
        ip += "." + str(octeto)
        return ip[1:]

    def octet_to_bin(self, octet):
        return '.'.join([bin(int(octet)+256)[3:]])

    def bin_to_octet(self, bin_str):
        ip = ""
        bandera = 128
        octeto = 0
        for i in range(0,len(bin_str)):
            if bin_str[i] == "1":
                octeto +=bandera
            bandera = bandera/2
        ip += "." + str(octeto)
        return ip[1:]

    def create_netmask_in_bin(self):
        netmask_str = ""
        for key in range(0,32):
            if key > int(self.netmask_cdr)-1:
                netmask_str += "0"
            else:
                netmask_str += "1"
        return netmask_str

    def dir_network(self):
        res = ""
        for key in range(0,32):
            if self.netmask_bin[key] == self.ip_bin[key]:
                res += self.ip_bin[key]
            else:
                res += "0"
        return self.bin_to_ip(res)

    def ip_minima(self):
        ip_int = []
        ip_int = self.bin_to_ip_int(self.network_bin)
        return str(ip_int[0]) + "." + str(ip_int[1]) + "." + str(ip_int[2]) + "." + str(ip_int[3]+1)

    def ip_maxima(self):
        ip_maxima_bin = ""
        ip_int = []
        for key in range(0,32):
            if key < int(self.netmask_cdr):
                ip_maxima_bin += self.network_bin[key]
            else:
                ip_maxima_bin += "1"
        ip_int = self.bin_to_ip_int(ip_maxima_bin)
        return str(ip_int[0]) + "." + str(ip_int[1]) + "." + str(ip_int[2]) + "." + str(ip_int[3]-1)

    def broadcast(self):
        ip_maxima_bin = ""
        for key in range(0,32):
            if key < int(self.netmask_cdr):
                ip_maxima_bin += self.network_bin[key]
            else:
                ip_maxima_bin += "1"
        return self.bin_to_ip(ip_maxima_bin)

    def result(self):
        for key in range(self.int_host_min,self.int_host_max+1):
            self.res.append(self.bin_to_ip(str(bin(key))[2:]))
        return self.res

ips = IP_Calc("192.168.1.0/25")
print "IP", ips.ip_str
print "Netmask", ips.netmask_str
print "Network", ips.network_str
print "Ip Minima", ips.ip_min_str
print "Ip Maxima", ips.ip_max_str
print "Broadcast", ips.broadcast_str
print "Cantidad de Host", ips.cantidad_host
print "Ips", ips.res
