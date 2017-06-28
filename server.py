#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  server.py
#  
#  Copyright 2017  <pi@raspberrypi>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  


import socket
import sys
PORT_NUMBER = 5002
SIZE = 4096


hostname = socket.gethostbyname('0.0.0.0')


mySocket = socket.socket( socket.AF_INET, socket.SOCK_STREAM)
mySocket.bind( (hostname, PORT_NUMBER) )
mySocket.listen(1)
(conn, addr) = mySocket.accept()

print ("Test server listening on port {0}\n".format(PORT_NUMBER))

while True:
	(data, address) = conn.recv(SIZE)
	print data
	conn.sendall(data)
sys.exit()