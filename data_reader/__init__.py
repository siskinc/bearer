from protocal import config_pb2
from data_reader.mysql import MysqlDataReader
from data_reader.influx import InfluxDataReader


def get_data_reader(database):
    if database.data_base_type == config_pb2.DataBaseTypeMysql:
        return MysqlDataReader(database.host, database.username, database.password, database.port)
    elif database.data_base_type == config_pb2.DataBaseTypeInflux:
        return InfluxDataReader(database.host, database.username, database.password, database.port)
    return None
