# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.flex_offer import FlexOffer  # noqa: F401,E501
from swagger_server.models.stacked_revenues_result_revenues import StackedRevenuesResultRevenues  # noqa: F401,E501
from swagger_server import util


class StackedRevenuesResult(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, sdate: date=None, flex_offer: FlexOffer=None, revenues: StackedRevenuesResultRevenues=None):  # noqa: E501
        """StackedRevenuesResult - a model defined in Swagger

        :param sdate: The sdate of this StackedRevenuesResult.  # noqa: E501
        :type sdate: date
        :param flex_offer: The flex_offer of this StackedRevenuesResult.  # noqa: E501
        :type flex_offer: FlexOffer
        :param revenues: The revenues of this StackedRevenuesResult.  # noqa: E501
        :type revenues: StackedRevenuesResultRevenues
        """
        self.swagger_types = {
            'sdate': date,
            'flex_offer': FlexOffer,
            'revenues': StackedRevenuesResultRevenues
        }

        self.attribute_map = {
            'sdate': 'sdate',
            'flex_offer': 'flex_offer',
            'revenues': 'revenues'
        }
        self._sdate = sdate
        self._flex_offer = flex_offer
        self._revenues = revenues

    @classmethod
    def from_dict(cls, dikt) -> 'StackedRevenuesResult':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The StackedRevenuesResult of this StackedRevenuesResult.  # noqa: E501
        :rtype: StackedRevenuesResult
        """
        return util.deserialize_model(dikt, cls)

    @property
    def sdate(self) -> date:
        """Gets the sdate of this StackedRevenuesResult.


        :return: The sdate of this StackedRevenuesResult.
        :rtype: date
        """
        return self._sdate

    @sdate.setter
    def sdate(self, sdate: date):
        """Sets the sdate of this StackedRevenuesResult.


        :param sdate: The sdate of this StackedRevenuesResult.
        :type sdate: date
        """
        if sdate is None:
            raise ValueError("Invalid value for `sdate`, must not be `None`")  # noqa: E501

        self._sdate = sdate

    @property
    def flex_offer(self) -> FlexOffer:
        """Gets the flex_offer of this StackedRevenuesResult.


        :return: The flex_offer of this StackedRevenuesResult.
        :rtype: FlexOffer
        """
        return self._flex_offer

    @flex_offer.setter
    def flex_offer(self, flex_offer: FlexOffer):
        """Sets the flex_offer of this StackedRevenuesResult.


        :param flex_offer: The flex_offer of this StackedRevenuesResult.
        :type flex_offer: FlexOffer
        """
        if flex_offer is None:
            raise ValueError("Invalid value for `flex_offer`, must not be `None`")  # noqa: E501

        self._flex_offer = flex_offer

    @property
    def revenues(self) -> StackedRevenuesResultRevenues:
        """Gets the revenues of this StackedRevenuesResult.


        :return: The revenues of this StackedRevenuesResult.
        :rtype: StackedRevenuesResultRevenues
        """
        return self._revenues

    @revenues.setter
    def revenues(self, revenues: StackedRevenuesResultRevenues):
        """Sets the revenues of this StackedRevenuesResult.


        :param revenues: The revenues of this StackedRevenuesResult.
        :type revenues: StackedRevenuesResultRevenues
        """
        if revenues is None:
            raise ValueError("Invalid value for `revenues`, must not be `None`")  # noqa: E501

        self._revenues = revenues
