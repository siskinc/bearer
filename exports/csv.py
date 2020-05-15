from exports.export import Export
import csv


class CsvExport(Export):
    def export(self, model, data_list, file_path, **kwargs):
        file_path = file_path.replace(':', '_')
        with open(file_path, 'wt', encoding='utf8', newline='') as f:
            csv_writer = csv.writer(f)
            csv_writer.writerow(model.comments)
            csv_writer.writerows(data_list)
        print('excel write complete，file name：{}'.format(file_path))
