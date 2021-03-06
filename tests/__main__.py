
# Copyright (c) 2017-2019, UChicago Argonne, LLC.  See LICENSE file.

import os
import sys
import unittest

_test_path = os.path.dirname(__file__)
_path = os.path.join(_test_path, '..')
if _path not in sys.path:
    sys.path.insert(0, _path)


def suite(*args, **kw):

    from tests import test_adl_parser
    from tests import test_calc2rules
    from tests import test_cli
    from tests import test_output_handler
    from tests import test_simple
    from tests import test_symbols
    from tests import test_testDisplay

    test_list = [
        test_simple,
        test_symbols,
        test_adl_parser,
        test_cli,
        test_calc2rules,
        test_output_handler,
        test_testDisplay,
        ]

    test_suite = unittest.TestSuite()
    for test in test_list:
        test_suite.addTest(test.suite())
    return test_suite


if __name__ == '__main__':
    runner=unittest.TextTestRunner(verbosity=2)
    runner.run(suite())
