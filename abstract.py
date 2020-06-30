import pandas as pd
from abc import ABCMeta, abstractmethod


class AbstractClassCSV(metaclass=ABCMeta):

    def __init__(self, path, file_name):

        self._path = path
        self._file_name = file_name

    @property
    @abstractmethod
    def path(self):
        pass

    @path.setter
    @abstractmethod
    def path(self, value):
        pass

    @property
    @abstractmethod
    def file_name(self):
        pass

    @file_name.setter
    @abstractmethod
    def file_name(self, value):
        pass

    @abstractmethod
    def display_summary(self):
        pass


class CSVGetInfo(AbstractClassCSV):
    """
    This class displays the summary of the tabular data contained in a CSV file.
    """

    @property
    def path(self):
        """
        The docstring for the path property
        """
        print('Getting value of path')
        return self._path

    @path.setter
    def path(self, value):
        if '/' in value:
            self._path = value
            print('Setting value of path to {}'.format(value))
        else:
            print('Error: {} is not a valid path string'.format(value))

    @property
    def file_name(self):
        """
        The docstring for the file_name property
        """
        print('Getting the value of file_name')
        return self._file_name

    @file_name.setter
    def file_name(self, value):
        if '.' in value:
            self._file_name = value
            print('Setting the value of file_name to {}'.format(value))
        else:
            print('Error: {} is not a valid file name'.format(value))

    def display_summary(self):
        data = pd.read_csv(self._path + self._file_name)
        print(self._file_name)
        print(data.info())


csv = CSVGetInfo('data/', 'ge.us.csv')

csv.display_summary()


