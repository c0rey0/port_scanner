import socket, sys
# ip_range = '193.104.16.0-255'

ip_range = '194.187.216-219.0-255'

# ip = '77.222.153.190'
ips= list()
port = 3389
def convert_ranges_ips(ip_range):
    list_ip = list()
    sections = ip_range.split('.')
    stable = list()
    for index, section in enumerate(sections):
        if '-' not in section:
            stable.append(section)
        if index == 2 and '-' in section:

            start = int(section.split('-')[0])
            end = int(section.split('-')[1])
            i_start = int(sections[3].split('-')[0])
            i_end = int(sections[3].split('-')[1])
            while end >= start:
                i_res= list()
                i_res.append(str(start))
                i_stable = stable + i_res
                print(i_stable)
                i_start = int(sections[3].split('-')[0])
                i_end = int(sections[3].split('-')[1])
                # import pdb; pdb.set_trace()
                while i_end >= i_start:
                    # import pdb; pdb.set_trace()
                    res = list()
                    res.append(str(i_start))
                    list_ip.append('.'.join(i_stable + res))
                    i_start+=1
                    # import pdb; pdb.set_trace()              
                start+=1
        elif '-' in section and index == 3 and '-' not in sections[2]:
                start = int(section.split('-')[0])
                print(start)
                end = int(section.split('-')[1])
                while end >= start:
                    res = list()
                    res.append(str(start))
                    
                    list_ip.append('.'.join(stable + res))
                    start+=1

    return list_ip
    

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
        with open('success.txt', 'a') as f:
            f.write(f'{ip}\n')
    else:
       print(ip+':'+str(port),' is not available')
    sock.close()



if __name__ == '__main__':
    list_ip = convert_ranges_ips(sys.argv[1])

    for ip in list_ip:
        check_port(ip, port)

    print(ips)

    # check_port('194.44.226.37',3389)    
    # sock.close()