#coding=utf-8
from pywedding import app
from gdata.spreadsheet.service import SpreadsheetsService, ListQuery
from gdata.spreadsheet.text_db import Record
from datetime import datetime

client  = SpreadsheetsService()
feed    = client.GetWorksheetsFeed(visibility='public', projection='basic', key=app.config['SPREADSHEET_KEY'])
sheet   = None
for s in feed.entry:
  if s.title.text == 'wishlist':
      wishlist = s
  elif s.title.text == 'accommodation':
      accommodation = s



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
        print record.content
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
    #records = wishlist.GetRecords(1,300)

    row_query = ListQuery()
    row_query.start_index = str(1)
    rows_feed = client.GetListFeed(key=app.config['SPREADSHEET_KEY'], visibility='public', projection='full', wksht_id=wishlist.id.text.split('/')[-1])

    records = []

    for row in rows_feed.entry:
        records.append  (   Record  (   spreadsheet_key=app.config['SPREADSHEET_KEY'],
                                        worksheet_id=wishlist.id.text.split('/')[-1],
                                        row_entry=row,
                                    )
                        )

    return [Item(r) for r in records]



def load_accommodation():
    """
    Load all items in the list of accommodation (300 max). google requires a limit...
    """
    row_query = ListQuery()
    row_query.start_index = str(1)
    rows_feed = client.GetListFeed(key=app.config['SPREADSHEET_KEY'], visibility='public', projection='full', wksht_id=accommodation.id.text.split('/')[-1])

    records = []

    for row in rows_feed.entry:
        records.append  (   Record  (   spreadsheet_key=app.config['SPREADSHEET_KEY'],
                                        worksheet_id=accommodation.id.text.split('/')[-1],
                                        row_entry=row
                                    )
                        )

    return [Accommodation(r) for r in records]




def update_wishlist_by_id(id, mail):
    """
    Update an item of the wishlist, setting an e-mail.
    """
    row = client.GetListFeed(key=app.config['SPREADSHEET_KEY'], visibility='public', projection='full', wksht_id=wishlist.id.text.split('/')[-1], row_id=id)
    r = Record(content=None, row_entry=row,
           spreadsheet_key=app.config['SPREADSHEET_KEY'],
           worksheet_id=wishlist.id.text.split('/')[-1], database_client=client)

    if r is not None:
        r.content['mail'] = mail
        r.content['date'] = datetime.now().strftime('%Y/%m/%d %H:%M')
        client.UpdateRow(row, r.content)
        return True

    return False