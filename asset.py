#The COPYRIGHT file at the top level of this repository contains the full
#copyright notices and license terms.
from trytond.model import ModelSQL, ModelView, fields

__all__ = ['Vehicle']


class Vehicle(ModelSQL, ModelView):
    'Vehicle'
    __name__ = 'asset.vehicle'
    asset = fields.Many2One('asset', 'Asset', required=True,
        ondelete='CASCADE')
    description = fields.Char('Description')
    driver = fields.Many2One('company.employee', 'Driver',
        help='The driver that normally drives this vehicle')
    technical_description = fields.Text('Technical Description')
    active = fields.Function(fields.Boolean('Active'),
        'get_active', searcher='search_active')

    def get_rec_name(self, name):
        return self.asset.name

    @classmethod
    def search_rec_name(cls, name, clause):
        return [('asset.name',) + tuple(clause[1:])]

    def get_active(self, name):
        return self.asset.active

    @classmethod
    def search_active(cls, name, clause):
        return [('asset.active',) + tuple(clause[1:])]
