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
        if where:
            sql_str = '{} where {}'.format(sql_str, where)
        self.influx_client.switch_database(database)
        # self.connection.select_db(database)
        # cursor = self.connection.cursor()
        offset = 0
        result = []
        while True:
            exec_sql_str = '{} LIMIT {} OFFSET {}'.format(sql_str, limit, offset)
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
            if count < limit:
                break
            offset += count
        return result
