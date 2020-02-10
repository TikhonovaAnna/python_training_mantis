from model.project import Project
from datetime import datetime



def test_add_project(app):
    app.session.login("administrator", "root")
    old_projects= app.projects.get_project_list()
    #project = Project(name="new project664u33", description="test6s9wfr")
    project = Project(name=("Project " + str(datetime.now().strftime("%m_%d %H:%M:%S"))),
                             description="Description")
    app.projects.create_project(project)
    new_projects= app.projects.get_project_list()
    assert len(old_projects) + 1 == len(new_projects)
    old_projects.append(project)
    #assert sorted(old_projects) == sorted(new_projects)

    print(old_projects)
    print(new_projects)

    #assert sorted(old_projects, key=old_projects[0]) == sorted(new_projects, key=new_projects[0])