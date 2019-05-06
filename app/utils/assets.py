from flask_assets import Bundle, Environment
from os import path

def init_assets(app):
    with app.app_context():
        env = Environment(app)
        env.load_path = [path.join(path.dirname(__file__), '..', 'static')]

        # App Enging doesn't support automatic building
        # so only auto build if in debug mode
        env.auto_build = app.debug
        app.logger.info('auto_build set to {}'.format(
            env.auto_build
        ))

        # Make sure this file is shipped
        env.manifest = 'file'

        bundles = {

            'index_js': Bundle(
                'js/common.js',
                output='gen/index.js'),

            'index_css': Bundle(
                'css/bootstrap-extensions.css',
                'css/common.css',
                'css/index.css',
                output='gen/index.css'),

            'latencyTest_js': Bundle(
                'js/common.js',
                'js/latencyTest.js',
                output='gen/latencyTest.js'),

            'latencyTest_css': Bundle(
                'css/bootstrap-extensions.css',
                'css/common.css',
                'css/latencyTest.css',
                output='gen/latencyTest.css'),
        }
         
        env.register(bundles)
        return bundles

if __name__ == '__main__':
    bundles = init_assets()
    for bundleKey in bundles:
        bundles[bundleKey].build()
