import webbrowser
import requests
from selenium import webdriver
import click
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def get_driver_and_wait(url):

    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(url)
    wait = WebDriverWait(driver, 20)
    print('siteye girildi.')
    
    return driver, wait

def wait_until_and_click(wait, by_type, locater):
    element = wait.until(EC.element_to_be_clickable((by_type, locater)))
    click(element)    
    print("wait_until_and_click.")
    
    return  element


def click(element):
    try:
        element.click()
    except Exception as e:
        print(f'Error:  {e}')

def wait_until_and_click(wait, by_type, locater):
    element = wait.until(EC.element_to_be_clickable((by_type, locater)))
    click(element)    
    print("wait_until_and_click.")
    
    return  element

def find_element(driver, by_type, locater):
    element = driver.find_element(by_type, locater)
    print("find_element")
    
    return element

def find_elements(driver, by_type, locater):
    elements = driver.find_elements(by_type, locater)
    print("find_elements")
    
    return elements
    
def click_to_element(driver, by_type, locater):
    find_element(driver, by_type, locater).click()
    print("click_to_element")
    
def click_selected_filter(results_options, selected_filter):
    
    filtered_element = None
    for option in results_options:
        if option.text == selected_filter:
            filtered_element  = option
            print(f'filtered_element tespit edildi: {option.text}')
            return filtered_element
            

def select_filter(wait, driver, selected_filter, filter_container_path, filter_by_id):
        
    filter_list = list()
    while True:
        
        element = wait_until_and_click(wait, By.XPATH, filter_container_path)
        results = find_element(driver, By.ID, filter_by_id)
        results_options = find_elements(results, By.CLASS_NAME, "select2-results__option")
        
        for option in results_options:
            filter_list.append(option.text)
        
        if filter_list == ['All']:
            sleep(10)
            click(element)
            print('!tekrar dene')
            
        else:
            sleep(10)
            print('lokasyonlar listelendi.')
            break 
        
    selected_element = click_selected_filter(results_options, selected_filter)
    click(selected_element)
    
def check_job_properties(driver, property_name, target_property):
    
    property = find_element(driver, By.CLASS_NAME, property_name)
    print(property.text)
    if target_property in property.text:
        print("True")
        return True
    else:
        print("false")
        print(f"This propety's ({property_name}) condition ({target_property}) is false: {property.text}")
        return False
