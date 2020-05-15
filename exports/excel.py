from .export import Export
import openpyxl


class ExcelExport(Export):

    def export(self, model, data_list: list, file_path: str, **kwargs):
        file_path = file_path.replace(':', '_')
        comments = list(model.comments)
        workbook = openpyxl.Workbook(write_only=True)
        sheet = workbook.create_sheet(kwargs.get('sheet_name', 'Sheet1'))
        sheet.append(comments)
        for data in data_list:
            sheet.append(list(map(lambda x: str(x), data)))
        workbook.save(file_path)
        print('excel write complete，file name：{}'.format(file_path))
