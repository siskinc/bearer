import argparse
from tools.generate_model import logger
from tools.generate_model.mysql import get_mysql_info
from tools.generate_model.generate_model import generate_model
from tools.generate_model.influx import get_influx_info


def main():
    parser = argparse.ArgumentParser(description='export mysql table struct to python class')
    parser.add_argument('--host', type=str, help='host', dest="host", required=True)
    parser.add_argument('--user', type=str, dest="user")
    parser.add_argument('--password', type=str, dest="password")
    parser.add_argument('--port', default=3306, type=int, dest="port", required=True)
    parser.add_argument('--db-type', default='mysql', type=str, dest="db_type")
    parser.add_argument('--database', type=str, dest="database", required=True)
    parser.add_argument('--table', type=str, action='append', dest="table")
    parser.add_argument('--file-path', type=str, dest="file_path", required=True)
    args = parser.parse_args()
    host = args.host
    user = args.user
    password = args.password
    port = args.port
    database = args.database
    tables = args.table
    file_path = args.file_path
    db_type = args.db_type
    logger.info('数据库地址：{}'.format(host))
    logger.info('数据库端口：{}'.format(port))
    logger.info('数据库名：{}'.format(database))
    logger.info('数据库类型: {}'.format(db_type))
    info_list = None
    if db_type == 'mysql':
        info_list = get_mysql_info(host, user, password, port, database, tables)
    elif db_type == 'influx':
        info_list = get_influx_info(host, user, password, port, database, tables)
    if info_list:
        generate_model(info_list, file_path)


if __name__ == '__main__':
    main()
