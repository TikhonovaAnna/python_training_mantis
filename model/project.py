from sys import maxsize


class Project:

    def __init__(self, id=None, name=None, status=None, inherit_global=None, view_state=None,
                 description=None):
        self.name = name
        self.status = status
        self.inherit_global = inherit_global
        self.view_state = view_state
        self.description = description
        self.id = id

    def __repr__(self):
        return "%s:%s:%s:%s:%s:%s" % (
        self.id, self.name, self.status, self.inherit_global, self.view_state, self.description)

    def __eq__(self, other):
        return (self.name is None or other.name is None or self.name == other.name) and self.id == other.id

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize 