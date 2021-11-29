#noinspection CucumberUndefinedStep
Feature: Login

  Scenario: Login correcto

    Given Preparar clases para el flujo de login
    When Verificar vista home
    When Presionar boton tu cuenta
    When Presionar boton login en tu cuenta
    Then Validar vista login
    When Ingresar usuario y contraseña edgar.navarrete@coppel.com 123456
    Then Presionar boton iniciar sesion
    And Validar home despues de login
