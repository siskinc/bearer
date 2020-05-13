import influxdb
from typing import List
from tools.generate_model.struct_info import TableStructInfo
from tools.generate_model import logger


def get_influx_info(host: str, user: str, password: str, port: int, database: str,
                    tables: List[str]) -> List[TableStructInfo]:
    influx_client = influxdb.InfluxDBClient(host, port, user, password, database)
    if not tables:
        resp = influx_client.query('show measurements')
        print(resp)


if __name__ == '__main__':
    get_influx_info('172.17.101.76', '', '', 8086, 'iot_rockontrol_modbus_gujiao', [])
