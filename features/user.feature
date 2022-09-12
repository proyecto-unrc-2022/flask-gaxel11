Feature: Handle storing, retrieving and deleting customer details # test/features/user.feature:1

  Scenario: Retrieve a customers details
    Given some users are in the system
    When I retrieve the customer 'jasonb'
    Then I should get a '200' response
    And the following user details are returned:
      | name        |
      | Jason Borne |

  Scenario: Agregar nuevo usuario
      Given un usuario que no existe en la lista de usuarios existentes
      And se lo recibe a traves de un POST
      When yo agrego ese usuario nuevo
      Then deberia de obtener un '200'
      And mostrar el mensaje: Created user

  Scenario: Mostrar todos los usuarios
      Given un usuario ingresa al sistema
      And recibo una solicitud GET
      Then deberia de obtener un '200'
      And mostrar todos los usuarios
      | name        |
      | Jason Borne |
      | Esto Esuntest |

  Scenario: Modificar un usuario
      Given ingresa con un usuario existente
      When modifico ese usuario
      Then deberia de obtener un '200'
      And mostrar los detalles de ese usuario modificado
  
  Scenario: Eliminar un usuario
      Given se ingresa al sistema con un usuario existente
      When se elimina el usuario 
      Then deberia de obtener un '200'
      And mostrar el mensaje: User Deleted
