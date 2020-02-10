from model.project import Project
import random
from datetime import datetime
import time


def test_del_project(app):
    #app.session.login("administrator", "root")
    if len(app.projects.get_project_list())==0:
        project = Project(name=("Project " + str(datetime.now().strftime("%m_%d %H:%M:%S"))),
                             description="Description")
        app.projects.create_project(project)

    time.sleep(5)
    old_projects= app.projects.get_project_list()
    project = random.choice(old_projects)
    app.projects.delete_project(project)
    new_projects= app.projects.get_project_list()
    assert len(old_projects)-1 == len(new_projects)
    old_projects.remove(project)
    #assert sorted(old_projects) == sorted(new_projects)