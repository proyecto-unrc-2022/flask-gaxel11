Feature: Handle storing, retrieving and deleting customer details # test/features/user.feature:1

  Scenario: Retrieve a customers details
    Given some users are in the system
    When I retrieve the customer 'jasonb'
    Then I should get a '200' response
    And the following user details are returned:
      | name        |
      | Jason Borne |

  Scenario: Agregar nuevo usuario
      Given un usuario 'test' con nombre 'Esto Esuntest' que no existe en USERS
      And se lo recibe a traves de un POST
      When yo agrego ese usuario nuevo
      Then deberia responder con un '200'
      And mostrar el mensaje: Created user

  Scenario: Mostrar todos los usuarios
      Given un usuario ingresa al sistema
      And recibo una solicitud GET
      Then deberia responder con un '200'
      And mostrar todos los usuarios
      | name        |
      | Jason Borne |
      | Esto Esuntest |
          