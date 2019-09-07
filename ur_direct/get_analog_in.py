from utilities import send_script, is_available

script = ""
script += "def program():\n"
script += "\tvalue = get_analog_in(0)\n"
script += "\ttextmsg(value)\n"
script += "\tvalue = get_analog_in(1)\n"
script += "\ttextmsg(value)\n"
script += "end\n"
script += "program()\n\n\n"

def print_analog_in(ur_ip):

    global script
    print(script)

    ur_available = is_available(ur_ip)

    if ur_available:
        send_script(ur_ip, script)

if __name__ == "__main__":
	ur_ip = "192.168.10.13"
	print_analog_in(ur_ip)