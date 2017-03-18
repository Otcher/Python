from socket import *

path_to_file = raw_input("Enter the path to the directory the file is located in: ")
server_s = socket(AF_INET, SOCK_STREAM)
server_s.bind(("0.0.0.0", 80))
server_s.listen(5)

while(1):
	(client_s, client_addr) = server_s.accept()
	input = client_s.recv(1000)
	
	input_split = input.split(" ")
	if (input_split[0] == "GET" and (len(input_split) >= 2)):
		try:
			f = open(path_to_file + input_split[1], 'r').read()
			file_data = "HTTP/1.0 200 Document Follows\nContent-length: " + str(len(file)) + "\n\n" + f
 		except:
			file_data = "HTTP/1.0 404 File Not Found\n\n"
		client_s.sendall(file_data)
	client_s.shutdown(SHUT_RDWR)
	client_s.close()