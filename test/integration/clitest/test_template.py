from example import TemplateControl
from test.integration.clitest.cli import CLITest
import pytest

arguments = ["test", "123", "bla"]


class TestTemplate(CLITest):

    def setup_method(self, method):
        super(TestTemplate, self).setup_method(method)
        self.cli.register("template", TemplateControl, "TEST")
        self.args += ["template"]

    @pytest.mark.parametrize("argument", arguments)
    def test_template(self, capsys, argument):
        self.args += ['%s' % argument]
        self.cli.invoke(self.args, strict=True)

        out, err = capsys.readouterr()
        assert argument in out