import selenium
from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys

options = webdriver.ChromeOptions()
options.add_argument('headless')

driver = Chrome(chrome_options = options)
driver.get('https://auth.dadeschools.net/_auth/dsLogon.aspx?ru=aHR0cDovL21kY3BzcG9ydGFsLmRhZGVzY2hvb2xzLm5ldC8=')

username = '*******'
password = '********

usernameBox = driver.find_element_by_id('txtUsername')
usernameBox.send_keys(username)

passwordBox = driver.find_element_by_id('txtPassword')
passwordBox.send_keys(password)

passwordBox.send_keys(Keys.RETURN)

driver.get('https://mdcpsportalapps2.dadeschools.net/PIVredirect/')

def returnCourse(i):
    courses = []
    for course in driver.find_elements_by_css_selector('div.course a')[:8]:
        courses.append(course.get_attribute('innerHTML'))
    return courses[i]

def returnGrade(i):
    grades = []
    for container in driver.find_elements_by_css_selector('td.letter')[:8]:
        try:
            grades.append(container.find_element_by_css_selector('span.percent').get_attribute('innerHTML').strip())
        except selenium.common.exceptions.NoSuchElementException:
            grades.append('No grades yet.')
    return grades[i]

# Temporary testing feature. Integrate the above code into something else.
for i in range(8):
    print(returnCourse(i)+': ' + returnGrade(i))


    

    
