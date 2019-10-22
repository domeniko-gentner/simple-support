#!/usr/bin/env python3
from flask import Flask, render_template, request, redirect, url_for
from support_mail import send_mail
import wsgiserver
support_app = Flask(__name__)


@support_app.route('/')
def index():
    return render_template('index.tpl')


@support_app.route('/send-email', methods=['POST'])
def process_mail():
    if request.method == 'POST':
        send_mail(request.form['form-employee'],
                  request.form['form-subject'],
                  request.form['form-room'],
                  request.form['form-body'])
        return redirect(url_for('index'))


if __name__ == "__main__":
    # DAS IST NUR FUER DIE ENTWICKLUNG!
    # support_app.jinja_env.auto_reload = True
    # support_app.config['TEMPLATES_AUTO_RELOAD'] = True
    # support_app.run('10.10.10.1', port=80, debug=True)
    server = wsgiserver.WSGIServer(support_app, host="WARBOSS", port=80)
    server.start()
