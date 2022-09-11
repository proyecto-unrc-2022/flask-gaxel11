from email import header
import json
from behave import *
from application import USERS

#Scenario: Retrieve a customers details
@given('some users are in the system')
def step_impl(context):
    USERS.update({'jasonb': {'name': 'Jason Bourne'}})

@when('I retrieve the customer \'jasonb\'')
def step_impl(context):
    context.page = context.client.get('/users/{}'.format('jasonb'))
    assert context.page

@then('I should get a \'200\' response')
def step_impl(context):
    assert context.page.status_code is 200

@then('the following user details are returned')
def step_impl(context):
    # assert context.table[0].cells[0] in context.page.text
    assert "Jason Bourne" in context.page.text


#Scenario: Agregar nuevo usuario
@given('un usuario \'test\' que no existe en la lista de usuarios')
def step_given(self) :
   assert (not USERS.get('test'))  

@given('se lo recibe a traves de un POST')
def step_given(context) :
    context.headers = {'Content-Type': 'application/json'}
    context.page = context.client.post('/users', data=json.dumps({"test": "Esto Esuntest"}), headers=context.headers)
    assert context.page
    
@when('yo agrego ese usuario nuevo')
def step_when(self) :
    USERS.update({'test': {'name': 'Esto Esuntest'}})
    assert (USERS.get('test'))  
    
@then('deberia de obtener un \'200\'')
def step_then(context) :
    assert context.page.status_code is 200
  

@then('mostrar el mensaje: Created user')
def step_then(context) :
    assert "Created user" in context.page.text


#Scenario: Mostrar todos los usuarios
@given('un usuario ingresa al sistema')
def step_given(self) :
    USERS.update({'jasonb': {'name': 'Jason Bourne'}})
    USERS.update({'test': {'name': 'Esto Esuntest'}})

@given('recibo una solicitud GET')
def step_given(context) :
    context.page = context.client.get('/users')
    assert context.page
    
@then('mostrar todos los usuarios')
def step_then(context) :
    print(USERS)
    print(context.page.text)
    assert USERS == json.loads(context.page.text)

