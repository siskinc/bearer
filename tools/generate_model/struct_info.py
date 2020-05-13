class TableStructInfo(object):
    def __init__(self, class_name: str, filed_list=None, comments=None):
        if filed_list is None:
            filed_list = []
        if comments is None:
            comments = []
        self.class_name = class_name
        self.comments = comments
        self.filed_list = filed_list

    def add_field_and_comment(self, filed: str, comment: str):
        self.filed_list.append(filed)
        self.comments.append(comment)
