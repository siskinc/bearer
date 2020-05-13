from .export import Export
import xlwt


class ExcelExport(Export):

    def export(self, model, data: list, file_path: str, **kwargs):
        comments = model.comments
        workbook = xlwt.Workbook()
        sheet = workbook.add_sheet(kwargs['sheet_name'])
        for i in range(0, len(comments)):
            sheet.write(0, i, comments[i])
        for i in range(0, len(data)):
            for j in range(0, len(data[i])):
                sheet.write(i + 1, j, data[i][j])
        workbook.save(file_path)
        print('excel 写入完成，文件：{}'.format(file_path))
