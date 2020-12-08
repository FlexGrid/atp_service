# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.location import Location  # noqa: F401,E501
from swagger_server import util


class StorageUnit(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, power_capacity_kw: float=None, energy_capacity_k_wh: float=None, inefficiency_rate_per_cent: float=None, initial_final_so_c_per_cent: float=None, location: Location=None):  # noqa: E501
        """StorageUnit - a model defined in Swagger

        :param power_capacity_kw: The power_capacity_kw of this StorageUnit.  # noqa: E501
        :type power_capacity_kw: float
        :param energy_capacity_k_wh: The energy_capacity_k_wh of this StorageUnit.  # noqa: E501
        :type energy_capacity_k_wh: float
        :param inefficiency_rate_per_cent: The inefficiency_rate_per_cent of this StorageUnit.  # noqa: E501
        :type inefficiency_rate_per_cent: float
        :param initial_final_so_c_per_cent: The initial_final_so_c_per_cent of this StorageUnit.  # noqa: E501
        :type initial_final_so_c_per_cent: float
        :param location: The location of this StorageUnit.  # noqa: E501
        :type location: Location
        """
        self.swagger_types = {
            'power_capacity_kw': float,
            'energy_capacity_k_wh': float,
            'inefficiency_rate_per_cent': float,
            'initial_final_so_c_per_cent': float,
            'location': Location
        }

        self.attribute_map = {
            'power_capacity_kw': 'power_capacity_KW',
            'energy_capacity_k_wh': 'energy_capacity_KWh',
            'inefficiency_rate_per_cent': 'inefficiency_rate_per_cent',
            'initial_final_so_c_per_cent': 'initial_final_SoC_per_cent',
            'location': 'location'
        }
        self._power_capacity_kw = power_capacity_kw
        self._energy_capacity_k_wh = energy_capacity_k_wh
        self._inefficiency_rate_per_cent = inefficiency_rate_per_cent
        self._initial_final_so_c_per_cent = initial_final_so_c_per_cent
        self._location = location

    @classmethod
    def from_dict(cls, dikt) -> 'StorageUnit':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The StorageUnit of this StorageUnit.  # noqa: E501
        :rtype: StorageUnit
        """
        return util.deserialize_model(dikt, cls)

    @property
    def power_capacity_kw(self) -> float:
        """Gets the power_capacity_kw of this StorageUnit.


        :return: The power_capacity_kw of this StorageUnit.
        :rtype: float
        """
        return self._power_capacity_kw

    @power_capacity_kw.setter
    def power_capacity_kw(self, power_capacity_kw: float):
        """Sets the power_capacity_kw of this StorageUnit.


        :param power_capacity_kw: The power_capacity_kw of this StorageUnit.
        :type power_capacity_kw: float
        """

        self._power_capacity_kw = power_capacity_kw

    @property
    def energy_capacity_k_wh(self) -> float:
        """Gets the energy_capacity_k_wh of this StorageUnit.


        :return: The energy_capacity_k_wh of this StorageUnit.
        :rtype: float
        """
        return self._energy_capacity_k_wh

    @energy_capacity_k_wh.setter
    def energy_capacity_k_wh(self, energy_capacity_k_wh: float):
        """Sets the energy_capacity_k_wh of this StorageUnit.


        :param energy_capacity_k_wh: The energy_capacity_k_wh of this StorageUnit.
        :type energy_capacity_k_wh: float
        """

        self._energy_capacity_k_wh = energy_capacity_k_wh

    @property
    def inefficiency_rate_per_cent(self) -> float:
        """Gets the inefficiency_rate_per_cent of this StorageUnit.


        :return: The inefficiency_rate_per_cent of this StorageUnit.
        :rtype: float
        """
        return self._inefficiency_rate_per_cent

    @inefficiency_rate_per_cent.setter
    def inefficiency_rate_per_cent(self, inefficiency_rate_per_cent: float):
        """Sets the inefficiency_rate_per_cent of this StorageUnit.


        :param inefficiency_rate_per_cent: The inefficiency_rate_per_cent of this StorageUnit.
        :type inefficiency_rate_per_cent: float
        """

        self._inefficiency_rate_per_cent = inefficiency_rate_per_cent

    @property
    def initial_final_so_c_per_cent(self) -> float:
        """Gets the initial_final_so_c_per_cent of this StorageUnit.


        :return: The initial_final_so_c_per_cent of this StorageUnit.
        :rtype: float
        """
        return self._initial_final_so_c_per_cent

    @initial_final_so_c_per_cent.setter
    def initial_final_so_c_per_cent(self, initial_final_so_c_per_cent: float):
        """Sets the initial_final_so_c_per_cent of this StorageUnit.


        :param initial_final_so_c_per_cent: The initial_final_so_c_per_cent of this StorageUnit.
        :type initial_final_so_c_per_cent: float
        """

        self._initial_final_so_c_per_cent = initial_final_so_c_per_cent

    @property
    def location(self) -> Location:
        """Gets the location of this StorageUnit.


        :return: The location of this StorageUnit.
        :rtype: Location
        """
        return self._location

    @location.setter
    def location(self, location: Location):
        """Sets the location of this StorageUnit.


        :param location: The location of this StorageUnit.
        :type location: Location
        """
        if location is None:
            raise ValueError("Invalid value for `location`, must not be `None`")  # noqa: E501

        self._location = location