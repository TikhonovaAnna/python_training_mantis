from model.project import Project
import random
from datetime import datetime
import time


def test_del_project(app):
    app.session.login("administrator", "root")
    if len(app.soap.get_projects_list("administrator", "root"))==0:
        project = Project(name=("Project " + str(datetime.now().strftime("%m_%d %H:%M:%S"))),
                             description="Description")
        app.projects.create_project(project)

    time.sleep(5)
    # old_projects= app.projects.get_project_list()
    old_projects = app.soap.get_projects_list("administrator", "root")
    project = random.choice(old_projects)
    app.projects.delete_project(project)
    # new_projects= app.projects.get_project_list()
    new_projects = app.soap.get_projects_list("administrator", "root")
    assert len(old_projects)-1 == len(new_projects)
    # old_projects.remove(project)
    # #assert sorted(old_projects) == sorted(new_projects)
    old_projects.remove(project)
    assert sorted(old_projects, key=Project.id_or_max) == sorted(new_projects, key=Project.id_or_max)