class Model(object):
    def __init__(self, fields, comments):
        self.fields = fields
        self.comments = comments
        if len(fields) == len(comments):
            pass
        elif len(fields) < len(comments):
            self.comments = self.comments[:len(fields)]
        elif len(fields) > len(comments):
            self.comments = self.comments + self.fields[len(comments):]
