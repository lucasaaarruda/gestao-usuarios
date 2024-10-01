from flask import Blueprint, render_template

cliente_route = Blueprint('cliente', __name__)

@cliente_route.route('/')
def lista_clientes():
    """ Listar os clientes """
    return render_template('lista_clientes.html')

@cliente_route.route('/', methods=['POST'])
def inserir_cliente():
    """ Inserir os dados do cliente no servidor """
    pass

@cliente_route.route('/new')
def form_cliente():
    """ Renderiza o formulario para cadastrar um cliente """
    return render_template('form_cliente.html')

@cliente_route.route('/<int:cliente_id>')
def detalhe_cliente(cliente_id):
    """ Obtem dados do cliente """
    return render_template('detalhe_cliente.html')

@cliente_route.route('/<int:cliente_id>/edit')
def form_edit_cliente(cliente_id):
    """ Renderiza o formulário para editar um cliente """
    return render_template('form_edit_cliente.html')

@cliente_route.route('/<int:cliente_id>/update', methods=['PUT'])
def atualizar_cliente(cliente_id):
    """ Atualizar dados do cliente """
    pass

@cliente_route.route('/<int:cliente_id>/delete', methods=['DELETE'])
def deletar_cliente(cliente_id):
    """ Deleta o registro do cliente """
    pass