import os
import re

from .conftest import root_dir


class TestReadme:

    def test_readme(self):
        try:
            with open(f'{os.path.join(root_dir, "README.md")}', 'r', encoding='utf-8') as f:
                readme = f.read()
        except FileNotFoundError:
            assert False, 'Check that you have added the README.md file'
