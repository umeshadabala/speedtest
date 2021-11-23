import speedtest
s=speedtest.Speedtest()
print('''
███████╗██████╗ ███████╗███████╗██████╗ ████████╗███████╗███████╗████████╗
██╔════╝██╔══██╗██╔════╝██╔════╝██╔══██╗╚══██╔══╝██╔════╝██╔════╝╚══██╔══╝
███████╗██████╔╝█████╗  █████╗  ██║  ██║   ██║   █████╗  ███████╗   ██║   
╚════██║██╔═══╝ ██╔══╝  ██╔══╝  ██║  ██║   ██║   ██╔══╝  ╚════██║   ██║   
███████║██║     ███████╗███████╗██████╔╝   ██║   ███████╗███████║   ██║   
╚══════╝╚═╝     ╚══════╝╚══════╝╚═════╝    ╚═╝   ╚══════╝╚══════╝   ╚═╝                                     
''')
up= s.download() *0.000001
down = s.upload() *0.000001
print('Output is in mbps')
print('pinging your client/server.....')
print('calculating your upload speed....')
print(int(up))
print('calculating your download speed...')
print(int(down))
