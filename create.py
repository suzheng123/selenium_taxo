from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains
from getInfo import get_webinfo,get_id
from login import login,findElement,sendKey
from test_log import create_Log

def goPage(browser,page_id): # go to home page
	page = browser.find_element_by_id(page_id)
	ActionChains(browser).click(page).perform()

def createNew(browser,web_dict,RunID,create_log):
	# find element fields for to fill info for new analysis
	new_analysis_fields = [web_dict['analysis_name'],web_dict['analysis_description'],web_dict['create_new_button']]
	inputField_tuple = findElement(browser,new_analysis_fields)

	# enter info for new analysis
	new_analysis_list = [new_analysis_dict['Analysis Name'],new_analysis_dict['Analysis Description']]
	sendKey(browser,inputField_tuple,new_analysis_list)

	# click button 'Select Reads'
	select_reads1 = browser.find_element_by_css_selector(web_dict['select_reads_button']).click()
	select_reads2 = browser.find_element_by_css_selector(web_dict['select_reads_button']).click()

	# select 'Enter Sra Run ID' from dropdown menu
	select_menu = browser.find_element_by_xpath(web_dict['select_reads_dropdown']).click()	
	time.sleep(2)
	enterSRAid(browser,web_dict,RunID)

	# check runid valid or not
	id_validate = id_check(browser,RunID,create_log)
	if id_validate is False:
		close = browser.find_element_by_css_selector('.btn-danger').click()

def enterSRAid(browser,web_dict,RunID):
	# find SRA Run ID field
	enter_sra_id_fields = [web_dict['run_id_field'],web_dict['run_id_go_button']]
	idField_tuple = findElement(browser, enter_sra_id_fields)
	# enter in SRA RUN ID & click 'Go'
	sra_id = [RunID] 
	sendKey(browser,idField_tuple,sra_id)
	time.sleep(20)

def id_check(browser,id_to_check,create_log):
	valid = ['SRR','ERR','DRR']
	if id_to_check[0:3] in valid:
		create_log.log_write('---------------------------------------\n')
		msg = id_to_check + ' is a valid id\nNew analysis running...\n'
		create_log.log_write(msg)
		return True
	if id_to_check[0:3] not in valid:
		create_log.log_write('---------------------------------------\n')
		msg = 'id: ' + id_to_check + ' currently not acceptable\n'
		create_log.log_write(msg)
		return False

if __name__ == '__main__':
	account_dict = {'username':'jjsmailmail@gmail.com', 'password':'jac123'}
	new_analysis_dict = {'Analysis Name':'new analysis', 'Analysis Description':'n/a'}
	web_dict = get_webinfo(r'webinfo')
	ids = get_id(r'ids')

	browser = login(web_dict,account_dict)
	create_log = create_Log() # log edit result to a txt file
	# click 'new analysis', input valid id
	goPage(browser,web_dict['create_new'])
	createNew(browser,web_dict,ids[0],create_log)
	
	# go to Home Page	
	goPage(browser,web_dict['home_page'])
	# click yellow 'analyze your sequencing data', input invalid id
	goPage(browser,web_dict['yellow_new'])
	createNew(browser,web_dict,ids[1],create_log)

	# go to Home Page	
	goPage(browser,web_dict['home_page'])
	# # click 'quick analysis', input valid id
	goPage(browser,web_dict['quick_analysis'])
	sra_run_id_btn = browser.find_element_by_xpath(web_dict['quick_analysis_rsa_select']).click()
	createNew(browser,web_dict,ids[2],create_log)

	# go to Home Page	
	goPage(browser,web_dict['home_page'])
	# # click 'quick analysis', input invalid id
	goPage(browser,web_dict['quick_analysis'])
	sra_run_id_btn = browser.find_element_by_xpath(web_dict['quick_analysis_rsa_select']).click()
	createNew(browser,web_dict,ids[3],create_log)

	create_log.log_close()