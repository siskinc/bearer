from .export import Export
import openpyxl


class ExcelExport(Export):

    def export(self, model, data_list: list, file_path: str, **kwargs):
        file_path = file_path.replace(':', '_')
        comments = model.comments
        workbook = openpyxl.Workbook(write_only=True)
        sheet = workbook.create_sheet(kwargs.get('sheet_name', 'Sheet1'))
        sheet.append(comments)
        for data in data_list:
            sheet.append(list(map(lambda x: str(x), data)))
        # for i in range(1, len(comments)):
        #     sheet.append()
        #     sheet.cell(1, i+1, comments[i])
        # for i in range(0, len(data)):
        #     for j in range(0, len(data[i])):
        #         sheet.cell(i + 2, j+1, str(data[i][j]))
        workbook.save(file_path)
        print('excel 写入完成，文件：{}'.format(file_path))
