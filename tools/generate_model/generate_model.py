import json
from typing import List
from tools.generate_model.struct_info import TableStructInfo
from tools.generate_model.common import table_name_to_class_name


def generate_model(info_list: List[TableStructInfo], file_name=None):
    for info in info_list:
        class_body = 'class {}(object):'.format(table_name_to_class_name(info.class_name))
        class_body = '{}\n    fields = {}'.format(class_body, json.dumps(info.filed_list))
        class_body = '{}\n    comments = {}'.format(class_body, json.dumps(info.comments, ensure_ascii=False))
        if file_name:
            f = open(file_name, 'w', encoding='utf8')
            f.write(class_body)
            f.close()
