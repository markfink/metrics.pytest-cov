# -*- coding: utf-8 -*-
"""A metrics plugin to do get gitinfo."""
from __future__ import unicode_literals, print_function

import coverage
from coverage.misc import NoSource

from metrics.metricbase import MetricBase


def get_file_processors():
    """plugin mechanism for file based metrics."""
    return [CovMetric]


def get_build_processors():
    """plugin mechanism for build based metrics."""
    return []


class CovMetric(MetricBase):
    """Compute the pylint_score for a source file."""
    def __init__(self, context):
        self._context = context
        self.reset()
        self.cov = coverage.Coverage()
        self.cov.load()

    def reset(self):
        self.coverage = 0.0
        self.missing = 'all'

    def process_file(self, language, key, token_list):
        """determine the pytest_cov_score for a given key"""
        # gather metrics which are often used like this: "$ coverage report -m"
        # extract the pytest_cov_score as described here:
        # https://stackoverflow.com/questions/35224643/how-do-i-access-coverage-py-results-programmatically
        if language == 'Text only':
            self.coverage = None
            self.missing = 'n.a.'
        elif language.startswith('Python'):
            try:
                a = self.cov._analyze(key)
                self.coverage = a.numbers.pc_covered
                self.missing = a.missing_formatted()
            except NoSource:
                # make it tolerant
                self.reset()

    def get_metrics(self):
        if self.coverage is not None:
            data = {
                'test_coverage': round(self.coverage, 2),
            }
            if self.missing:
                data['test_missing'] = self.missing
            return data
        else:
            return {}

    metrics = property(get_metrics)
