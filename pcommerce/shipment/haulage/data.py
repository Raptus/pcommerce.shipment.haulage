from pcommerce.core.data import ShipmentData

def HaulageShipmentData(as_customer=True, address=None):
    data = ShipmentData('pcommerce.shipment.haulage')
    data.as_customer = as_customer
    data.address = address
    return data
