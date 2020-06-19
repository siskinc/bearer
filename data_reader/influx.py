import influxdb
from .data_reader import DataReader


class InfluxDataReader(DataReader):
    def __init__(self, host, username, password, port):
        self.influx_client = influxdb.InfluxDBClient(host, port, username, password)

    def get_data(self, model, database, *args, **kwargs):
        where = kwargs.get('where', '')
        table_name = kwargs['table_name']
        field_list = model.fields
        limit = kwargs.get('limit', 1000)
        sql_str = 'select {} from {}'.format(','.join(field_list), table_name)
        result = []
        if not where:
            where = [""]
        for where_item in where:
            sql_str_sub = sql_str
            if where_item:
                sql_str_sub = '{} where {}'.format(sql_str, where_item)
            self.influx_client.switch_database(database)
            # self.connection.select_db(database)
            # cursor = self.connection.cursor()
            offset = 0
            while True:
                exec_sql_str = sql_str_sub
                if limit > 0:
                    exec_sql_str = '{} LIMIT {} OFFSET {}'.format(exec_sql_str, limit, offset)
                print(exec_sql_str)
                resp = self.influx_client.query(exec_sql_str)
                count = 0
                for fields in resp:
                    for field in fields:
                        count += 1
                        data = []
                        for excel_field in field_list:
                            data.append(field[excel_field])
                        result.append(data)
                if limit <= 0:
                    break
                if count < limit:
                    break
                offset += count
        return result
