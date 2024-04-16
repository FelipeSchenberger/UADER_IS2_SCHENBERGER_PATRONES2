from pythonping import ping

class Ping:
    def __init__(self):
        pass

    def execute(self, ip_address):
        if ip_address.startswith("192."):
            for _ in range(10):
                response = ping(ip_address, count=1)
                if response._responses[0].success:
                    print(ip_address + " es accesible")
                else:
                    print(ip_address + " no es accesible")
        else:
            print("la direccion no comienza '192.', Abortar la ejecución del ping.")

    def executefree(self, ip_address):
        for _ in range(10):
            response = ping(ip_address, count=1)
            if response._responses[0].success:
                print(ip_address + " es accesible")
            else:
                print(ip_address + " no es accesible")

class PingProxy:
    def __init__(self):
        self.ping = Ping()

    def execute(self, ip_address):
        if ip_address == "192.168.0.254":
            self.ping.executefree("www.google.com")
        else:
            self.ping.execute(ip_address)

# Ejemplo de uso
ping_proxy = PingProxy()
ping_proxy.execute("192.168.0.1")  # Realiza ping a la dirección IP local
ping_proxy.execute("8.8.8.8")       # Realiza ping a una dirección IP pública
ping_proxy.execute("192.168.0.254") # Realiza ping a www.google.com