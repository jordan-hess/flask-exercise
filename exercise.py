from flask import Flask, redirect, url_for

app = Flask(__name__)


@app.route('/user/<name>')
def user_page(name):
    if name == "godwin":
        return redirect(url_for('admin', name=name))
    else:
        return redirect(url_for('guest_page', name=name))


@app.route('/admin/<name>')
def admin(name):
    return "Admin %s has logged in." % name


@app.route('/geust/<name>')
def guest_page(name):
    return "I am the guest page. My name is %s" % name


if __name__ == '__main__':
    app.debug = True
    app.run()
