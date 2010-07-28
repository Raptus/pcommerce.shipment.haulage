from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from Products.CMFCore.utils import getToolByName

from pcommerce.core.interfaces import IAddressFactory
from pcommerce.shipment.haulage.browser.base import HaulageBase
from pcommerce.shipment.haulage.data import HaulageShipmentData

class HaulageShipment(HaulageBase):
    template = ViewPageTemplateFile('shipment.pt')
    
    def validate(self):
        self.errors = {}
        haulage_as_customer = self.request.form.get('haulage_address_as_customer', False)
        if not haulage_as_customer:
            factory = IAddressFactory(self.request)
            self.errors = factory.validate('haulage_address')
        return len(self.errors) == 0
    
    def process(self):
        self.data = HaulageShipmentData()
        address_as_customer = self.request.form.get('haulage_address_as_customer', False)
        if not address_as_customer:
            factory = IAddressFactory(self.request)
            self.data.address = factory.create('haulage_address')
        self.data.as_customer = address_as_customer
        props = getToolByName(self.context, 'portal_properties').pcommerce_properties
        self.data.pretaxcharge = props.getProperty('haulage_pretaxcharge', 0.0)
        self.data.posttaxcharge = props.getProperty('haulage_posttaxcharge', 0.0)
        return self.data
