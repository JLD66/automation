import argparse
import webbrowser

#create the parser
parser = argparse.ArgumentParser()
subparser = parser.add_subparsers(dest='command')
angela = subparser.add_parser('angela')
padre = subparser.add_parser('padre')
christin = subparser.add_parser('christin')
grafana = subparser.add_parser('grafana')
outlook = subparser.add_parser('outlook')
confluence = subparser.add_parser('confluence')
clockify = subparser.add_parser('clockify')
eurecia = subparser.add_parser('eurecia')
jira = subparser.add_parser('jira')
bitbucket = subparser.add_parser('bitbucket')



#add arguments

angela.add_argument('--prod', action="store_true")
angela.add_argument('--wordpress', action='store_true')
angela.add_argument('--l', action='store_true')

padre.add_argument('--prod', action="store_true")
padre.add_argument('--wordpress', action='store_true')
padre.add_argument('--l', action='store_true')

christin.add_argument('--prod', action="store_true")
christin.add_argument('--wordpress', action='store_true')
christin.add_argument('--l', action='store_true')

brand_list = ['christin', 'padre', 'angela']

#parse arguments
args = parser.parse_args()

prefix = 'https://'
wp = 'www.'
beta= ''
site=''

#create the website string
if args.command in brand_list and args.wordpress:
    wp = 'wordpress.'
if args.command in brand_list and args.wordpress and args.prod:
    prefix = 'http://'
if args.command in brand_list and not args.prod:
    beta = 'beta.'
    prefix = 'http://'
if args.command == 'angela':
    site='guardian-angel-messenger.com'
if args.command == 'padre':
    site='guardian-angel-reading.com'
if args.command == 'christin':
    site = 'christin-medium.com'
if args.command in brand_list and args.l:
    wp = 'wordpress'
    site = site + '/admin'
connect_str = prefix + wp + beta + site

if args.command == 'grafana':
    connect_str = 'https://grafana.logdirect.net'
if args.command == 'confluence':
    connect_str = 'https://confluence.logdirect.net'
if args.command == 'outlook':
    connect_str = 'https://outlook.office.com'
if args.command == 'clockify':
    connect_str = 'https://app.clockify.me'
if args.command == 'bitbucket':
    connect_str = 'https://bitbucket.logdirect.net'
if args.command == 'jira':
    connect_str = 'https://jira.logdirect.net'
if args.command == 'eurecia':
    connect_str = 'https://plateforme.eurecia.com'

webbrowser.get('firefox').open_new_tab(connect_str)

