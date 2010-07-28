from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile

from pcommerce.shipment.haulage.browser.base import HaulageBase

class HaulageConfirmation(HaulageBase):
    template = ViewPageTemplateFile('confirmation.pt')