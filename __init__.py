# The COPYRIGHT file at the top level of this repository contains the full
# copyright notices and license terms.
from trytond.pool import Pool
from .asset import *


def register():
    Pool.register(
        Vehicle,
        module='asset_vehicle', type_='model')