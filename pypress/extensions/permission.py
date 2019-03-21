
# coding=utf-8
"""    extensions: permission.py
    permission for tornado. from flask-principal.
    :modified by laoqiu.com@gmail.com
    Example:
    >>> from extensions.permission import UserNeed, RoleNeed, ItemNeed, Permission
    >>> admin = Permission(RoleNeed('admin'))
    >>> editor = Permission(UserNeed(1)) & admin

    # handers
    ~~~~~~~~~

    @admin.require(401)
    def get(self):
        self.write('is admin')
        return     
    def post(self):
        # or
        if editor.can(self.identity):
            print 'admin'
        # or
        editor.test(self.identity, 401)
        return
"""
import sys
import tornado.web

from functools import wraps, partial
from collections import namedtuple

__all__ = ['UserNeed', 'RoleNeed', 'ItemNeed',
           'Permission', 'Identity', 'AnoymousIdentity']

Need = namedtuple('Need', ['method', 'value'])

UserNeed = partial(Need, 'user')
RoleNeed = partial(Need, "role")
ItemNeed = namedtuple('ItemNeed', ['method', 'value', 'type'])


class PermissionDenied(RuntimeError):
    """Permission denied to the resource"""
    pass


class Identity(object):
    """
    A set of needs provided by this user

    example:
        identity = Identity('ali')
        iden
    """

    def __init__(self, name):
        self.name = name
        self.provides = set()

    def can(self, permission):
        return permission.allows(self)


class AnonymousIdentity(Identity):
    """An anonymous identity
    :attr name: "anonymous"
    """
    def __init__(self):
        Identity.__init__(self, ' ')