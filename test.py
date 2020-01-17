# ip_range = '194.187.216-219.0-255'
ip_range = '193.104.16.0-255'

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
print(list_ip)


