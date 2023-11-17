*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Go To Register New User Page

*** Test Cases ***
Register With Valid Username And Password
    Set Username  jyrki
    Set Password  jyrki123
    Set Password Confirmation  jyrki123
    Submit Credentials
    Register Should Succeed

Register With Too Short Username And Valid Password
    Set Username  j
    Set Password  jyrki123
    Set Password Confirmation  jyrki123
    Submit Credentials
    Register Should Fail With Message  Username should be at least 3 characters long and only contain letters a-z.

Register With Valid Username And Invalid Password
    Set Username  jyrki
    Set Password  jyrkijyrki
    Set Password Confirmation  jyrkijyrki
    Submit Credentials
    Register Should Fail With Message  Password should be at least 8 characters long and contain special symbols and/or numbers.

Register With Nonmatching Password And Password Confirmation
    Set Username  jyrki
    Set Password  jyrkijyrki
    Set Password Confirmation  jyrkikalle
    Submit Credentials
    Register Should Fail With Message  Passwords do not match.

Login After Successful Registration
    Set Username  matias
    Set Password  matias123
    Set Password Confirmation  matias123
    Submit Credentials
    Register Should Succeed
    Open Main Page
    Log Out
    Go To Login Page
    Set Username  matias
    Set Password  matias123
    Submit Login Credentials
    Login Should Succeed

Login After Failed Registration
    Set Username  matias
    Set Password  matias
    Set Password Confirmation  matias
    Submit Credentials
    Register Should Fail With Message  Password should be at least 8 characters long and contain special symbols and/or numbers.
    Go To Login Page
    Set Username  matias
    Set Password  matias
    Submit Login Credentials
    Login Should Fail With Message  Invalid username or password

*** Keywords ***
Register Should Succeed
    Welcome Page Should Be Open

Login Should Succeed
    Main Page Should Be Open

Register Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}

Login Should Fail With Message
    [Arguments]  ${message}
    Login Page Should Be Open
    Page Should Contain  ${message}

Submit Credentials
    Click Button  Register

Submit Login Credentials
    Click Button  Login

Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Set Password Confirmation
    [Arguments]  ${password_confirmation}
    Input Password  password_confirmation  ${password_confirmation}

Go To Register New User Page
    Go To Register Page
    Register Page Should Be Open

Open Main Page
    Click Link  Continue to main page

Log Out
    Click Button  Logout