from abc import ABCMeta, abstractmethod


class DataReader(metaclass=ABCMeta):

    @abstractmethod
    def get_data(self, model, database, *args, **kwargs):
        raise NotImplementedError
