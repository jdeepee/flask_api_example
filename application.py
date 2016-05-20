from api.app import application
#Importing application into master applicaion file to allow easy relative imports in application. 
#Master file named application so AWS elastic beanstalk or other Saas services can run our application

if __name__ == '__main__':
	application.run(debug=True)