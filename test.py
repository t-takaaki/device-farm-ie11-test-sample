import os
import sys
import settings
from datetime import datetime
# Include boto3, the Python SDK's main package:
import boto3, pytest
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver import Remote

timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
# File Name
FILENAME = os.path.join(os.path.dirname(os.path.abspath(__file__)), f'screenshots/test-{timestamp}.png')


# in your tests:
# Set up the Device Farm client, get a driver URL:
class TestSuite:
    def setup_method(self, method):
        devicefarm_client = boto3.client("devicefarm", region_name="us-west-2")
        testgrid_url_response = devicefarm_client.create_test_grid_url(
          projectArn=settings.PROJECT_ARN,
          expiresInSeconds=300)
        desired_capabilities = DesiredCapabilities.INTERNETEXPLORER # EDGE, FIREFOX, CHROME, ANDROID, SAFARI, IPAD, IPHONE..etc
        desired_capabilities["platform"] = "windows"
        self.driver = Remote(testgrid_url_response["url"], desired_capabilities)
        self.driver.set_window_size(1366, 768)


    # later, make sure to end your WebDriver session:
    def teardown_method(self, method):
        self.driver.quit()


    def test_proguru(self):
        print('exec pytest...')
        self.driver.get("https://proguru.jp")
        title = self.driver.title
        assert title == "プログル｜学校の授業で使えるプログラミング教材"

        self.driver.save_screenshot(FILENAME)
