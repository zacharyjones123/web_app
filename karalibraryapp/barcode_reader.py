#
import usb1

VENDOR_ID = "Hello"
PRODUCT_ID = "hELLO"
INTERFACE = "hELLO"
ENDPOINT = "hELLO"
BUFFER_SIZE = 20
with usb1.USBContext() as context:
    handle = context.openByVendorIDAndProductID(
        VENDOR_ID,
        PRODUCT_ID,
        skip_on_error=True,
    )
    if handle is None:
        # Device not present, or user is not allowed to access device.
        print("Device could not be found, wrong parameters")
    with handle.claimInterface(INTERFACE):
        # Do stuff with endpoints on claimed interface.
        print("The interface was found!, now use it")

        # Synchronous I/O
        while True:
            data = handle.bulkRead(ENDPOINT, BUFFER_SIZE)
            # Process data...
            print(data)
            print("We now have the data and the testing of it can begin!")


#Asynchronous I/0, with more error handling
def processReceivedData(transfer):
    if transfer.getStatus() != usb1.TRANSFER_COMPLETED:
        # Transfer did not complete successfully, there is no data to read.
        # This example does not resubmit transfers on errors. You may want
        # to resubmit in some cases (timeout, ...).
        return
    data = transfer.getBuffer()[:transfer.getActualLength()]
    # Process data...
    # Resubmit transfer once data is processed.
    transfer.submit()


# Build a list of transfer objects and submit them to prime the pump.
transfer_list = []
for _ in range(TRANSFER_COUNT):
    transfer = handle.getTransfer()
    transfer.setBulk(
        usb1.ENDPOINT_IN | ENDPOINT,
        BUFFER_SIZE,
        callback=processReceivedData,
    )
    transfer.submit()
    transfer_list.append(transfer)
# Loop as long as there is at least one submitted transfer.
while any(x.isSubmitted() for x in transfer_list):
    try:
        context.handleEvents()
    except usb1.USBErrorInterrupted:
        pass
