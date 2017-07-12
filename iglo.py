#!/usr/bin/python3

import socket

PORT = 8080
COMMANDS = {
    'ON': b'\xfe\xef\x04\xa3\x00\x12\x4a',
    'OFF': b'\xfe\xef\x04\xa3\x00\x11\x4b'
}

class IGlo():
    
    def __init__(self, iglo_ip_addr):
        self.ip_addr = iglo_ip_addr
        self._connect()
        self.send_command('ON')
    
    def get_status(self):
        return self._status

    def send_command(self, cmd):
        if cmd in COMMANDS:
            self._status = cmd
            self._socket.send(COMMANDS[cmd])
        return self.status

    def _connect(self):
        self._socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._socket.connect((self.ip_addr, PORT))

