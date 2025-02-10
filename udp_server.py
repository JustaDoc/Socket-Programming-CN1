import socket
import os
import hashlib  # needed to verify file hash


IP = '127.0.0.1'  # change to the IP address of the server
PORT = 12000  # change to a desired port number
BUFFER_SIZE = 1024  # change to a desired buffer size


def get_file_info(data: bytes) -> (str, int):
    return data[8:].decode(), int.from_bytes(data[:8],byteorder='big')


def upload_file(server_socket: socket, file_name: str, file_size: int):
    # create a SHA256 object to verify file hash
    # TODO: section 1 step 5 in README.md file

    # create a new file to store the received data
    with open(file_name+'.temp', 'wb') as file:
        # TODO: section 1 step 7a - 7e in README.md file
        pass  # replace this line with your code for section 1 step 7a - 7e

    # get hash from client to verify
    # TODO: section 1 step 8 in README.md file
    # TODO: section 1 step 9 in README.md file


def start_server():
    # create a UDP socket and bind it to the specified IP and port
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind((IP, PORT))
    print(f'Server ready and listening on {IP}:{PORT}')

    try:
        while True:
            # TODO: section 1 step 2 in README.md file
            # expecting an 8-byte byte string for file size followed by file name
            # TODO: section 1 step 3 in README.md file
            # TODO: section 1 step 4 in README.md file
            upload_file(server_socket, file_name, file_size)
    except KeyboardInterrupt as ki:
        pass
    except Exception as e:
        print(f'An error occurred while receiving the file:str {e}')
    finally:
        server_socket.close()


if __name__ == '__main__':
    start_server()
