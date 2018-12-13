#List all the ips between an ip range.
int_ip = lambda x: '.'.join([str(x/(256**i)%256) for i in range(3,-1,-1)])
ip_int = lambda x:sum([256**j*int(i) for j,i in enumerate(x.split('.')[::-1])])
def get_ips(ip1,ip2):
    ip1_num = ip_int(ip1)
    ip2_num = ip_int(ip2)
    for i in range(ip1_num,ip2_num+1):
        print str(int_ip(i))

ip1 = raw_input('ip1:')
ip2 = raw_input('ip2:')

get_ips(ip1, ip2)

#Did't check the if the ip is correct.