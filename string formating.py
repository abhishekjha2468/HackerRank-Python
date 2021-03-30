
def print_formatted(i):
	for a in range (1,i+1):
		print(" "*(+len(str(i))-len(str(a))),str(a)," "*((len(oct(i)))-len(oct(a))),oct(a)[2::]," "*((len(hex(i)))-len(hex(a))),hex(a)[2::].upper()+" "*(len(bin(i))-len(bin(a))),bin(a)[2::])