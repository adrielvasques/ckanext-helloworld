from flask import Blueprint, render_template, abort

helloworld_blueprint = Blueprint('helloworld', __name__, url_prefix='/hello')

@helloworld_blueprint.route('/world/<eggs>', methods=['GET'])
def hello_world(eggs):
    """A simple hello world page."""
    return f"Hello World! You passed: {eggs}"

# If you had more complex logic or wanted to use templates, you could do something like:
# @helloworld_blueprint.route('/template/<name>', methods=['GET'])
# def hello_template(name):
#     return render_template('helloworld/hello.html', name=name)