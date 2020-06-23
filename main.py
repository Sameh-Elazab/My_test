from selenium import webdriver
import time
import DMCCount


###### Variabls #####
LoginEmail=input('please insert your login email : ').strip().capitalize()
inpassword = input('Please Type Your Password :')
loopcount=int(input('Please Enter How Many Crimes You Want To Do ?? : '))
driver = webdriver.Chrome()
########################
#### Open The Site #####
driver.get('https://dark-minds.com/?page=logout')
time.sleep(20)
########################
###### type Email ######
Login_Email=driver.find_element_by_name('email')
Login_Email.send_keys(LoginEmail)
time.sleep(2)
#########################
##### Type Passward #####
password=driver.find_element_by_name('password')
password.send_keys(inpassword)
time.sleep(2)
#######################
##### Click Login #####
login=driver.find_element_by_xpath('/html/body/div/div[2]/div[3]/div[1]/div/div[2]/form/div/div[2]/div/button')
login.click()
time.sleep(10)
########################
##### Commit Crime #####
while loopcount >0 :
    DMCCount.Task1()
    loopcount-=1
    print(loopcount)
else:
    print('You Finshed Your Crime Count Down !!')
