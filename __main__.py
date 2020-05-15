import argparse
from protocal.config_pb2 import Configure
from google.protobuf.json_format import Parse
from __init__ import logger
from exports import get_export
from data_reader import get_data_reader


def merge_database(global_database, database):
    if not database.host:
        database.host = global_database.host
    if not database.username:
        database.username = global_database.username
    if not database.password:
        database.password = global_database.password
    if database.port == 0:
        database.port = global_database.port
    if not database.misc:
        database.misc.update(global_database.misc)
    if not database.database_name:
        database.database_name = global_database.database_name
    return database


def exec_jobs(configure):
    # generate model
    model_map = dict()
    for model in configure.models:
        model_map[model.name] = model
    global_database = configure.database
    for job in configure.jobs:
        logger.info('run job: {}'.format(job.name))
        database = job.database
        database = merge_database(global_database, database)
        model_name = job.model
        model = model_map.get(model_name, None)
        if not model:
            raise ValueError('not found model, model name: {}'.format(model_name))
        export_type = job.export.export_type
        export = get_export(export_type)
        if not export:
            raise ValueError('not found export, export type: {}'.format(export_type))
        data_reader = get_data_reader(database)
        if not data_reader:
            raise ValueError('not found database reader, data base type: {}'.format(database.data_base_type))
        batch_size = job.batch_size
        if batch_size == 0:
            batch_size = 1000
        data_list = data_reader.get_data(model, database.database_name, limit=batch_size, where=job.where,
                                         **database.misc)
        export.export(model=model, data_list=data_list, file_path=job.export.output_file_path, **job.export.misc)


def read_config(config_path):
    config_file = open(config_path, 'rt', encoding='utf-8')
    body = config_file.read()
    configure = Configure()
    Parse(body, configure)
    return configure


def main():
    parser = argparse.ArgumentParser(description='export mysql data to excel')
    parser.add_argument('--config-path', type=str, default='config.json', help='config-path', dest="config_path")
    args = parser.parse_args()
    config_path = args.config_path
    configure = read_config(config_path)
    exec_jobs(configure)


if __name__ == '__main__':
    main()
