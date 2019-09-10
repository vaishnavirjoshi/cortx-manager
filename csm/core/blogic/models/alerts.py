"""
 ****************************************************************************
 Filename:          alerts.py
 Description:       Contains functionality for alert plugin.

 Creation Date:     12/08/2019
 Author:            Pawan Kumar Srivastava

 Do NOT modify or remove this copyright and confidentiality notice!
 Copyright (c) 2001 - $Date: 2015/01/14 $ Seagate Technology, LLC.
 The code contained herein is CONFIDENTIAL to Seagate Technology, LLC.
 Portions are also trade secret. Any use, duplication, derivation, distribution
 or disclosure of this code, for any reason, not expressly authorized is
 prohibited. All other rights are expressly reserved by Seagate Technology, LLC.
 ****************************************************************************
"""

import sys
from csm.common.errors import CsmError, CsmNotFoundError
from csm.common.log import Log
from datetime import datetime
from abc import ABC, abstractmethod
from csm.common.queries import SortBy, QueryLimits, DateTimeRange
from typing import Optional
import json
import threading
import errno


class Alert(object):
    """ Represents an alert to be sent to front end """

    def __init__(self, data):
        self._key = None
        self._data = data
        self._timestamp = datetime.utcnow()

    def key(self):
        return self._key

    def data(self):
        return self._data

    def timestamp(self):
        return self._timestamp

    def store(self, key):
        self._key = key

    def isstored(self):
        return self._key != None

    def show(self, **kwargs):
        # TODO
        raise CsmError(errno.ENOSYS, 'Alert.get() not implemented')

    def acknowledge(self, id):
        # TODO
        raise CsmError(errno.ENOSYS, 'Alert.acknowledge() not implemented')


class IAlertStorage(ABC):
    """
        Interface for Alerts repository
    """
    @abstractmethod
    async def store(self, alert):
        pass

    @abstractmethod
    async def retrieve(self, alert_id):
        pass

    @abstractmethod
    async def update(self, alert):
        pass

    @abstractmethod
    async def retrieve_by_range(self,
                                sort: Optional[SortBy],
                                time_range: DateTimeRange,
                                limits: Optional[QueryLimits]):
        pass

    @abstractmethod
    async def count_by_range(self, time_range: DateTimeRange):
        pass
