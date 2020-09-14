"""TODO: Doku."""
from tests import unittest
from tests.utils import (prepare_client, prepare_configuration,
                         restore_configuration, WEB_CONFIG_PATH)
from tests.web.test_login import TestLogin

from easywall.config import Config


class TestFirstrun(unittest.TestCase):
    """TODO: Doku."""

    def setUp(self) -> None:
        """TODO: Doku."""
        prepare_configuration()
        self.config = Config(WEB_CONFIG_PATH)
        self.config.set_value("WEB", "username", "")
        self.config.set_value("WEB", "password", "")
        self.client = prepare_client()
        self.login = TestLogin()

    def tearDown(self) -> None:
        """TODO: Doku."""
        restore_configuration()

    def test_firstrun_logged_out(self) -> None:
        """TODO: Doku."""
        response = self.client.get('/')
        self.assertIn(b"username and password", response.data)

    def test_firstrun_save_logged_out(self) -> None:
        """TODO: Doku."""
        self.login.log_in(self.client)
        response = self.client.post('/firstrun-save', data={
            "username": "demo",
            "password": "demo",
            "password-confirm": "demo"
        }, follow_redirects=True)
        self.assertIn(b"The Configuration was saved successfully", response.data)
