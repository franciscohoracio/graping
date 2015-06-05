class IP_Calc(object):
    """Esta clase recibe un string con una cadena y resuelve IPs validas"""
    res =[]

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

    def ip_to_bin(self,ip):
        return ''.join([bin(int(x)+256)[3:] for x in ip.split('.')])

    def bin_to_ip(self,bin_str):
        ip = ""
        ipt = ""
        for key in range(0,32):
            if key == 8 or key == 16 or key == 24:
                ipt += "."
            ipt +=bin_str[key]
        num = ipt.split(".")
        for i in num:
            bandera = 128
            octeto = 0
            for j in range(0,len(i)):
                if i[j] == "1":
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
        ip_str = ""
        ipt = ""
        for key in range(0,32):
            if key == 8 or key == 16 or key == 24:
                ipt += "."
            ipt +=self.network_bin[key]
        num = ipt.split(".")
        for i in num:
            bandera = 128
            octeto = 0
            for j in range(0,len(i)):
                if i[j] == "1":
                    octeto +=bandera
                bandera = bandera/2
            ip_int.append(octeto)
            ip_str = ""
        return str(ip_int[0]) + "." + str(ip_int[1]) + "." + str(ip_int[2]) + "." + str(ip_int[3]+1)

    def ip_maxima(self):
        ip_maxima_bin = ""
        ip_int = []
        ipt = ""
        for key in range(0,32):
            if key < int(self.netmask_cdr)-1:
                ip_maxima_bin += self.network_bin[key]
            else:
                ip_maxima_bin += "1"
        for key in range(0,32):
            if key == 8 or key == 16 or key == 24:
                ipt += "."
            ipt +=ip_maxima_bin[key]
        num = ipt.split(".")
        for i in num:
            bandera = 128
            octeto = 0
            for j in range(0,len(i)):
                if i[j] == "1":
                    octeto +=bandera
                bandera = bandera/2
            ip_int.append(octeto)
            ip_str = ""
        return str(ip_int[0]) + "." + str(ip_int[1]) + "." + str(ip_int[2]) + "." + str(ip_int[3]-1)

    def broadcast(self):
        ip_maxima_bin = ""
        for key in range(0,32):
            if key < int(self.netmask_cdr)-1:
                ip_maxima_bin += self.network_bin[key]
            else:
                ip_maxima_bin += "1"
        return self.bin_to_ip(ip_maxima_bin)

    def ips(self):
        pass



ips = IP_Calc("192.168.34.0/21")
print "IP", ips.ip_str
print "Netmask", ips.netmask_str
print "Network", ips.network_str
print "Ip Minima", ips.ip_minima()
print "Ip Maxima", ips.ip_maxima()
print "Broadcast", ips.broadcast_str