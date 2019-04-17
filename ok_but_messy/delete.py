from selenium import webdriver
import time
from login import login,findElement,sendKey
from getInfo import get_webinfo
from create import goHome
from test_log import delete_Log

def clickIcon(browser,icon_css):
	icon_element = browser.find_element_by_css_selector(icon_css).click()

def delete(browser, delete_icon, delete_action,web_dict,delete_log):
	clickIcon(browser,delete_icon)
	time.sleep(3)
	clickIcon(browser,delete_action)
	delete = delete_action_check(web_dict,delete_action,delete_log)
	del_log(delete,delete_log)

def delete_action_check(web_dict,delete_action,delete_log):
	delete = False
	if delete_action == web_dict['delete_confirm_css']:
		delete = True
	return delete

def del_log(delete,delete_log):
	if delete == True:
		delete_log.log_write('----------------\n')
		delete_log.log_write('Analysis deleted\n')
	if delete == False:
		delete_log.log_write('----------------\n')
		delete_log.log_write('Nothing changed\n')

if __name__ == '__main__':
	account_dict = {'username':'jjsmailmail@gmail.com', 'password':'jac123'}
	web_dict = get_webinfo(r'webinfo')

	browser = login(web_dict,account_dict)
	delete_log = delete_Log() # log edit result to a txt file
	
	# delete by clicking 'trash icon', confirm delete
	delete(browser,web_dict['delete_icon_css'],web_dict['delete_confirm_css'],web_dict,delete_log)

	# back to home page
	goHome(browser,web_dict['home_page'])
	# delete by clicking 'trash icon', cancel delete
	delete(browser,web_dict['delete_icon_css1'],web_dict['delete_cancel_css'],web_dict,delete_log)

	# back to 'analysis list'
	goHome(browser,web_dict['analyst_list_id'])
	# delete by clicking 'trash icon', confirm delete
	delete(browser,web_dict['delete_icon_css2'],web_dict['delete_confirm_css'],web_dict,delete_log)
	delete_log.log_close()
