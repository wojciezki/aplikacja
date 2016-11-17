import wtforms
from manage_data import get_material
from bottle import request, route, run, view, static_file, redirect, error
from models import Company, Material


# Edit form class for editing data
class MaterialForm(wtforms.Form):
    mat_name = wtforms.StringField('name')
    comp_id = wtforms.StringField('comp_id')
    description = wtforms.StringField('description')
    notes = wtforms.StringField('notes')
    supplier = wtforms.StringField('supplier')
    price = wtforms.StringField('price')
    currency = wtforms.StringField('currency')
    ID = wtforms.StringField('ID')


# login view
@route('/')
@route("/login/", method=['GET', 'POST'])
@view("login")
def login():
    users = {"a": "1"}
    login = request.forms.get('username')
    password = request.forms.get('password')
    if login in users:
        if password == users[login]:
            return redirect('/companies/')
        else:
            redirect('/')


# companies view
@route("/companies/")
@view('companies')
def companies():
    return dict(companies=[dict(
        companyName=i.name,
        companyID=i.id
    ) for i in Company().select()])


# material view
@route("/companies/<id:int>/")
@view('materials')
def comp_materials(id):
    return dict(comp_materials=[dict(
        name=mat.mat_name,
        ID=mat.mat_id,
        id=mat.id
    ) for mat in Material.select().where(Material.comp_id == id)])


# list of material view
@route('/material/<id:int>/')
@view("material")
def material(id):
    material_specification = Material.select().where(Material.mat_id == id).get()
    return dict(material=[dict(
        name=material_specification.mat_name,
        ID=material_specification.mat_id,
        id=material_specification.comp_id,
        description=material_specification.description,
        notes=material_specification.notes,
        supplier=material_specification.supplier,
        price=material_specification.price,
        currency=material_specification.currency
    )])


# edit material view
@route('/material/<id:int>/edit/', method=['POST', 'GET'])
@view('edit')
def edit_data(id):
    #import pdb
    #pdb.set_trace()
    edit_mat = Material.select().where(Material.mat_id == id).get()
    form = MaterialForm(obj=edit_mat)
    if request.method == 'POST':
        form = MaterialForm(request.POST, edit_mat)
        if form.validate():
            form.populate_obj(edit_mat)
            edit_mat.save()
            redirect('/material/{id}/'.format(id=id))
    return {'form': form, 'id': id}


#  restore view
@route('/material/<id:int>/restore/', method=['GET', 'POST'])
@view('restore')
def restore(id):
    if request.method == 'POST':
        edit_mat = Material.select().where(Material.mat_id == id).get()
        mat = get_material(id, edit_mat.comp_id)
        edit_mat.mat_id = mat.get("mat_id", "")
        edit_mat.mat_name = mat.get("mat_name", "")
        edit_mat.comp_id = edit_mat.comp_id
        edit_mat.description = mat.get("description", "")
        edit_mat.notes = mat.get("notes", "")
        edit_mat.supplier = mat.get("supplier", "")
        edit_mat.price = mat.get("price", "")
        edit_mat.currency = mat.get("currency", "")
        edit_mat.save()
        redirect('/material/{id}/'.format(id=id))
    return {'id': id}




@error(404)
def error404(error):
    return 'Ups, there is some mistake'


# filec that make everything look skeletonlike
@route('/static/<filepath:path>')
def server_static(filepath):
    return static_file(filepath, root='/home/wojtas/PycharmProjects/rekrutacja/static')

if __name__ == '__main__':
    run(host="localhost", port=8080, debug=True)