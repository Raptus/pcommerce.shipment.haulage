from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile

from pcommerce.shipment.haulage.browser.base import HaulageBase

class HaulageOverview(HaulageBase):
    template = ViewPageTemplateFile('overview.pt')