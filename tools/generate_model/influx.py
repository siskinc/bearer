import influxdb
from typing import List
from tools.generate_model.struct_info import TableStructInfo
from tools.generate_model import logger
from tools.generate_model.common import table_name_to_class_name


def get_influx_info(host: str, user: str, password: str, port: int, database: str,
                    tables: List[str]) -> List[TableStructInfo]:
    influx_client = influxdb.InfluxDBClient(host, port, user, password, database)
    if not tables:
        resp = influx_client.query('show measurements')
        for data in resp:
            for dd in data:
                tables += list(dd.values())
    logger.info('需要生成Model的表：{}'.format(','.join(tables)))
    info_list = []
    for measurement in tables:
        info = TableStructInfo(measurement)
        resp = influx_client.query('show field keys from {}'.format(measurement))
        for fields in resp:
            for field in fields:
                # field_name_list.append(field['fieldKey'])
                info.add_field_and_comment(field['fieldKey'], field['fieldKey'])
        resp = influx_client.query('SHOW TAG KEYS from {}'.format(measurement))
        for tags in resp:
            for tag in tags:
                # tag_name_list.append(tag['tagKey'])
                info.add_field_and_comment(tag['tagKey'], tag['tagKey'])
        info_list.append(info)
    # logger.info(info_list)
    return info_list


if __name__ == '__main__':
    get_influx_info('172.17.101.76', '', '', 8086, 'iot_rockontrol_modbus_gujiao', [])
