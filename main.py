import requests
import time
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException, InvalidElementStateException

def internet_on():
    try:
        response=requests.head("http://www.google.com", timeout=1)
        return True
    except requests.exceptions.Timeout as err:
    	print("Cannot connect to network in 0.1 seconds")
    except Exception as err:
    	pass
    return False

def siti_connector(username, password):
	driver = webdriver.PhantomJS() # or add to your PATH
	driver.set_window_size(1024, 768) # optional
	driver.get('http://10.10.0.1/24online/webpages/client.jsp')
	user_id_field = driver.find_element_by_name("username")
	password_field = driver.find_element_by_name("password")

	user_id_field.send_keys(username)
	password_field.send_keys(password)

	password_field.submit()
	driver.save_screenshot('screen.png') # save a screenshot to disk


def loop_connector(username, password):
	while True:
		if internet_on():
			time.sleep(5)
		else:
			try:
				siti_connector(username, password)
				notify("Connected! Enjoy", "Your internet is now connected.")
			except NoSuchElementException as e:
				print("May be you have some serious trouble")
			except InvalidElementStateException as e:
				print("I guess you are connected to internet!")
			finally:
				pass

# The notifier function
def notify(title, message):
    t = '-title {!r}'.format(title)
    # s = '-subtitle {!r}'.format(subtitle)
    m = '-message {!r}'.format(message)
    p = '-appIcon favicon.ico'
    os.system('terminal-notifier {}'.format(' '.join([m, t, p])))

loop_connector("username", "password)