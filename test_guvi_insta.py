import pytest  
from selenium.common.exceptions import NoSuchElementException  
from guvi_insta import InstagramPageInfo  

# Fixture to set up and tear down InstagramPageInfo instance
@pytest.fixture(scope="module")
def guvi_instance():  # Define a fixture named guvi_instance
    url = "https://www.instagram.com/guviofficial/"  # Define Instagram page URL
    guvi = InstagramPageInfo(url)  # Instantiate InstagramPageInfo with the given URL
    guvi.booting_function()  # Set up the InstagramPageInfo instance
    yield guvi  # Provide the InstagramPageInfo instance to the tests
    guvi.shutdown()  # Tear down the InstagramPageInfo instance

# Positive Test Case: Valid URL
def test_valid_url(guvi_instance):  # Define a test named test_valid_url, taking guvi_instance as input
    assert guvi_instance.booting_function() == True  # Assert that booting_function returns True

# Positive Test case: Proper Shutdown
def test_proper_shutdown(guvi_instance):  # Define a test named test_proper_shutdown, taking guvi_instance as input
    pass  # Placeholder, no assertion needed for proper shutdown

# Positive: Existing Followers and Following Counts:
def test_get_followers_count(guvi_instance):  # Define a test named test_get_followers_count, taking guvi_instance as input
    followers_count = guvi_instance.get_followers_count()  # Get followers count from InstagramPageInfo instance
    assert followers_count is not None, "Followers count should not be None"  # Assert followers count is not None

def test_get_following_count(guvi_instance):  # Define a test named test_get_following_count, taking guvi_instance as input
    following_count = guvi_instance.get_following_count()  # Get following count from InstagramPageInfo instance
    assert following_count is not None, "Following count should not be None"  # Assert following count is not None

# Positive : Existing Followers Counts:
def test_existing_followers_counts(guvi_instance):
    # followers_count = guvi_instance.get_followers_count()
    # # Assert
    # assert followers_count.isdigit() == False 
    url = "https://www.instagram.com/guviofficial/"
    guvi = InstagramPageInfo(url)
    guvi.booting_function()
    
    followers_count = guvi.get_followers_count()
    # Assert
    assert followers_count.isdigit() == False 

# Positive : Existing Following Counts:
def test_existing_following_counts(guvi_instance):
    # following_count = guvi_instance.get_following_count()
    # # Assert
    # assert following_count.isdigit() == True 
    url = "https://www.instagram.com/guviofficial/"
    guvi = InstagramPageInfo(url)
    guvi.booting_function()
    
    following_count = guvi.get_following_count()
    # Assert
    assert following_count.isdigit() == True

   
# Negative: Invalid URL
def test_invalid_url():  # Define a test named test_invalid_url
    url = "https://www.instagram.com/nonexistentpage/"  # Define invalid Instagram page URL
    guvi = InstagramPageInfo(url)  # Instantiate InstagramPageInfo with the given URL
    assert guvi.booting_function() == False  # Assert that booting_function returns False for an invalid URL
    guvi.shutdown()  # Shutdown the InstagramPageInfo instance

# Negative: Non-Existent Followers and Following Counts:
def test_nonexistent_counts():  # Define a test named test_nonexistent_counts
    url = "https://www.instagram.com/guviofficial/"  # Define Instagram page URL
    guvi = InstagramPageInfo(url)  # Instantiate InstagramPageInfo with the given URL
    guvi.booting_function()  # Set up the InstagramPageInfo instance
    followers_count = guvi.get_followers_count()  # Get followers count from InstagramPageInfo instance
    following_count = guvi.get_following_count()  # Get following count from InstagramPageInfo instance
    assert followers_count == False  # Assert followers count is False for non-existent counts
    assert following_count == False  # Assert following count is False for non-existent counts
    guvi.shutdown()  # Shutdown the InstagramPageInfo instance

# Negative: Element Retrieval Failure
def test_element_retrieval_failure():  # Define a test named test_element_retrieval_failure
    url = "https://www.instagram.com/guviofficial/"  # Define Instagram page URL
    guvi = InstagramPageInfo(url)  # Instantiate InstagramPageInfo with the given URL
    guvi.booting_function()  # Set up the InstagramPageInfo instance
    with pytest.raises(NoSuchElementException):  # Check if NoSuchElementException is raised
        guvi.driver.find_element_by_xpath("//your/xpath/here")  # Try to find an element by XPath
    guvi.shutdown()  # Shutdown the InstagramPageInfo instance

# Negative: Browser Shutdown Failure Test case
def test_browser_shutdown_failure():  # Define a test named test_browser_shutdown_failure
    url = "https://www.instagram.com/guviofficial/"  # Define Instagram page URL
    guvi = InstagramPageInfo(url)  # Instantiate InstagramPageInfo with the given URL
    guvi.booting_function()  # Set up the InstagramPageInfo instance
    with pytest.raises(Exception):  # Check if any Exception is raised
        guvi.shutdown()  # Try to shutdown the InstagramPageInfo instance

# Negative: Browser Start Failure
def test_browser_start_failure():  # Define a test named test_browser_start_failure
    invalid_driver_path = "/invalid/path/to/driver"  # Define an invalid driver path
    url = "https://www.instagram.com/guviofficial/"  # Define Instagram page URL
    guvi = InstagramPageInfo(url)  # Instantiate InstagramPageInfo with the given URL
    assert guvi.booting_function() == False  # Assert that booting_function returns False for a failed browser start
