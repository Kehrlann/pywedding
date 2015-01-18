#coding=utf-8
from wedding import app
from gdata.spreadsheet.text_db import DatabaseClient
from datetime import datetime

print "connect"
client          =   DatabaseClient(username=app.config['GOOGLE_USERNAME'], password=app.config['GOOGLE_PASSWORD'])
db              =   client.GetDatabases(name=app.config['SPREADSHEET_NAME'])[0]
wishlist        =   db.GetTables(name="wishlist")[0]
accommodation   =   db.GetTables(name="accommodation")[0]
print "connected"


class Item:
    """
    Represents an item in the wishlist.

    Properties :
    - id            :   the row_id of the row in the wishlist
    - title         :   name of the item
    - description   :   description
    - photo         :   (optional) the URL of the picture
    - link          :   (optional) URL of the item (reference, description ...)
    - reserved      :   Whether this item has been reserved or not
    """
    def __init__(self, record):
        self.record         =   record
        self.id             =   record.row_id
        self.title          =   record.content['title']
        self.description    =   record.content['description']
        self.photo          =   record.content['photo']
        self.link           =   record.content['link']
        self.reserved       =   record.content['mail'] is not None


class Accommodation:
    """
    Represents an accommodation.

    Properties :
    - id            :   the row_id of the row in the wishlist
    - name          :   name of the accommodation
    - type          :   type (camping, hotel, hostel, etc)
    - site          :   (optional) url of the website of the accommodation
    - email         :   (optional) contact e-mail
    - phone         :   (optional) contact phone
    """
    def __init__(self, record):
        self.record     =   record
        self.id         =   record.row_id
        self.name       =   record.content['name']
        self.address    =   record.content['address']
        self.type       =   record.content['type']
        self.site       =   record.content['site']
        self.email      =   record.content['email']
        self.phone      =   record.content['phone']


def load_wishlist():
    """
    Load all items in the wishlist (300 max). google requires a limit...
    """
    records = wishlist.GetRecords(1,300)
    return [Item(r) for r in records]



def load_accommodation():
    """
    Load all items in the list of accommodation (300 max). google requires a limit...
    """
    records = accommodation.GetRecords(1,300)
    return [Accommodation(r) for r in records]



def update_wishlist_by_id(id, mail):
    """
    Update an item of the wishlist, setting an e-mail.
    """
    r = wishlist.GetRecord(row_id=id)

    if r is not None:
        r.content['mail'] = mail
        r.content['date'] = datetime.now().strftime('%Y/%m/%d %H:%M')
        r.Push()
        return True

    return False