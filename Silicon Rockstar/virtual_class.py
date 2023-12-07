class Data:
    """Class to store arbitrary data"""

    def __init__(self, *info):
        """Initialize with data stored in a list"""
        self.info = list(info)

    def __getitem__(self, i):
        """Allow indexing into stored data"""
        return self.info[i]


class Teacher:
    """Class to model a teacher"""

    def __init__(self):
        """Initialize with number of teachings"""
        self.work = 0

    def teach(self, info, *pupil):
        """Teach pupils by giving them info
        Increment number of teachings
        """
        for i in pupil:
            i.take(info)
        self.work += 1


class Pupil:
    """Class to model a pupil"""

    def __init__(self):
        """Initialize with empty knowledge"""
        self.knowledge = []

    def take(self, info):
        """Learn new information"""
        self.knowledge.append(info)
