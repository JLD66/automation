import webbrowser
import sys, getopt

def main(argv):
    
    opts, args = getopt.getopt(argv, "o:fb")
    print(opts, args)
    for opt, arg in opts:
        if opt == "-o" and arg == "confluence":
            webbrowser.get("firefox").open_new_tab("https://confluence.logdirect.net")
        elif opt == "-o" and arg == "email":
            webbrowser.get("firefox").open_new_tab("https://outlook.office.com/")
        elif opt == "-o" and arg == "jira":
            webbrowser.get("firefox").open_new_tab("https://jira.logdirect.net/")
        elif opt == "-o" and arg == "eurecia":
            webbrowser.get("firefox").open_new_tab("https://plateforme.eurecia.com/")
        elif opt == "-o" and arg == "clockify":
            webbrowser.get("firefox").open_new_tab("https://app.clockify.me")
        elif opt == "-o" and arg == "bitbucket":
            webbrowser.get("firefox").open_new_tab("https://bitbucket.logdirect.net")
        elif opt == "-f":
            webbrowser.get("firefox").open_new_tab("https://confluence.logdirect.net")
            webbrowser.get("firefox").open_new_tab("https://outlook.office.com/")
            webbrowser.get("firefox").open_new_tab("https://jira.logdirect.net/")
            webbrowser.get("firefox").open_new_tab("https://plateforme.eurecia.com/")
            webbrowser.get("firefox").open_new_tab("https://app.clockify.me")
            webbrowser.get("firefox").open_new_tab("https://bitbucket.logdirect.net")

if __name__ == "__main__":
    main(sys.argv[1:])
