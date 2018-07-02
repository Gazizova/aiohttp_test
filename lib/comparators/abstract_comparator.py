from os.path import join
from tempfile import mkdtemp
import time
from lib.logger import LoggingHandler

# __author__ = ''


class AbstractPDFComparator(LoggingHandler):
    def __init__(self, pdf1, pdf2, output_report_dir=None):
        super().__init__()
        self.pdf1 = pdf1
        self.pdf2 = pdf2
        self._output_report_dir = output_report_dir

        self.__temp_dir = mkdtemp()

    def run_compare(self):
        raise NotImplementedError

    def get_pages_count(self, file):
        raise NotImplementedError

    def get_temp_dir(self):
        return self.__temp_dir

    def get_output_file_path(self, opt_postfix=''):
        if self._output_report_dir is None:
            return join(self.get_temp_dir(),
                        'compared_{}{}'.format(int(time.time()), opt_postfix))
        else:
            return join(self._output_report_dir,
                        'compared_{}{}'.format(self.pdf1.get_filename(), opt_postfix))
