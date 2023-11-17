*** Settings ***
Resource  resource.robot
Test Setup  Create User Command

*** Test Cases ***
Register With Valid Username And Password
    Output Should Contain  New user registered


Register With Already Taken Username And Valid Password
    Input New Command
    Input Credentials  jyrkiollila  jyrkiollila123
    Output Should Contain  User with username jyrkiollila already exists


Register With Too Short Username And Valid Password
    Input New Command
    Input Credentials  j  jyrkiollila123
    Output Should Contain  Username should be at least 3 characters long and only contain letters a-z.

Register With Enough Long But Invalid Username And Valid Password
    Input New Command
    Input Credentials  jyrkiollila!!!  jyrkiollila123
    Output Should Contain  Username should be at least 3 characters long and only contain letters a-z.

Register With Valid Username And Too Short Password
    Input New Command
    Input Credentials  jyrkiollila  jyrki
    Output Should Contain  Password should be at least 8 characters long and contain special symbols and/or numbers.

Register With Valid Username And Long Enough Password Containing Only Letters
    Input New Command
    Input Credentials  jyrkiollila  jyrkiollila
    Output Should Contain  Password should be at least 8 characters long and contain special symbols and/or numbers.

*** Keywords ***
Create User Command
    Input New Command
    Input Credentials  jyrkiollila  jyrkiollila123
