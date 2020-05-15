from protocal import config_pb2
from exports.excel import ExcelExport
from exports.csv import CsvExport


def get_export(export_type):
    if export_type == config_pb2.ExportTypeExcel:
        return ExcelExport()
    elif export_type == config_pb2.ExportTypeCsv:
        return CsvExport()
    return None
