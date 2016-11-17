import json
import urllib2
from models import Company, Material
from peewee import SqliteDatabase


# function creates empty database
def create_database():
    with open("/home/wojtas/PycharmProjects/aplikacja/data.db", "a") as f:
        f.write("")
    db = SqliteDatabase("data.db")
    db.connect()
    db.create_table(Company)
    db.create_table(Material)


#
def fetch_data(url):
    """ getting company data from url

    :param url: string with endpoint address
    :return: dict with fetched data
    """
    f = urllib2.urlopen(url)
    return json.loads(f.read())


# put company data to database
def get_data_comapny():
    for i in fetch_data('http://193.142.112.220:8337/companyList'):
        yield {"name": i['companyName'],
               "id": i['companyID']
               }


def get_data_material():
    for i in fetch_data("http://193.142.112.220:8337/materialList"):
        yield get_material(i['ID'], i['companyID'])


def get_material(id, comp_ID):
    material = fetch_data("http://193.142.112.220:8337/materialDetails?ID={id}".format(id=id))
    return {"mat_id": material['ID'],
            "mat_name": material['name'],
            'comp_id': comp_ID,
            "description": material['description'],
            "notes": material['notes'],
            "supplier": material['supplier'],
            "price": material['price'],
            'currency': material['currency'],
           }


if __name__ == '__main__':
    create_database()
    Company.insert_many(get_data_comapny()).execute()
    Material.insert_many(get_data_material()).execute()