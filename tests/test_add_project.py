from model.project import Project

def test_add_project(app):
    app.session.login("administrator", "root")
    old_projects= app.projects.get_project_list()
    project = Project(name="Project for test ", description="test")
    app.projects.create_project(project)
    new_projects= app.projects.get_project_list()
    assert len(old_projects)+1 == len(new_projects)
    old_projects.append(project)
    assert sorted(old_projects) == sorted(new_projects)
