from selenium import webdriver
import time
from selenium.webdriver.support.ui import WebDriverWait
from getInfo import get_webinfo


def openBrowser():			#open browser
	browser = webdriver.Firefox(executable_path='/Users/JacZh/Downloads/webdrivers/geckodriver')
	browser.set_window_size(920,750)
	return browser

def openUrl(browser, url):	#open url
	browser.get(url)

def findElement(browser, fields): #return input fields, (input MUST be list[])
	field_list = []
	if len(fields) > 1:
		for i in range(0,len(fields)-1):
			field_list.append(browser.find_element_by_id(fields[i]))
	field_list.append(browser.find_element_by_css_selector(fields[-1])) # find the button
	return field_list

def sendKey(browser,inputField_tuple,keys_tuple):	# send keys to input fields
	print ('send key: ',keys_tuple)
	for i in range (0, len(inputField_tuple)-1):
		inputField_tuple[i].send_keys(keys_tuple[i])
	time.sleep(5)
	inputField_tuple[-1].click()

def login_check(browser,err_selector):	# check account log in success or not
	result = False
	browser.implicitly_wait(5)
	try:
		err = browser.find_element_by_xpath(err_selector)
		print (err.text)
	except:
		print ('Logged in sucessfully!')
		result = True
	return result

def login(web_dict,account_dict):
	browser = openBrowser()
	url_open = openUrl(browser, web_dict['url'])

	signin = browser.find_element_by_partial_link_text(web_dict['login_text']).click()
	browser.implicitly_wait(2)

	login_fields_list = [web_dict['account_email'],web_dict['account_pwd'], web_dict['login_button']]
	inputField_tuple = findElement(browser,login_fields_list)

	account_list = [account_dict['username'],account_dict['password']]
	sendKey(browser,inputField_tuple,account_list)

	login_check(browser,web_dict['login_error'])

	return browser


if __name__ == '__main__':

	account_dict = {'username':'jjsmailmail@gmail.com', 'password':'jac123'}
	web_dict = get_webinfo(r'webinfo')

	login(web_dict,account_dict)
