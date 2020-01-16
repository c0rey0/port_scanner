import socket
ip_range = '193.104.16.0-255'
# ip = '77.222.153.190'
ips= list()
port = 3389
def convert_ranges_ips(ip_range):
    list_ip = list()
    sections = list()
    sections = ip_range.split('.')
    stable = list()
    for i, section in enumerate(sections):
        if not '-' in section:
            stable.append(section)
        elif '-' in section:
            start = int(section.split('-')[0])
            print(start)
            end = int(section.split('-')[1])
            while end >= start:
                res = list()
                res.append(str(start))
                
                list_ip.append('.'.join(stable + res))
                start+=1
    print('Ips: \n', list_ip)
    return(list_ip)

def check_port(ip, port):
    print('Checking', ip)
    # try:
    #     ping.verbose_ping(ip, count=3)
    #     delay = ping.Ping(ip, timeout=2000).do()
    # except socket.error as e:
    #     print ("Ping Error:", e)
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)
    result = sock.connect_ex((ip,port))
    if result == 0:
        ips.append(ip)
        print(ip,':',port,' is available')
    else:
       print(ip+':'+str(port),' is not available')
    sock.close()



if __name__ == '__main__':
    # check_port(ip, port)
    list_ip = convert_ranges_ips(ip_range)
    # sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    for ip in list_ip:

        check_port(ip, port)
    print(ips)

    # check_port('193.104.16.205',3389)    
    # sock.close()