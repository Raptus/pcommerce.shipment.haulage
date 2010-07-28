from zope.interface import implements, Interface
from zope.component import adapts

from pcommerce.core import PCommerceMessageFactory as _
from pcommerce.core.interfaces import IShipmentMethod
from pcommerce.shipment.haulage.interfaces import IHaulageShipment

class HaulageShipment(object):
    implements(IShipmentMethod, IHaulageShipment)
    adapts(Interface)
    
    title = _('Haulage')
    description = _('Shipment by a haulage company')
    icon = '++resource++pcommerce_shipment_haulage_icon.gif'
    logo = '++resource++pcommerce_shipment_haulage_logo.gif'
    
    def __init__(self, context):
        self.context = context
    
    def mailInfo(self, order, lang=None, customer=False):
        data = order.shipmentdata['pcommerce.shipment.haulage']
        address = data.as_customer and order.address or data.address
        return _('haulage_mailinfo', default="""Haulage shipment address
${address}""", mapping=dict(address=address.mailInfo(self.context.REQUEST, lang, customer)))
