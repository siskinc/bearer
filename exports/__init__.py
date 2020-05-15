from protocal import config_pb2
from exports.excel import ExcelExport


def get_export(export_type):
    if export_type == config_pb2.ExportTypeExcel:
        return ExcelExport()
    return None
