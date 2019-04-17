from selenium import webdriver
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from getInfo import get_webinfo,get_id
from login import login,findElement,sendKey


def newRoute(browser,path):	# go to new route 
	goTo = browser.find_element_by_id(path).click()

def goHome(browser,home_id): # go to home page
	home = browser.find_element_by_id(home_id)
	ActionChains(browser).click(home).perform()

def createNew(browser,web_dict):
	# find element fields for to fill info for new analyst
	new_analyst_fields = [web_dict['analysis_name'],web_dict['analysis_description'],web_dict['create_new_button']]
	inputField_tuple = findElement(browser,new_analyst_fields)

	# enter info for new analyst
	new_analyst_list = [new_analyst_dict['Analysis Name'],new_analyst_dict['Analysis Description']]
	sendKey(browser,inputField_tuple,new_analyst_list)

	# click button 'Select Reads'
	select_reads1 = browser.find_element_by_css_selector(web_dict['select_reads_button']).click()
	select_reads2 = browser.find_element_by_css_selector(web_dict['select_reads_button']).click()

	# select 'Enter Sra Run ID' from dropdown menu
	select_menu = browser.find_element_by_xpath(web_dict['select_reads_dropdown']).click()	
	browser.implicitly_wait(2)

def enterSRAid(browser,web_dict,RunID):
	# find SRA Run ID field
	enter_sra_id_fields = [web_dict['run_id_field'],web_dict['run_id_go_button']]
	idField_tuple = findElement(browser, enter_sra_id_fields)
	# enter in SRA RUN ID & click 'Go'
	sra_id = [RunID] 
	sendKey(browser,idField_tuple,sra_id)
	time.sleep(20)

if __name__ == '__main__':
	account_dict = {'username':'jjsmailmail@gmail.com', 'password':'jac123'}
	new_analyst_dict = {'Analysis Name':'test3', 'Analysis Description':'n/a'}
	web_dict = get_webinfo(r'webinfo')
	valid_id = get_id(r'valid_IDs')
	invalid_id = get_id('invalid_IDs')

	browser = login(web_dict,account_dict)
	# click 'new analyst' with valid id
	newRoute(browser,web_dict['create_new'])
	createNew(browser,web_dict)
	valid = enterSRAid(browser,web_dict,valid_id[0])

	# go to Home Page	
	goHome(browser,web_dict['home_page'])
	# click yellow 'analyze your sequencing data', input invalid id
	newRoute(browser,web_dict['yellow_new'])
	createNew(browser,web_dict)
	invalid = enterSRAid(browser,web_dict,invalid_id[0])
	close = browser.find_element_by_css_selector('.btn-danger').click()

	# go to Home Page
	goHome(browser,web_dict['home_page'])
	# click 'quick analyst', input valid id
	newRoute(browser,web_dict['quick_analyst'])
	sra_run_id_btn = browser.find_element_by_xpath(web_dict['quick_analyst_rsa_select']).click()
	valid = enterSRAid(browser,web_dict,valid_id[1])


	# go to Home Page
	goHome(browser,web_dict['home_page'])
	# click 'quick analyst', input invalid id
	newRoute(browser,web_dict['quick_analyst'])
	sra_run_id_btn = browser.find_element_by_xpath(web_dict['quick_analyst_rsa_select']).click()
	invalid = enterSRAid(browser,web_dict,invalid_id[1])

