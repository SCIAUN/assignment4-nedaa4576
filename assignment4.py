
import nmap

def port_scanner(ports):
    nm = nmap.PortScanner()
    nm.scan(ports, '21-1000')
    for host_names in nm.all_hosts():
        ports = nm[host_names].get('tcp')
        writess(ports)

    return ports


def writess(contents):
    f = open('Natije', 'w')
    s = str(contents)
    f.write(s)

    pass


def main():
    hosts = [
        'blogfa.com',
        'w3schools.com',
        'hadipoor.ir'
        'google.com',
    ]

    for host_name in hosts:
        port_scanner(host_name)

main()
