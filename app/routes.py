from flask import redirect, render_template, url_for

from app import app

@app.route('/')
@app.route('/index')
def index():
    return render_template(
        'index.html',
        title='Home'
    )

@app.route('/latencyTest')
def latencyTest():
    return render_template(
        'latencyTest.html',
        title='Latency Test'
    )

@app.route('/<path:path>')
def catch_all(path):
    app.logger.info('User navigated to %s. Redirecting to index page', path)
    return redirect(url_for('index'))
