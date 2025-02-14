def hostname():
    pass


class Server:
    def __init__(self, hostname, ip):
        self.hostname = hostname()
        self.ip = str(ip)
        self.active = False

    def start(self):
        print('server is up and running')

    def __str__(self):
        return