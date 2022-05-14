from pydantic import BaseModel

class AddressBook(BaseModel):
    name : str
    address: str
    phone : int
    long : float
    lat:float
    distance : int


class ShowAddressBook(AddressBook):
    name : str
    address: str
    phone : int
    long : float
    lat:float
    distance : int
    class Config():
        orm_mode =True
