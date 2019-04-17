from selenium import webdriver
import time
from selenium.webdriver.support.ui import WebDriverWait
from getInfo import get_webinfo,get_id
from login import login,findElement,sendKey
from create import goHome
from test_log import edit_Info

def clickIcon(browser,icon_css):
	icon_element = browser.find_element_by_css_selector(icon_css).click()

def editAnalyst(browser,web_dict,edit_list,edit_text_list,edit_icon):
	editField_tuple = findElement(browser,edit_list)
	if edit_icon == web_dict['edit_update_css']: # confirm update
		sendKey(browser,editField_tuple,edit_text_list)
		browser.refresh()
		return True

	for i in range (0, len(editField_tuple)-1): # cancel update
		editField_tuple[i].send_keys(edit_text_list[i])
	clickIcon(browser,edit_icon)
	browser.refresh()
	return False

def updateResult(updated, new_text_list,edit_log):
	field = ['Name: ', 'Description: ']
	if updated == True:
		edit_log.log_write('---------------------------------------------------\n')
		edit_log.log_write('Updated confirmed! Following fields were appended by text: \n')
		for i in range(0,len(field)):
			new = field[i] + new_text_list[i]
			edit_log.log_write(new)
			edit_log.log_write('\n')
	if updated == False:
		edit_log.log_write('---------------------------------------------------\n')
		edit_log.log_write('Nothing changed\n')


if __name__ == '__main__':
	account_dict = {'username':'jjsmailmail@gmail.com', 'password':'jac123'}
	edit_text = [' updated',' updated']
	web_dict = get_webinfo(r'webinfo')

	browser = login(web_dict,account_dict)
	edit_log = edit_Info() # log edit result to a txt file
	edit = False
	clickIcon(browser,web_dict['edit_icon_css']) # click edit icon
	edit_fields = [web_dict['analysis_name'],web_dict['analysis_description'],web_dict['edit_update_css']]
	# edit 
	edit = editAnalyst(browser,web_dict,edit_fields,edit_text,web_dict['edit_update_css'])
	updateResult(edit,edit_text,edit_log)

	# go to 'analyst list' page
	clickIcon(browser,web_dict['analyses_css'])
	clickIcon(browser,web_dict['edit_icon_css2'])
	# edit 
	edit = editAnalyst(browser,web_dict,edit_fields,edit_text,web_dict['edit_cancel_css'])
	updateResult(edit,edit_text,edit_log)

	# go to 'analyst result'
	result = browser.find_element_by_xpath('//*[@id="ember776"]').click()
	time.sleep(2)
	browser.find_element_by_xpath('//*[@id="ember975"]').click()
	clickIcon(browser,web_dict['edit_analysis_icon'])
	edit = editAnalyst(browser,web_dict,edit_fields,edit_text,web_dict['edit_update_css'])
	updateResult(edit,edit_text,edit_log)
	edit_log.log_close()

	goHome(browser,web_dict['home_page2'])

