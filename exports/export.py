from abc import ABCMeta, abstractmethod


class Export(metaclass=ABCMeta):

    @abstractmethod
    def export(self, model, data, file_path):
        raise NotImplementedError
