import os
import re

from .conftest import root_dir


class TestWorkflow:

    def test_workflow(self):
        yamdb_workflow_basename = 'yamdb_workflow'

        yaml = f'{yamdb_workflow_basename}.yaml'
        is_yaml = yaml in os.listdir(root_dir)

        yml = f'{yamdb_workflow_basename}.yml'
        is_yml = yml in os.listdir(root_dir)

        if not is_yaml and not is_yml:
            assert False, (
                f'No workflow description file found in directory {root_dir} '
                f'{yaml} or {yml}.\n'
                '(This is needed for testing on the platform)'
            )

        if is_yaml and is_yml:
            assert False, (
                f'There must not be two {yamdb_workflow_basename} files in directory {root_dir}'
                'with extensions .yaml and .yml\n'
                'Remove one of them'
            )

        filename = yaml if is_yaml else yml

        try:
            with open(f'{os.path.join(root_dir, filename)}', 'r') as f:
                yamdb = f.read()
        except FileNotFoundError:
            assert False, f'Check that you have added the file {filename} to the directory {root_dir} to check'

        assert (
                re.search(r'on:\s*push:\s*branches:\s*-\smaster', yamdb) or
                'on: [push]' in yamdb or
                'on: push' in yamdb
        ), f'Check that you`ve added a push action to {filename}'
        assert 'pytest' in yamdb, f'Check that you have added pytest to the file {filename}'
        assert 'appleboy/ssh-action' in yamdb, f'Check that you have added the deployment to the file {filename}'
        assert 'appleboy/telegram-action' in yamdb, (
            'Check that you have set up sending a telegram message '
            f'to file {filename}'
        )
