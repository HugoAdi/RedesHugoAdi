import socket
import threading
import logging
import time
from FTP import *
bufferSize = 1024

logging.basicConfig(level=logging.DEBUG,format='(%(threadName)-2s) %(message)s',)
threading.current_thread().setName("Cliente")

HOST = input("Ingresa la IP del servidor: ")
PORT = 21
bufferSize = 1024
passs='admin'
user='user'

TCPClientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
FTP=protocoloTFP()
FTP.cliente_Connect(TCPClientSocket,HOST,PORT)
FTP.cliente_login(TCPClientSocket,user,passs)
FTP.cliente_DIR(TCPClientSocket)
FTP.cliente_SET(TCPClientSocket)
FTP.cliente_CLOSE(TCPClientSocket)
