"""Test cases for the __main__ module."""
import os.path

import pytest
from click.testing import CliRunner

import mccoy
from mccoy import __main__


@pytest.fixture
def runner() -> CliRunner:
    """Fixture for invoking command-line interfaces."""
    return CliRunner()


def test_main_succeeds(runner: CliRunner) -> None:
    """It exits with a status code of zero."""
    result = runner.invoke(__main__.main)
    assert result.exit_code == 0


def test_basic_docker():
    f = mccoy.flow("infra_jenkinsci")
    for con in f.client.containers.list():
        print(con.name)


def test_backup_docker():
    f = mccoy.flow(None)
    f.volumes = ["infra_jenkins_home"]
    f.backup()
    for p in f._backups_made:
        assert os.path.exists(os.path.join(f.backup_folder, p))
