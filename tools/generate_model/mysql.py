import pymysql
from typing import List
from .struct_info import TableStructInfo
from . import logger


def is_field(field: str) -> bool:
    if len(field) <= 2:
        return False
    return field[0] == '`' and field[-1] == '`'


def is_comment(comment: str) -> bool:
    if len(comment) <= 3:
        return False
    comment = comment[:-1]
    return comment[0] in ("'", '"') and comment[-1] in ("'", '"')


def get_field_and_comment(keys: list) -> (str, str):
    if len(keys) <= 2:
        return None, None
    if not is_field(keys[0]):
        return None, None
    field = keys[0][1:-1]
    if not is_comment(keys[-1]):
        comment = field
    else:
        comment = keys[-1][1:-2]
    return field, comment


def get_mysql_info(host: str, user: str, password: str, port: int, database: str,
                   tables: List[str]) -> List[TableStructInfo]:
    connection = pymysql.connect(
        host=host,
        port=port,
        user=user,
        password=password,
        database=database,
        charset='utf8'
    )
    cursor = connection.cursor()
    if not tables:
        cursor.execute('show tables')
        all_data = cursor.fetchall()
        tables = []
        for data in all_data:
            tables.append(data[0])
    logger.info('需要生成Model的表：{}'.format(','.join(tables)))
    info_list = []
    for table in tables:
        try:
            cursor.execute('show create table {}'.format(table))
            data = cursor.fetchone()
        except Exception as e:
            logger.error('无法获取{}表结构，报错原因：{}'.format(table, str(e)))
            continue
        table_struct = data[1]
        # logger.info(table_struct)
        class_name = ''.join(word.title() for word in table[2:].split('_'))
        table_struct_lines = table_struct.split('\n')
        info = TableStructInfo(class_name)
        for table_struct_line in table_struct_lines:
            table_struct_line = table_struct_line.strip()
            # logger.info(table_struct_line)
            keys = table_struct_line.split(' ')
            # logger.info(keys)
            filed, comment = get_field_and_comment(keys)
            logger.info('field: {}, comment: {}'.format(filed, comment))
            if not filed:
                continue
            info.add_field_and_comment(filed, comment)
        info_list.append(info)
    return info_list
