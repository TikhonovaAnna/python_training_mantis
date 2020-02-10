from model.project import Project
import random

def test_del_project(app):
    app.session.login("administrator", "root")
    if len(app.projects.get_project_list())==0:
        project = Project(name="Project for test ", description="test")
        app.projects.create_project(project)
    old_projects= app.projects.get_project_list()
    project = random.choice(old_projects)
    app.projects.delete_project(project)
    new_projects= app.projects.get_project_list()
    assert len(old_projects)-1 == len(new_projects)
    old_projects.remove(project)
    assert sorted(old_projects) == sorted(new_projects)
