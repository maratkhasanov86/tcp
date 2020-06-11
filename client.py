#Реализация клиента, который отправляет put запросы серверу.
#Таким образом мы отправляем запросы серверу на хранение каких-либо данных.


import socket


import asyncio
async def tcp_echo_client(message, loop):
    reader, writer = await asyncio.open_connection("127.0.0.1",
    10001, loop=loop)
    print("send: %r" % message)
    writer.write(message.encode())
    writer.close()



class client:
    def __init__(self, host, port, timeout = 15):

        self.host = host
        self.port = port
        self.timeout = timeout

    def put(self, key, value, timestamp):
        protocol_str = "put " + key +" " + str(value) + " " + str(timestamp)

        loop = asyncio.get_event_loop()

        loop.run_until_complete(tcp_echo_client(protocol_str, loop))
        loop.close()

        return









