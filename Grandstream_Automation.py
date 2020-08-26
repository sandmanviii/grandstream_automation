#!/usr/bin/python


#Gonna actually finish this one. Grandstream automation
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

#VALUES TO BE CHANGED
ip_addr = "10.1.0.46" 
number = "8597444904"
passwd = "5(9sS054" 
domain = "sip.univergeblue.com"



#To open ATA IP once obtained
driver = webdriver.Chrome(executable_path='C:\\Users\\sande\\Downloads\\chromedriver_win32\\chromedriver.exe')
driver.get('http://' + ip_addr)

#Enter password
password = driver.find_element_by_name("P2")
password.send_keys("admin")

#Click login button
loginButton = driver.find_element_by_name("Login")
loginButton.submit()

#Configure profile 1
prof1 = driver.find_element_by_xpath("//a[contains(@href, 'config_a1')]").click()

sip_server = driver.find_element_by_name("P47")
sip_server.send_keys(domain)

#dns_mode = driver.find_element_by_("1")
dns_mode = driver.find_element_by_xpath("//*[@name='P103'][@value='1']")
dns_mode.click()

reg_ip = driver.find_element_by_xpath("//*[@name='P28092'][@value='1']").click()

unreg_reboot = driver.find_element_by_xpath("//*[@name='P81'][@value='1']").click()

outgoing_unreg = driver.find_element_by_xpath("//*[@name='P109'][@value='0']").click()

p_assert = driver.find_element_by_xpath("//*[@name='P2339'][@value='1']").click()

disable_call_wait = driver.find_element_by_xpath("//*[@name='P91'][@value='1']").click()

disable_call_wait_id = driver.find_element_by_xpath("//*[@name='P714'][@value='1']").click()

disable_call_wait_tone = driver.find_element_by_xpath("//*[@name='P186'][@value='1']").click()

loop_current_disco = driver.find_element_by_xpath("//*[@name='P892'][@value='1']").click()

loop_current_duration = driver.find_element_by_name("P856")
loop_current_duration.send_keys(Keys.CONTROL + "a")
loop_current_duration.send_keys(Keys.DELETE)
loop_current_duration.send_keys("600")

apply = driver.find_element_by_name("apply").click()

time.sleep(3)
#Configure Lines
fxs_ports = driver.find_element_by_xpath("//a[contains(@href, 'config_fxs')]").click()

userID = driver.find_element_by_name("P4060").send_keys(number)
authID = driver.find_element_by_name("P4090").send_keys(number)
authPass = driver.find_element_by_name("P4120").send_keys(passwd)
name = driver.find_element_by_name("P4180").send_keys(number)
request_uri = autID = driver.find_element_by_name("P4669").send_keys(number)
#Make sure first port is enabled at least
enable_port= driver.find_element_by_xpath("//*[@name='P4595'][@value='1']").click()

apply_fxs = driver.find_element_by_name("apply").click()
#Wrap it up
time.sleep(2)
driver.close()
driver.quit()



