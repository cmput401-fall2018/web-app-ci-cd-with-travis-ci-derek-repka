from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
def test_home():
	driver = webdriver.Chrome()
	driver.get("http://162.246.157.227:8000/")
	
	nameelem = driver.find_element_by_id("name")
	assert nameelem != None
	
	aboutelem = driver.find_element_by_id("about")
	assert aboutelem != None

	educationelem = driver.find_element_by_id("education")
	assert educationelem != None

	skillselem = driver.find_element_by_id("skills")
	assert skillselem != None
	
	workelem = driver.find_element_by_id("work")
	assert workelem != None

	contactelem = driver.find_element_by_id("contact")
	assert contactelem != None

	time.sleep(5);
	driver.quit();
