# The COPYRIGHT file at the top level of this repository contains the full
# copyright notices and license terms.

from trytond.model import fields
from trytond.pool import PoolMeta
from trytond.pyson import Eval


__all__ = ['Asset']

__metaclass__ = PoolMeta

_STATES = {
    'invisible': Eval('type') != 'vehicle',
    }
_DEPENDS = ['type']


class Asset:
    __name__ = 'asset'

    description = fields.Char('Description', states=_STATES, depends=_DEPENDS)
    driver = fields.Many2One('company.employee', 'Driver',
        help='The driver that normally drives this vehicle',
        states=_STATES, depends=_DEPENDS)
    technical_description = fields.Text('Technical Description',
        states=_STATES, depends=_DEPENDS)

    @classmethod
    def __setup__(cls):
        super(Asset, cls).__setup__()
        vehicle = ('vehicle', 'Vehicle')

        if vehicle not in cls.type.selection:
            cls.type.selection.append(vehicle)
