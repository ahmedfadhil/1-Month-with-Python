from argparse import ArgumentParser
from data_manager import read_data

from hungrypy.templates import render_context, get_template

parser = ArgumentParser(prog="hungry")
parser.add_argument('type', type=str, choices=['view', 'message'])
# parser.add_argument('did_send', type=str, choices=['true','false'])
parser.add_argument('-id', '--user_id', type=int)
parser.add_argument('-e', '--email', type=str)
args = parser.parse_args()

if args.type == 'view':
    print(read_data(user_id=args.user_id))
    print(read_data(email=args.email))
elif args.type == 'message':
    file_ = 'hungrypy/templates/email_message'
    file_html = 'hungrypy/templates/email_message.html'
    template = get_template(file_).format(name="justin", date="12.12.12", total=None)
    template_text = get_template(file_)
    template_html = get_template(file_html)
    context = {
        "name": "Justin",
        "date": "today",
        "total": "23"
    }
    print(render_context(template_text, context))
    print(render_context(template_html, context))

    print("Send message")
