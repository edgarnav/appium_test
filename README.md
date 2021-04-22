# appium_test

As requested in the instructions, 3 test cases or scenarios were automated. I'm using BDD with the behave python library and as a framework or architecture POM.
I'm also adding a log and reporter with allure. This is the example of the command to execute it:

behave /Path/to/proyect/appium_test -f allure_behave.formatter:AllureFormatter -o /Path/to/proyect/appium_test/reports
