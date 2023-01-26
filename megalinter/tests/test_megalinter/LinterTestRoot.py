# !/usr/bin/env python3
"""
Unit tests for Linter class (and sub-classes)
"""
import os

from typing import Optional

from megalinter import config, linter_factory
from megalinter.tests.test_megalinter.helpers import utilstest


class LinterTestRoot:
    descriptor_id: Optional[str] = None
    linter_name: Optional[str] = None

    def get_linter_instance(self):
        return linter_factory.build_linter(self.descriptor_id, self.linter_name, {
                "default_linter_activation": True,
                "enable_descriptors": [],
                "enable_linters": [],
                "disable_descriptors": [],
                "disable_linters": [],
                "disable_errors_linters": [],
                "github_workspace": os.getcwd(),
                "post_linter_status": True,
            })

    def test_success(self):
        utilstest.linter_test_setup()
        utilstest.test_linter_success(self.get_linter_instance(), self)

    def test_failure(self):
        utilstest.linter_test_setup()
        utilstest.test_linter_failure(self.get_linter_instance(), self)

    def test_get_linter_version(self):
        utilstest.linter_test_setup()
        utilstest.test_get_linter_version(self.get_linter_instance(), self)

    def test_get_linter_help(self):
        utilstest.linter_test_setup()
        utilstest.test_get_linter_help(self.get_linter_instance(), self)

    def test_report_tap(self):
        utilstest.linter_test_setup({"report_type": "tap"})
        utilstest.test_linter_report_tap(self.get_linter_instance(), self)

    def test_report_sarif(self):
        utilstest.linter_test_setup({"report_type": "SARIF"})
        utilstest.test_linter_report_sarif(self.get_linter_instance(), self)

    def test_format_fix(self):
        utilstest.linter_test_setup()

        if self.linter_name == 'prettier':
            config.set_value("JAVASCRIPT_DEFAULT_STYLE", "prettier")
        
        utilstest.test_linter_format_fix(self.get_linter_instance(), self)
