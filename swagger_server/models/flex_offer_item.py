# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.day_offer_vector_euro_m_var import DayOfferVectorEuroMVar  # noqa: F401,E501
from swagger_server.models.day_offer_vector_euro_m_wh import DayOfferVectorEuroMWh  # noqa: F401,E501
from swagger_server.models.day_offer_vector_euro_m_wh2 import DayOfferVectorEuroMWh2  # noqa: F401,E501
from swagger_server import util


class FlexOfferItem(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, storage_unit: str=None, day_ahead_market_offer: DayOfferVectorEuroMWh=None, reserve_market_offer_up: DayOfferVectorEuroMWh2=None, reserve_market_offer_down: DayOfferVectorEuroMWh2=None, d_lm_ps: DayOfferVectorEuroMWh=None, q_lm_ps: DayOfferVectorEuroMVar=None, balancing_market_offer_up: DayOfferVectorEuroMWh=None, balancing_market_offer_down: DayOfferVectorEuroMWh=None):  # noqa: E501
        """FlexOfferItem - a model defined in Swagger

        :param storage_unit: The storage_unit of this FlexOfferItem.  # noqa: E501
        :type storage_unit: str
        :param day_ahead_market_offer: The day_ahead_market_offer of this FlexOfferItem.  # noqa: E501
        :type day_ahead_market_offer: DayOfferVectorEuroMWh
        :param reserve_market_offer_up: The reserve_market_offer_up of this FlexOfferItem.  # noqa: E501
        :type reserve_market_offer_up: DayOfferVectorEuroMWh2
        :param reserve_market_offer_down: The reserve_market_offer_down of this FlexOfferItem.  # noqa: E501
        :type reserve_market_offer_down: DayOfferVectorEuroMWh2
        :param d_lm_ps: The d_lm_ps of this FlexOfferItem.  # noqa: E501
        :type d_lm_ps: DayOfferVectorEuroMWh
        :param q_lm_ps: The q_lm_ps of this FlexOfferItem.  # noqa: E501
        :type q_lm_ps: DayOfferVectorEuroMVar
        :param balancing_market_offer_up: The balancing_market_offer_up of this FlexOfferItem.  # noqa: E501
        :type balancing_market_offer_up: DayOfferVectorEuroMWh
        :param balancing_market_offer_down: The balancing_market_offer_down of this FlexOfferItem.  # noqa: E501
        :type balancing_market_offer_down: DayOfferVectorEuroMWh
        """
        self.swagger_types = {
            'storage_unit': str,
            'day_ahead_market_offer': DayOfferVectorEuroMWh,
            'reserve_market_offer_up': DayOfferVectorEuroMWh2,
            'reserve_market_offer_down': DayOfferVectorEuroMWh2,
            'd_lm_ps': DayOfferVectorEuroMWh,
            'q_lm_ps': DayOfferVectorEuroMVar,
            'balancing_market_offer_up': DayOfferVectorEuroMWh,
            'balancing_market_offer_down': DayOfferVectorEuroMWh
        }

        self.attribute_map = {
            'storage_unit': 'storage_unit',
            'day_ahead_market_offer': 'day_ahead_market_offer',
            'reserve_market_offer_up': 'reserve_market_offer_up',
            'reserve_market_offer_down': 'reserve_market_offer_down',
            'd_lm_ps': 'd-LMPs',
            'q_lm_ps': 'q-LMPs',
            'balancing_market_offer_up': 'balancing_market_offer_up',
            'balancing_market_offer_down': 'balancing_market_offer_down'
        }
        self._storage_unit = storage_unit
        self._day_ahead_market_offer = day_ahead_market_offer
        self._reserve_market_offer_up = reserve_market_offer_up
        self._reserve_market_offer_down = reserve_market_offer_down
        self._d_lm_ps = d_lm_ps
        self._q_lm_ps = q_lm_ps
        self._balancing_market_offer_up = balancing_market_offer_up
        self._balancing_market_offer_down = balancing_market_offer_down

    @classmethod
    def from_dict(cls, dikt) -> 'FlexOfferItem':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The FlexOfferItem of this FlexOfferItem.  # noqa: E501
        :rtype: FlexOfferItem
        """
        return util.deserialize_model(dikt, cls)

    @property
    def storage_unit(self) -> str:
        """Gets the storage_unit of this FlexOfferItem.


        :return: The storage_unit of this FlexOfferItem.
        :rtype: str
        """
        return self._storage_unit

    @storage_unit.setter
    def storage_unit(self, storage_unit: str):
        """Sets the storage_unit of this FlexOfferItem.


        :param storage_unit: The storage_unit of this FlexOfferItem.
        :type storage_unit: str
        """

        self._storage_unit = storage_unit

    @property
    def day_ahead_market_offer(self) -> DayOfferVectorEuroMWh:
        """Gets the day_ahead_market_offer of this FlexOfferItem.


        :return: The day_ahead_market_offer of this FlexOfferItem.
        :rtype: DayOfferVectorEuroMWh
        """
        return self._day_ahead_market_offer

    @day_ahead_market_offer.setter
    def day_ahead_market_offer(self, day_ahead_market_offer: DayOfferVectorEuroMWh):
        """Sets the day_ahead_market_offer of this FlexOfferItem.


        :param day_ahead_market_offer: The day_ahead_market_offer of this FlexOfferItem.
        :type day_ahead_market_offer: DayOfferVectorEuroMWh
        """

        self._day_ahead_market_offer = day_ahead_market_offer

    @property
    def reserve_market_offer_up(self) -> DayOfferVectorEuroMWh2:
        """Gets the reserve_market_offer_up of this FlexOfferItem.


        :return: The reserve_market_offer_up of this FlexOfferItem.
        :rtype: DayOfferVectorEuroMWh2
        """
        return self._reserve_market_offer_up

    @reserve_market_offer_up.setter
    def reserve_market_offer_up(self, reserve_market_offer_up: DayOfferVectorEuroMWh2):
        """Sets the reserve_market_offer_up of this FlexOfferItem.


        :param reserve_market_offer_up: The reserve_market_offer_up of this FlexOfferItem.
        :type reserve_market_offer_up: DayOfferVectorEuroMWh2
        """

        self._reserve_market_offer_up = reserve_market_offer_up

    @property
    def reserve_market_offer_down(self) -> DayOfferVectorEuroMWh2:
        """Gets the reserve_market_offer_down of this FlexOfferItem.


        :return: The reserve_market_offer_down of this FlexOfferItem.
        :rtype: DayOfferVectorEuroMWh2
        """
        return self._reserve_market_offer_down

    @reserve_market_offer_down.setter
    def reserve_market_offer_down(self, reserve_market_offer_down: DayOfferVectorEuroMWh2):
        """Sets the reserve_market_offer_down of this FlexOfferItem.


        :param reserve_market_offer_down: The reserve_market_offer_down of this FlexOfferItem.
        :type reserve_market_offer_down: DayOfferVectorEuroMWh2
        """

        self._reserve_market_offer_down = reserve_market_offer_down

    @property
    def d_lm_ps(self) -> DayOfferVectorEuroMWh:
        """Gets the d_lm_ps of this FlexOfferItem.


        :return: The d_lm_ps of this FlexOfferItem.
        :rtype: DayOfferVectorEuroMWh
        """
        return self._d_lm_ps

    @d_lm_ps.setter
    def d_lm_ps(self, d_lm_ps: DayOfferVectorEuroMWh):
        """Sets the d_lm_ps of this FlexOfferItem.


        :param d_lm_ps: The d_lm_ps of this FlexOfferItem.
        :type d_lm_ps: DayOfferVectorEuroMWh
        """

        self._d_lm_ps = d_lm_ps

    @property
    def q_lm_ps(self) -> DayOfferVectorEuroMVar:
        """Gets the q_lm_ps of this FlexOfferItem.


        :return: The q_lm_ps of this FlexOfferItem.
        :rtype: DayOfferVectorEuroMVar
        """
        return self._q_lm_ps

    @q_lm_ps.setter
    def q_lm_ps(self, q_lm_ps: DayOfferVectorEuroMVar):
        """Sets the q_lm_ps of this FlexOfferItem.


        :param q_lm_ps: The q_lm_ps of this FlexOfferItem.
        :type q_lm_ps: DayOfferVectorEuroMVar
        """

        self._q_lm_ps = q_lm_ps

    @property
    def balancing_market_offer_up(self) -> DayOfferVectorEuroMWh:
        """Gets the balancing_market_offer_up of this FlexOfferItem.


        :return: The balancing_market_offer_up of this FlexOfferItem.
        :rtype: DayOfferVectorEuroMWh
        """
        return self._balancing_market_offer_up

    @balancing_market_offer_up.setter
    def balancing_market_offer_up(self, balancing_market_offer_up: DayOfferVectorEuroMWh):
        """Sets the balancing_market_offer_up of this FlexOfferItem.


        :param balancing_market_offer_up: The balancing_market_offer_up of this FlexOfferItem.
        :type balancing_market_offer_up: DayOfferVectorEuroMWh
        """

        self._balancing_market_offer_up = balancing_market_offer_up

    @property
    def balancing_market_offer_down(self) -> DayOfferVectorEuroMWh:
        """Gets the balancing_market_offer_down of this FlexOfferItem.


        :return: The balancing_market_offer_down of this FlexOfferItem.
        :rtype: DayOfferVectorEuroMWh
        """
        return self._balancing_market_offer_down

    @balancing_market_offer_down.setter
    def balancing_market_offer_down(self, balancing_market_offer_down: DayOfferVectorEuroMWh):
        """Sets the balancing_market_offer_down of this FlexOfferItem.


        :param balancing_market_offer_down: The balancing_market_offer_down of this FlexOfferItem.
        :type balancing_market_offer_down: DayOfferVectorEuroMWh
        """

        self._balancing_market_offer_down = balancing_market_offer_down
