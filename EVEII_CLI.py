if __name__ != "__main__":
	exit()

name = ""
def select_file(name_):
	name = name_
	open(name + ".txt", "w").close()
	print("New file created")

def set_blueprint_id(id):
	with open(name + ".txt", "w+") as f:
		contents = f.read()
		contents = contents.split("\n")
		contents[0] = "BP: %s" %id
		total_str = ""
		for s in contents:
			total_str += s + "\n"
		f.write(total_str)

while True:
	x = input("/")
	args = x.split()
	if args[0] == "select":
		try:
			select_file(args[1])
		except IndexError:
			print("[!] Enter file name")
	elif args[0] == "set_bp":
		try:
			set_blueprint_id(args[1])
		except IndexError:
			print("[!] Enter blueprint ID")
	else:
		print("Unknown command")
