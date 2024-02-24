from pydantic import BaseModel

class ContactDetails(BaseModel):
    email: str | None
    mobile: str | None
    customerServiceNumber: str | None
    phone: str | None
class Consoles(BaseModel):
    url: str
    
class StoreData(BaseModel):
    nameAr: str
    contactDetails: ContactDetails
    consoles: Consoles
    def model_dump(self) -> dict:
        return {
            "nameAr": self.nameAr,
            "email": self.contactDetails.email,
            "phone": self.contactDetails.phone,
            "mobile": self.contactDetails.mobile,
            "customerServiceNumber": self.contactDetails.customerServiceNumber,
            "url": self.consoles.url
        }
    