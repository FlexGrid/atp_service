# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.day_offer_vector import DayOfferVector  # noqa: F401,E501
from swagger_server import util


class DayOfferVectorEuroMWh2(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, values: DayOfferVector=None, price_unit: str=None, volume_unit: str=None):  # noqa: E501
        """DayOfferVectorEuroMWh2 - a model defined in Swagger

        :param values: The values of this DayOfferVectorEuroMWh2.  # noqa: E501
        :type values: DayOfferVector
        :param price_unit: The price_unit of this DayOfferVectorEuroMWh2.  # noqa: E501
        :type price_unit: str
        :param volume_unit: The volume_unit of this DayOfferVectorEuroMWh2.  # noqa: E501
        :type volume_unit: str
        """
        self.swagger_types = {
            'values': DayOfferVector,
            'price_unit': str,
            'volume_unit': str
        }

        self.attribute_map = {
            'values': 'values',
            'price_unit': 'price_unit',
            'volume_unit': 'volume_unit'
        }
        self._values = values
        self._price_unit = price_unit
        self._volume_unit = volume_unit

    @classmethod
    def from_dict(cls, dikt) -> 'DayOfferVectorEuroMWh2':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The DayOfferVectorEuroMWh2 of this DayOfferVectorEuroMWh2.  # noqa: E501
        :rtype: DayOfferVectorEuroMWh2
        """
        return util.deserialize_model(dikt, cls)

    @property
    def values(self) -> DayOfferVector:
        """Gets the values of this DayOfferVectorEuroMWh2.


        :return: The values of this DayOfferVectorEuroMWh2.
        :rtype: DayOfferVector
        """
        return self._values

    @values.setter
    def values(self, values: DayOfferVector):
        """Sets the values of this DayOfferVectorEuroMWh2.


        :param values: The values of this DayOfferVectorEuroMWh2.
        :type values: DayOfferVector
        """
        if values is None:
            raise ValueError("Invalid value for `values`, must not be `None`")  # noqa: E501

        self._values = values

    @property
    def price_unit(self) -> str:
        """Gets the price_unit of this DayOfferVectorEuroMWh2.


        :return: The price_unit of this DayOfferVectorEuroMWh2.
        :rtype: str
        """
        return self._price_unit

    @price_unit.setter
    def price_unit(self, price_unit: str):
        """Sets the price_unit of this DayOfferVectorEuroMWh2.


        :param price_unit: The price_unit of this DayOfferVectorEuroMWh2.
        :type price_unit: str
        """
        allowed_values = ["€/MWh^2"]  # noqa: E501
        if price_unit not in allowed_values:
            raise ValueError(
                "Invalid value for `price_unit` ({0}), must be one of {1}"
                .format(price_unit, allowed_values)
            )

        self._price_unit = price_unit

    @property
    def volume_unit(self) -> str:
        """Gets the volume_unit of this DayOfferVectorEuroMWh2.


        :return: The volume_unit of this DayOfferVectorEuroMWh2.
        :rtype: str
        """
        return self._volume_unit

    @volume_unit.setter
    def volume_unit(self, volume_unit: str):
        """Sets the volume_unit of this DayOfferVectorEuroMWh2.


        :param volume_unit: The volume_unit of this DayOfferVectorEuroMWh2.
        :type volume_unit: str
        """
        allowed_values = ["MWh^2"]  # noqa: E501
        if volume_unit not in allowed_values:
            raise ValueError(
                "Invalid value for `volume_unit` ({0}), must be one of {1}"
                .format(volume_unit, allowed_values)
            )

        self._volume_unit = volume_unit
