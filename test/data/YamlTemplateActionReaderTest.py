from hamcrest.core.assert_that import assert_that
from hamcrest.core.core.isequal import equal_to

from src.data.action.YamlTemplateActionBuilder import YamlTemplateActionBuilder
from src.data.action.YamlTemplateActionReader import YamlTemplateActionReader


__author__ = 'DWI'

import unittest


class YamlTemplateActionReaderTest(unittest.TestCase):
    def test_read_action_file(self):
        action_reader = YamlTemplateActionReader(YamlTemplateActionBuilder())
        actions = action_reader.read("./actions/actions.yaml")
        assert_that(len(actions), equal_to(2))
        assert_that(actions[0].field_name, equal_to("foo"))
        assert_that(actions[0].value, equal_to("hello world"))
        assert_that(actions[1].field_name, equal_to("bar"))
        assert_that(actions[1].value, equal_to("hello world2"))


if __name__ == '__main__':
    unittest.main()
