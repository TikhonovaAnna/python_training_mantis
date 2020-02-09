from selenium import webdriver
from fixture.session import SessionHelper
from fixture.projects import ProjectHelper


class Application:

    def __init__(self, browser, base_url):
        if browser=="firefox":
            self.wd = webdriver.Firefox()
        elif browser=="chrome":
            self.wd = webdriver.Chrome()
        elif browser=="ie":
            self.wd = webdriver.Ie()
        else:
            raise ValueError("Unknown browser %s" % browser)
        self.wd.implicitly_wait(5)
        self.session = SessionHelper(self)
        self.projects = ProjectHelper(self)
        self.base_url=base_url

    def open_home_page(self):
        wd = self.wd
        if not (wd.current_url.endswith("http://localhost/mantisbt-1.2.20/login_page.php")):
            wd.get(self.base_url)

    def destroy(self):
        self.wd.quit()

    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False