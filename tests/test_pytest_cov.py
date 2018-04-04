# -*- coding: utf-8 -*-
from metrics_pylint.info import PyLintMetric
import os
import tempfile
from shutil import copyfile

import pytest

from metrics_pytest_cov.cov import CovMetric
from . import here


@pytest.fixture
def coverage_info():
    """Get CovMetric with info loaded from the .coverage file"""
    # create a temp folder with the .coverage file and cd into it
    curr_dir = os.getcwd()
    with tempfile.TemporaryDirectory() as temp:
        copyfile(here('resources/.coverage'), os.path.join(temp, '.coverage'))
        os.chdir(temp)
        yield CovMetric({})
        os.chdir(curr_dir)


def test_pytest_cov_python_file(coverage_info):
    # process_file(self, language, key, token_list):
    coverage_info.process_file('Python', 'metrics/mccabe.py', [])
    assert coverage_info.metrics == {'coverage': 87.5, 'missing': '43, 47, 51'}


def test_pytest_cov_text_file(coverage_info):
    # process_file(self, language, key, token_list):
    coverage_info.process_file('Text only', 'research/ohcount.txt', [])
    assert coverage_info.metrics == {}


def test_pytest_cov_unknown_python_file(coverage_info):
    # process_file(self, language, key, token_list):
    coverage_info.process_file('Python', 'unknown/not_there.py', [])
    assert coverage_info.metrics == {}

