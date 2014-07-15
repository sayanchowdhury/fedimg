#!/bin/env python
# -*- coding: utf8 -*-

import unittest

import fedmsg.consumers


class TestKojiConsumer(Base):
    """ Fedimg should pick up on completed createImage Koji tasks and kick off
    the upload process if they produce an image we want to upload. """

    def setup(self):
        pass

    def teardown(self):
        pass

if __name__ == '__main__':
    unittest.main()