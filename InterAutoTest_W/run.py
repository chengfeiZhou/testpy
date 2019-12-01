# coding=utf-8
import os
import pytest
from config import Conf

if __name__ == "__main__":
    report_path = Conf._report_path()
    pytest.main(['-s', '--alluredir', report_path+'/reslut'])