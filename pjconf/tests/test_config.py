"""Test suite."""
import os
import pjconf as pj
from pjconf.config import Config


DATA_PATH = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "data"
)

USER_CONFIG_PATH = os.path.join(DATA_PATH, 'user.json')
DEFAULTS_CONFIG_PATH = os.path.join(DATA_PATH, 'defaults.json')


def test_load():
    """Test the loading shorthand."""
    config = pj.load_config(DEFAULTS_CONFIG_PATH)
    assert config.get('opt2') == 1.0


def test_load_cascade():
    """Test the loading shorthand with cascade overrides."""
    config = pj.load_config(DEFAULTS_CONFIG_PATH, USER_CONFIG_PATH)
    assert isinstance(config, Config)
    assert config.get('opt2') == 2.0    


def test_recursive():
    """Test recursive syntax."""
    config = pj.load_config(USER_CONFIG_PATH)
    assert config.get('opt3.subopt1') == True


def test_cast():
    """Test that the cast operation works."""
    config = pj.load_config(USER_CONFIG_PATH)
    assert isinstance(config.get('opt2', cast=int), int)


def test_default():
    """Test that a default value is returned for a missing field."""
    config = pj.load_config(USER_CONFIG_PATH)
    assert config.get('optmissing', default=100.0) == 100.0


def test_default_and_cast():
    """Test that a default value is returned for a missing field and that the default is honoured before casting."""
    config = pj.load_config(USER_CONFIG_PATH)
    result = config.get('optmissing', default=100.0, cast=int)
    assert result == 100
    assert isinstance(result, int)