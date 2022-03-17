import unittest
from datetime import timedelta, datetime
from unittest import IsolatedAsyncioTestCase

import jwt
from fastapi import HTTPException
from freezegun import freeze_time

from auth.auth import User, AuthHandler, ACCESS_TOKEN_EXPIRE_MINUTES


class AuthModule(unittest.TestCase):

    @freeze_time("01-1-2022 23:23:23")
    def test_generate_token(self):
        user = User(username="test")
        token = AuthHandler().generate_token(user)
        decoded = jwt.decode(token, options={"verify_signature": False})
        time = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
        self.assertEqual(decoded['sub'], "test")
        self.assertEqual(decoded['exp'], int(time.timestamp()))

    def test_valid_auth_user(self):
        auth_handler = AuthHandler()
        user = auth_handler.authenticate_user("admin", "password")
        self.assertEqual(user.username, "admin")

    def test_invalid_auth_user(self):
        auth_handler = AuthHandler()
        user = auth_handler.authenticate_user("admin", "ups")
        self.assertEqual(user, False)


class AuthModuleAsync(IsolatedAsyncioTestCase):
    async def test_valid_current_user(self):
        user = User(username="admin")
        auth_handler = AuthHandler()
        token = auth_handler.generate_token(user)
        r_user = await auth_handler.get_current_user(token)
        self.assertEqual(r_user.username, "admin")

    async def test_invalid_current_user(self):
        user = User(username="invalid")
        auth_handler = AuthHandler()
        token = auth_handler.generate_token(user)
        with self.assertRaises(HTTPException):
            await auth_handler.get_current_user(token)
