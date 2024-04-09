#Name: Lakshmi Prabha
#Program : 
"""
Visit the url, https://www.instagram.com/guviofficial/ 
Try to fetch the following using Python Selenium
1. Followers of the webpage
2. Following of the webpage 
"""
#Date : 03 April 2024
#Version: 1
#Python Version: 3.12.0


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.common.exceptions import NoSuchElementException


# A class to interact with an Instagram page and retrieve followers and following counts.

class InstagramPageInfo:

    # Constructor method to initialize the class.
    def __init__(self, url):
        self.url = url
        # Initialize Firefox WebDriver using GeckoDriverManager to handle driver management
        self.driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
        # Set implicit wait to 10 seconds to handle dynamic page elements
        self.driver.implicitly_wait(10)

    # Method to start the browser and navigate to the Instagram page.
    def booting_function(self):

        try:
            # Maximize the browser window
            self.driver.maximize_window()
            # Open the provided URL
            self.driver.get(self.url)
            return True
        except Exception as e:
            # Print error message if browser fails to start
            print(f"ERROR: Unable to start the browser: {e}")
            return False

    # Method to close the browser.
    def shutdown(self):
        self.driver.quit()
        return True
    
    # Method to retrieve the followers count from the Instagram page.
    def get_followers_count(self):
        try:
            # XPath to locate the followers count element
            followers_xpath = "//ul/li[2]/button/span"
            # Find the followers count element
            followers_element = self.driver.find_element(By.XPATH, followers_xpath)
            return followers_element.text
        except NoSuchElementException:
            # Print message if followers element not found
            print("Followers element not found")
            return None

    # Method to retrieve the following count from the Instagram page.   
    def get_following_count(self):
        try:
            # XPath to locate the following count element
            following_xpath = "//ul/li[3]/button/span"
            # Find the following count element
            following_element = self.driver.find_element(By.XPATH, following_xpath)
            return following_element.text
        except NoSuchElementException:
            # Print message if following element not found
            print("Following element not found")
            return None


# URL of the Instagram page
url = "https://www.instagram.com/guviofficial/"

# Create an instance of InstagramPageInfo class
guvi = InstagramPageInfo(url)

# Start the browser and navigate to the Instagram page
if guvi.booting_function():
    # Get followers count
    followers_count = guvi.get_followers_count()
    if followers_count:
        print("Followers of the Guvi page on Instagram:", followers_count)
    
    # Get following count
    following_count = guvi.get_following_count()
    if following_count:
        print("Following of the Guvi page on Instagram:", following_count)
    
    # Shutdown the browser
    guvi.shutdown()
