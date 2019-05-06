import os
import threading
from wsgiref import simple_server
from wsgiref.simple_server import WSGIRequestHandler
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

os.environ['DB'] = 'test_db.json'
from pa.ui import app

chrome_options = Options()
# chrome_options.add_argument("headless")

CHROME_DRIVER = os.path.join(os.path.join(os.path.dirname(os.path.dirname(__file__)), 'driver'), 'chromedriver.exe')


def before_feature(context, feature):
    context.server = simple_server.WSGIServer(("", 5000), WSGIRequestHandler)
    context.server.set_app(app)
    context.pa_app = threading.Thread(target=context.server.serve_forever)
    context.pa_app.start()

    context.browser = webdriver.Chrome(options=chrome_options, executable_path=CHROME_DRIVER)
    context.browser.set_page_load_timeout(time_to_wait=200)


def after_feature(context, feature):
    context.browser.quit()
    context.server.shutdown()
    context.pa_app.join()