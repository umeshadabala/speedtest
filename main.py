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
up= s.download()
down = s.upload()
print('Output is in megabytes/s')
print('pinging your client/server.....')
print('calculating your upload speed....')
print('calculating your download speed...')


def convert_bytes(bytes_number):
    tags = ["Byte", "Kilobyte", "Megabyte", "Gigabyte", "Terabyte"]

    i = 0
    double_bytes = bytes_number

    while (i < len(tags) and bytes_number >= 1024):
        double_bytes = bytes_number / 1024.0
        i = i + 1
        bytes_number = bytes_number / 1024

    return str(round(double_bytes, 2))
print(convert_bytes(up))
print(convert_bytes(down))
