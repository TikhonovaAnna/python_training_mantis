from suds.client import Client
from suds import WebFault
from model.project import Project


class SoapHelper:

    def __init__(self, app):
        self.app = app

    def can_login(self, username, password):
        wd = self.app.wd
        client = Client(self.app.base_url + "/api/soap/mantisconnect.php" + "?wsdl")
        try:
            client.service.mc_login(username, password)
            return True
        except WebFault:
            return False

    def get_projects_list(self, username, password):
        client = Client(self.app.base_url + "/api/soap/mantisconnect.php" + "?wsdl")
        response = client.service.mc_projects_get_user_accessible(username, password)
        i = []
        for project_data in response:
            project = Project(id=project_data.id, name=str(project_data.name), status=project_data.view_state,
                              inherit_global=project_data.enabled, description=project_data.description)
            i.append(project)
        return i
