class Return_ips(object):
    """Esta clase recibe un string con una cadena y resuelve IPs validas"""
    res =[]

    def __init__(self,cadena):
        self.cadena = cadena

    def ip_to_bin(self,ip):
        return '.'.join([bin(int(x)+256)[3:] for x in ip.split('.')])

    def bin_to_ip(self,bin_str):
        ip = ""
        num = bin_str.split(".")
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

    def create_netmask_in_bin(self,bit_netmask_str):
        netmask_str = ""
        for key in range(0,32):
            if key == 8 or key == 16 or key == 24:
                netmask_str += "."
            if key > int(bit_netmask_str)-1:
                netmask_str += "0"
            else:
                netmask_str += "1"
        return netmask_str

    def dir_network(self):
        resultado = ["","","",""]
        network_parts = self.cadena.split("/")
        octets_str = network_parts[0].split(".")
        octets_bin = self.ip_to_bin(network_parts[0]).split(".")
        netmask_bin = self.create_netmask_in_bin(network_parts[1]).split(".")
        netmask_srt = self.bin_to_ip(netmask_bin[0] + "." +netmask_bin[1] + "."+netmask_bin[2] + "."+netmask_bin[3])
        for i in range(0,4):
            for j in range(0,8):
                if netmask_bin[i][j] == "1" and octets_bin [i][j] == "1":
                    resultado[i] += "1"
                else:
                    resultado[i] += "0"
        return self.bin_to_ip(resultado[0] + "." +resultado[1] + "."+resultado[2] + "."+resultado[3])

    def ip_minima(self):
        network_parts = self.cadena.split("/")
        direccion_red_string = self.dir_network().split(".")
        direccion_red_int =[]
        for key in direccion_red_string:
            direccion_red_int.append(int(key))

        direccion_red_int[3] += direccion_red_int[3] + 1
        print direccion_red_int

#    def ip_maxima(self):
#        network_parts = self.cadena.split("/")
#        direccion_red_string = self.dir_network().split(".")
#        netmask_bin = self.create_netmask_in_bin(network_parts[1]).split(".")
#        direccion_red_bin = self.ip_to_bin(network_parts[0]).split(".")
#        for i in range(0,4):
#            for j in range(0,8):
#if netmask_bin[i][j] == "1" and direccion_red_bin [i][j] == "1":
#                    pass
#                else:
#                    direccion_red_bin[i][j] = "1"
#       return direccion_red_bin

    def ips(self):
        network_parts = self.cadena.split("/")

        return res


print Return_ips("192.168.195.1/22").ip_minima()
print Return_ips("192.168.195.1/22").dir_network()
#print Return_ips("192.168.195.1/22").