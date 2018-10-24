# !/usr/bin/env python3
# coding=utf-8
# author: @netmanchris
# -*- coding: utf-8 -*-

import pybrid.data
from pybrid.auth import BridAuth
import datetime


class BridDev:
    def __init__(self, ip_address: str, auth: BridAuth, cache_time: float = 15,
                 aggregate_type='15-minute'):
        """
        Initialise AwairDev object.

        :param device_name: The name of the device a can be found in the Awair app. Careful, case sensitive.
        :param auth: The authentication object as created by the BridAuth function.
        :param cache_time: The time in minutes that the state values should be cached. When this time has expired, new values
                           will be requested. Keep in mind that the API has daily limits so setting this too low might
                           cause problems.
        :param aggregate_type: Type can be 'current', '5-minute' or '15-minute' referring to the aggregation. Keep in mind that
                               not all tiers have access to all of them.
        """
        self._auth = auth
        self._cache_time = cache_time
        if aggregate_type in ['current', '5-minute', '15-minute']:
            self._aggregate_type = aggregate_type
        else:
            raise ValueError("The argument aggregate_type cannot have this value.")
        self._last_update = datetime.datetime.now()  # records the last update

        self._ip_address = ip_address

        # Get device type and ID from name
        device = pybrid.device.get_device_info(self._auth)

        self._type = device['Model']  # get the device type
        self._serial = device['Serial Number']

        # Initiate data fields
        self._data = {}
        self._last_update = None

        self.refresh()

    def get_state(self, indicator: str) -> float:
        """
        Function to get the state of a specific indicator.

        The values are cached, in accordance with the cache time that is set for the object.

        :param indicator: A string containing one of the values from: score, temp, humid, co2, voc or dust.
        :return: The value of the specific indicator.
        """
        now = datetime.datetime.now()
        delta_min = (now - self._last_update).total_seconds() / 60
        if delta_min > self._cache_time:
            self.refresh()
        return self._data[indicator]

    def name(self) -> str:
        """
        Function to get the name of the device.

        :return: The name of the device.
        """
        return self._device_name

    def type(self) -> str:
        """
        Function to get the name of the device.

        :return: The type of the device.
        """
        return self._type

    def serial(self) -> str:
        """
        Function to get the name of the device.

        :return: The name of the device.
        """
        return self._serial

    def refresh(self):
        """
        Function to refresh the state of the objects.

        The values are cached internally for the period equal to the cache
        time value. The refresh function refreshed these values, independent of the time that has past since the last
        refresh.
        """
        if self._aggregate_type == 'current':
            data: list = pybrid.data.get_status(self._auth)
        elif self._aggregate_type == '5-minute':
            data: list = pybrid.data.get_status(self._auth)
        elif self._aggregate_type == '15-minute':
            data: list = pybrid.data.get_status(self._auth)

        self._data['score'] = data['Sensors']['Quality']
        self._data['temp'] = data['Sensors']['Temperature']
        self._data['humid'] = data['Sensors']['Humidity']
        self._data['co'] = data['Sensors']['CO']
        self._last_update = datetime.datetime.now()  # records the time of the last update
