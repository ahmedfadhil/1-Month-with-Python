import os


# getting the template file path
def get_template_path(path):
    file_path = os.path.join(os.getcwd(), path)
    if not os.path.isfile(file_path):
        raise Exception("This is not a valid template path %s" % (file_path))
    else:
        print("The path:")
    return file_path


def get_template(path):
    file_path = get_template_path(path)
    return open(file_path).read()


def render_context(template_string, context):
    return template_string.format(**context)


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
print(render_context(template_text,context))
print(render_context(template_html,context))
