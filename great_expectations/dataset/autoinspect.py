"""
Autoinspect utilities to automatically generate expectations by evaluating a data_asset.
"""
from __future__ import division

import warnings
from six import string_types

from .util import create_multiple_expectations


class AutoInspectError(Exception):
    """Exception raised for errors in autoinspection.

    Attributes:
        message -- explanation of the error
    """

    def __init__(self, message):
        self.message = message


def columns_exist(inspect_dataset):
    """
    This function will take a dataset and add expectations that each column present exists.

    Args:
        inspect_dataset (great_expectations.dataset): The dataset to inspect and to which to add expectations.
    """
    if not hasattr(inspect_dataset, 'table_columns'):
        warnings.warn(
            "No columns list found in dataset; no autoinspection performed.")
        return
    if not isinstance(inspect_dataset.table_columns[0], string_types):
        raise AutoInspectError("Unable to determine column names for this dataset.")
    create_multiple_expectations(inspect_dataset, inspect_dataset.table_columns, "expect_column_to_exist")
