import pymysql
from .data_reader import DataReader


class MysqlDataReader(DataReader):
    def __init__(self, host, username, password, port):
        # super.__init__(self, None, None)
        self.connection = pymysql.connect(
            host=host,
            port=port,
            user=username,
            password=password,
            charset='utf8'
        )

    def get_data(self, model, database, *args, **kwargs):
        where = kwargs.get('where', '')
        table_name = kwargs['table_name']
        field_list = model.fields
        limit = kwargs.get('limit', 1000)
        sql_str = 'select {} from {}'.format(','.join(field_list), table_name)
        if not where:
            where = [""]
        self.connection.select_db(database)
        cursor = self.connection.cursor()
        result = []
        for where_item in where:
            sql_str = '{} where {}'.format(sql_str, where_item)
            offset = 0
            while True:
                exec_sql_str = '{} limit {}, {}'.format(sql_str, offset, limit)
                print(exec_sql_str)
                cursor.execute(exec_sql_str)
                data_list = cursor.fetchall()
                # print(data_list)
                result = result + list(data_list)
                if len(data_list) < limit:
                    break
                offset += len(data_list)
            cursor.close()
        return result
