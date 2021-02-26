# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.day_offer_vector_euro_m_wh2 import DayOfferVectorEuroMWh2  # noqa: F401,E501
from swagger_server.models.flex_offer_result_expected_revenues import FlexOfferResultExpectedRevenues  # noqa: F401,E501
from swagger_server import util


class FlexOfferResult(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, reserve_market_offer_up: DayOfferVectorEuroMWh2=None, reserve_market_offer_down: DayOfferVectorEuroMWh2=None, expected_revenues: FlexOfferResultExpectedRevenues=None):  # noqa: E501
        """FlexOfferResult - a model defined in Swagger

        :param reserve_market_offer_up: The reserve_market_offer_up of this FlexOfferResult.  # noqa: E501
        :type reserve_market_offer_up: DayOfferVectorEuroMWh2
        :param reserve_market_offer_down: The reserve_market_offer_down of this FlexOfferResult.  # noqa: E501
        :type reserve_market_offer_down: DayOfferVectorEuroMWh2
        :param expected_revenues: The expected_revenues of this FlexOfferResult.  # noqa: E501
        :type expected_revenues: FlexOfferResultExpectedRevenues
        """
        self.swagger_types = {
            'reserve_market_offer_up': DayOfferVectorEuroMWh2,
            'reserve_market_offer_down': DayOfferVectorEuroMWh2,
            'expected_revenues': FlexOfferResultExpectedRevenues
        }

        self.attribute_map = {
            'reserve_market_offer_up': 'reserve_market_offer_up',
            'reserve_market_offer_down': 'reserve_market_offer_down',
            'expected_revenues': 'expected_revenues'
        }
        self._reserve_market_offer_up = reserve_market_offer_up
        self._reserve_market_offer_down = reserve_market_offer_down
        self._expected_revenues = expected_revenues

    @classmethod
    def from_dict(cls, dikt) -> 'FlexOfferResult':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The FlexOfferResult of this FlexOfferResult.  # noqa: E501
        :rtype: FlexOfferResult
        """
        return util.deserialize_model(dikt, cls)

    @property
    def reserve_market_offer_up(self) -> DayOfferVectorEuroMWh2:
        """Gets the reserve_market_offer_up of this FlexOfferResult.


        :return: The reserve_market_offer_up of this FlexOfferResult.
        :rtype: DayOfferVectorEuroMWh2
        """
        return self._reserve_market_offer_up

    @reserve_market_offer_up.setter
    def reserve_market_offer_up(self, reserve_market_offer_up: DayOfferVectorEuroMWh2):
        """Sets the reserve_market_offer_up of this FlexOfferResult.


        :param reserve_market_offer_up: The reserve_market_offer_up of this FlexOfferResult.
        :type reserve_market_offer_up: DayOfferVectorEuroMWh2
        """

        self._reserve_market_offer_up = reserve_market_offer_up

    @property
    def reserve_market_offer_down(self) -> DayOfferVectorEuroMWh2:
        """Gets the reserve_market_offer_down of this FlexOfferResult.


        :return: The reserve_market_offer_down of this FlexOfferResult.
        :rtype: DayOfferVectorEuroMWh2
        """
        return self._reserve_market_offer_down

    @reserve_market_offer_down.setter
    def reserve_market_offer_down(self, reserve_market_offer_down: DayOfferVectorEuroMWh2):
        """Sets the reserve_market_offer_down of this FlexOfferResult.


        :param reserve_market_offer_down: The reserve_market_offer_down of this FlexOfferResult.
        :type reserve_market_offer_down: DayOfferVectorEuroMWh2
        """

        self._reserve_market_offer_down = reserve_market_offer_down

    @property
    def expected_revenues(self) -> FlexOfferResultExpectedRevenues:
        """Gets the expected_revenues of this FlexOfferResult.


        :return: The expected_revenues of this FlexOfferResult.
        :rtype: FlexOfferResultExpectedRevenues
        """
        return self._expected_revenues

    @expected_revenues.setter
    def expected_revenues(self, expected_revenues: FlexOfferResultExpectedRevenues):
        """Sets the expected_revenues of this FlexOfferResult.


        :param expected_revenues: The expected_revenues of this FlexOfferResult.
        :type expected_revenues: FlexOfferResultExpectedRevenues
        """

        self._expected_revenues = expected_revenues
