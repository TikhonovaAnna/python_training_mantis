# from model.project import Project
import time


class ProjectHelper:

    def __init__(self, app):
        self.app = app

    def open_home_page(self):
        wd = self.app.wd
        wd.get("http://localhost/mantisbt-1.2.20")

    def open_manager_project_page(self):
        wd = self.app.wd
        wd.get("http://localhost/mantisbt-1.2.20/manage_proj_page.php")

    def data_filling(self, project_data):
        wd = self.app.wd
        wd.find_element_by_name("name").click()
        wd.find_element_by_name("name").clear()
        wd.find_element_by_name("name").send_keys(project_data.name)
        wd.find_element_by_name("description").click()
        wd.find_element_by_name("description").clear()
        wd.find_element_by_name("description").send_keys(project_data.description)

    def create_project(self, project):
        wd = self.app.wd
        self.open_manager_project_page()
        wd.find_element_by_xpath("//input[@value='Create New Project']").click()
        self.data_filling(project)
        wd.find_element_by_xpath("//input[@value='Add Project']").click()

    def delete_project(self, project):
        wd = self.app.wd
        self.open_manager_project_page()
        wd.find_element_by_link_text(project).click()
        wd.find_element_by_xpath("//input[@value='Delete Project']").click()
        time.sleep(5)
        wd.find_element_by_xpath("//input[@value='Delete Project']").click()

    def get_project_list(self):
        wd = self.app.wd
        self.open_manager_project_page()
        for element in wd.find_elements_by_css_selector('table.hide td.login-info-right'):
           element.find_element_by_tag_name("form").click()
           projects = element.find_element_by_name('project_id').text
           list = projects.split('\n')
           list.remove('All Projects')
           return list

        # if self.projects_cache is None:
        #     wd = self.app.wd
        #     self.open_manager_project_page()
        #     self.projects_cache = []
        #     for row in wd.find_elements_by_xpath("//table[3]/tbody/tr")[2:]:  # first two rows are not Projects
        #         cells = row.find_elements_by_tag_name("td")
        #         link = row.find_element_by_css_selector("a").get_attribute('href')
        #         id = link[link.find("=") + 1:]
        #         name = cells[0].text
        #         status = cells[1].text
        #         enabled = cells[2].text
        #         viewstatus = cells[3].text
        #         description = cells[4].text
        #         scanned_project = Project(id=id, name=name, status=status, enabled=enabled, viewstatus=viewstatus,
        #                                   description=description)
        #         self.projects_cache.append(scanned_project)
        # return list(self.projects_cache)