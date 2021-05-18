'''
Given a valid (IPv4) IP address, return a defanged version of that IP address.
A defanged IP address replaces every period "." with "[.]".
'''


# This solution is a normal solution, but not the fastests
# built in methods tend to faster than your own loops and stuff
# so look to use the built in replace methods! 
def defang(ipString: str) -> str:
    replacement = "[.]"
    defanged = ""
    for char in ipString:
        if char == ".":
            defanged = defanged + replacement
            continue
        defanged = defanged + char
    return defanged

def main():
    address = "1.1.1.1" # Output: "1[.]1[.]1[.]1"   
    defanged = defang(address)
    print(defanged)


main()