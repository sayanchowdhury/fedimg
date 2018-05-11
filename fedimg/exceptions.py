# This file is part of fedimg.
# Copyright (C) 2018 Red Hat, Inc.
#
# fedimg is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# fedimg is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public
# License along with fedimg; if not, see http://www.gnu.org/licenses,
# or write to the Free Software Foundation, Inc.,
# 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA
#
# Authors:  Sayan Chowdhury <sayanchowdhury@fedoraproject.org>
"""
Global fedimg exception and warning classes
"""


class SourceNotFound(Exception):
    """ The requested source was not found"""
    pass


class CommandRunFailed(Exception):
    """ The request command failed while running"""
    pass


class UnCompressFailed(Exception):
    """ The uncompress operation of the raw image failed"""
    pass


class RetryTimeout(Exception):
    """ This is raised when the retry timeout is hit."""
    pass
