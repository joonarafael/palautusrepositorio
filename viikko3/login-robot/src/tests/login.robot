*** Settings ***
Resource  resource.robot
Test Setup  Create User And Input Login Command

*** Test Cases ***
Login With Correct Credentials
    Input Credentials  kallematias  kallematias123
    Output Should Contain  Logged in

Login With Incorrect Password
    Input Credentials  kallematias  123
    Output Should Contain  Invalid username or password

Login With Nonexistent Username
    Input Credentials  jyrki  kallematias123
    Output Should Contain  Invalid username or password

*** Keywords ***
Create User And Input Login Command
    Create User  kallematias  kallematias123
    Input Login Command

