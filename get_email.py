from datetime import datetime

import pyperclip
import sys, getopt

def main(argv):

    print("=== WEBBLANKPAGE EMAIL WITH DATE ===\n")

    opts, args = getopt.getopt(argv, "hpbn:",["name="])

    name = "jonathan"
    env = ""
    
    for opt, arg in opts:
        if opt == "-h":
            print('get_email.py -p <prod tagged email> -b <beta tagged email> -n <:name>\n')
            sys.exit()
        elif opt == "-b":
            env = "beta"
        elif opt == "-p":
            env = "prod"
        elif opt in ("-n", "--name="):
            name = arg

    now = datetime.now()
    date_str = now.strftime("-%d%m%Y-%H%M%S-")
    suffix = "@webblankpage.com"
    result = name + date_str + env + suffix
    pyperclip.copy(result)
    print(result + "\n")

if __name__ == "__main__":
    main(sys.argv[1:])

