import webbrowser
import requests
from selenium import webdriver
import click
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils import *

# 3 Go to https://useinsider.com/careers/quality-assurance/, click “See all QA jobs”, filter jobs by Location: “Istanbul, Turkey”, and Department: “Quality Assurance”, check the presence of the job list
# 3.1 Go to https://useinsider.com/careers/quality-assurance/
driver,wait = get_driver_and_wait("https://useinsider.com/careers/quality-assurance/")
        
# 3.2 click “See all QA jobs”, filter jobs by Location: “Istanbul, Turkey”, and Department: “Quality Assurance”
wait_until_and_click(wait, By.XPATH, "//*[@id='page-head']/div/div/div[1]/div/div/a")

#cookie kabul
click_to_element(driver, By.ID, "wt-cli-accept-all-btn")

# filter jobs by Location: “Istanbul, Turkey”,
selected_filter = 'Istanbul, Turkiye'    
filter_container_path = "//*[@id='top-filter-form']/div[1]/span/span[1]/span/span[2]"
filter_by_id = "select2-filter-by-location-results"
select_filter(wait, driver, selected_filter, filter_container_path, filter_by_id)


# filter jobs by Department: “Quality Assurance”,
selected_filter = 'Quality Assurance'
filter_container_path = '//*[@id="select2-filter-by-department-container"]'
filter_by_id = "select2-filter-by-department-results"
select_filter(wait, driver, selected_filter, filter_container_path, filter_by_id)

#check the presence of the job list
job_list_element = find_element(driver, By.ID, "jobs-list")
job_lists = find_elements(job_list_element, By.CLASS_NAME, "position-list-item")
if job_list != []: print("job exists.")
else: print("job not exists")

#Check that all jobs’ Position contains “Quality Assurance”, Department contains “Quality Assurance”, and Location contains “Istanbul, Turkey”
for job in job_lists:
    
    #check Position contains “Quality Assurance”
    property_name = "position-title"
    target_property = "Quality Assurance"
    p1 = check_job_properties(job, property_name, target_property)
    
    #Department contains “Quality Assurance”,
    property_name = "position-department"
    target_property = "Quality Assurance"
    p2 = check_job_properties(job, property_name, target_property)
    
    #Location contains “Istanbul, Turkey”
    property_name = "position-location"
    target_property = "Istanbul, Turkey" # burası istanbul, Turkiye dönüyor.
    p3 = check_job_properties(job, property_name, target_property)     
    
    if p1 and p2 and p3:
        print("ALL PROPERTIES CORRECT")
    else:
        print("False")

#click view role button and this action redirects us to the Lever Application form page
for job in job_lists:
    view_role_button = find_elements(job, By.TAG_NAME, "a")
    for button in view_role_button:
        view_role_url =  button.get_attribute("href")
        driver,wait = get_driver_and_wait(view_role_url)