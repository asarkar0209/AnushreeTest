from xpresso.ai.core.data.connections.external_connectors.alluxiopy import alluxio

import telnetlib
from io import BytesIO

class AlluxioConn:
    def __init__(self):


        self.alluxio_host_ip = '10.0.23.22'
        self.alluxio_host_port = 39999

    def connect(self):
        try:
            client = alluxio.Client(self.alluxio_host_ip, self.alluxio_host_port)
            telnetlib.Telnet(self.alluxio_host_ip, self.alluxio_host_port)
            return client
        except Exception as exc:
            print(exc)



if __name__=="__main__":
    axcon=AlluxioConn()
    print(axcon.connect())
