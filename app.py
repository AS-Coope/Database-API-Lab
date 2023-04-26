from flask import Flask, request, make_response
import mysql.connector 

app = Flask(__name__)
'''
@app.route('/hello_world', methods=['GET'])
def hello_world():
    return "hello world"
''' 

# A: GET ALL CUSTOMERS
@app.route('/customers', methods=['GET'])
def get_customers():
    try:
        # connects to the database
        cnx = mysql.connector.connect(user='new_user', password='password',
                                    host = '127.0.0.1',
                                    database = 'lab3work')
        cursor = cnx.cursor()
        cursor.execute('SELECT * from Customers')
        customer_list = []
        for customerID, gender, age, annualIncome, spendingScore, profession, workExperience, familySize in cursor:
            customer = {}
            customer['CustomerID'] = customerID
            customer['Gender'] = gender
            customer['Age'] = age
            customer['AnnualIncome'] = annualIncome
            customer['SpendingScore'] = spendingScore
            customer['Profession'] = profession
            customer['WorkExperience'] = workExperience
            customer['FamilySize'] = familySize
            customer_list.append(customer)
        cursor.close()
        cnx.close()
        return make_response(customer_list) # by default make_response returns a 200, which means everything is OK
    except Exception as e:
        return make_response({'Error': 'Could not get all the customers'}, 400)
    #str(e)
    

# B: GET CUSTOMER BY ID
@app.route('/customer/<customer_id>', methods=['GET'])
def get_customer(customer_id):
    try:
        # connects to the database
        cnx = mysql.connector.connect(user='new_user', password='password',
                                    host = '127.0.0.1',
                                    database = 'lab3work')
        cursor = cnx.cursor()
        cursor.execute(f'SELECT * from Customers WHERE CustomerID = {customer_id} ')
        customer_list = []
        for customerID, gender, age, annualIncome, spendingScore, profession, workExperience, familySize in cursor:
            customer = {}
            customer['CustomerID'] = customerID
            customer['Gender'] = gender
            customer['Age'] = age
            customer['AnnualIncome'] = annualIncome
            customer['SpendingScore'] = spendingScore
            customer['Profession'] = profession
            customer['WorkExperience'] = workExperience
            customer['FamilySize'] = familySize
            customer_list.append(customer)
        cursor.close()
        cnx.close()
        return make_response(customer_list) # by default make_response returns a 200, which means everything is OK
    except Exception as e:
        return make_response({'Error': 'Could not get a customer based off that customer ID'}, 400)
    #str(e)

# C: ADD A CUSTOMER
@app.route('/add_customer', methods=['POST'])
def add_customer():
    try:
        cnx = mysql.connector.connect(user='new_user', password='password',
                                      host = '127.0.0.1',
                                      database = 'lab3work')
        cursor = cnx.cursor()
        customer_id = request.form.get('customer_id')
        gender = request.form.get('gender')
        age = request.form.get('age')
        annualIncome = request.form.get('annualIncome')
        spendingScore = request.form.get('spendingScore')
        profession = request.form.get('profession')
        workExperience = request.form.get('workExperience')
        familySize = request.form.get('familySize')
        cursor.execute(f"INSERT INTO Customers VALUES('{customer_id}', '{gender}', '{age}', '{annualIncome}', '{spendingScore}', '{profession}', '{workExperience}', '{familySize}')") # performs the queries
        cnx.commit() # sends to database
        cursor.close()
        cnx.close()
        return make_response({'success': f'Customer added'}, 201)
    except Exception as e:
        print(e)
        return make_response({'error': "An error has occurred; could not add the customer"}, 400)
    

# D: UPDATE CUSTOMER PROFESSION USING THEIR CUSTOMER ID
@app.route('/update_profession/<customer_id>', methods=['PUT'])
def update_profession(customer_id):
    try:
        cnx = mysql.connector.connect(user='new_user', password = 'password',
                                      host = "127.0.0.1",
                                      database = 'lab3work')
        cursor = cnx.cursor()
        content = request.json # reading json object
        profession = content['profession']
        cursor.execute(f"UPDATE Customers SET Profession='{profession}' WHERE CustomerID = {customer_id}")
        cnx.commit() # send to the database
        cursor.close()
        return make_response({'success' : "Customer profession updated"}, 202)
    except Exception as e:
        return make_response({'error': 'Could not get the customer profession using that Customer ID'}, 400)
    #str(e)

# E: GET CUSTOMER BY HIGHEST INCOME REPORT
@app.route('/highest_income_report', methods=['GET'])
def get_highest_income_report():
    try:
        # connects to the database
        cnx = mysql.connector.connect(user='new_user', password='password',
                                    host = '127.0.0.1',
                                    database = 'lab3work')
        cursor = cnx.cursor()
        #cursor.execute("SET GLOBAL sql_mode=(SELECT REPLACE(@@sql_mode,'ONLY_FULL_GROUP_BY',''));")
        cursor.execute(f'SELECT MAX(CustomerID), MAX(AnnualIncome), Profession from Customers GROUP BY Profession ')
        customer_list = []
        for customerID, annualIncome, profession in cursor:
            customer = {}
            customer['CustomerID'] = customerID
            customer['AnnualIncome'] = annualIncome
            customer['Profession'] = profession
            customer_list.append(customer)
        cursor.close()
        cnx.close()
        return make_response(customer_list) # by default make_response returns a 200, which means everything is OK
    except Exception as e:
        return make_response({'Error': 'Could not get the customer with the highest income per profession'}, 400)
    #str(e)
    
# F: GET THE TOTAL INCOME FOR EACH PROFESSION
@app.route('/total_income_report', methods=['GET'])
def get_total_income_report():
    try:
        # connects to the database
        cnx = mysql.connector.connect(user='new_user', password='password',
                                    host = '127.0.0.1',
                                    database = 'lab3work')
        cursor = cnx.cursor()
        cursor.execute(f'SELECT SUM(AnnualIncome), Profession from Customers GROUP BY Profession ')
        customer_list = []
        for annualIncome, profession in cursor:
            customer = {}
            customer['AnnualIncome'] = annualIncome
            customer['Profession'] = profession
            customer_list.append(customer)
        cursor.close()
        cnx.close()
        return make_response(customer_list) # by default make_response returns a 200, which means everything is OK
    except Exception as e:
        return make_response({'Error': 'Could not get total income for each profession'}, 400)
    #str(e)
    
# G: GET THE AVERAGE WORK EXPERIENCE FOR EACH PROFESSION
@app.route('/average_work_experience', methods=['GET'])
def get_average_work_experience():
    try:
        # connects to the database
        cnx = mysql.connector.connect(user='new_user', password='password',
                                    host = '127.0.0.1',
                                    database = 'lab3work')
        cursor = cnx.cursor()
        cursor.execute(f'SELECT AVG(WorkExperience), Profession from Customers WHERE AnnualIncome > 5000 AND Age > 35 GROUP BY Profession ')
        customer_list = []
        for workExperience, profession in cursor:
            customer = {}
            customer['WorkExperience'] = workExperience
            customer['Profession'] = profession
            customer_list.append(customer)
        cursor.close()
        cnx.close()
        return make_response(customer_list) # by default make_response returns a 200, which means everything is OK
    except Exception as e:
        return make_response({'Error': 'Could not get average work experience based on profession'}, 400)
    #str(e)

# H: GET THE AVERAGE SPENDING SCORE DEPENDING ON THE PROFESSION
@app.route('/average_spending_score/<profession>', methods=['GET'])
def get_average_spending_score(profession):
    try:
        # connects to the database
        cnx = mysql.connector.connect(user='new_user', password='password',
                                    host = '127.0.0.1',
                                    database = 'lab3work')
        cursor = cnx.cursor()
        cursor.execute(f'SELECT Gender, AVG(SpendingScore) from Customers WHERE Profession={profession} GROUP BY Gender ')
        customer_list = []
        for gender, spendingScore in cursor:
            customer = {}
            customer['Gender'] = gender
            customer['SpendingScore'] = spendingScore
            customer_list.append(customer)
        cursor.close()
        cnx.close()
        return make_response(customer_list) # by default make_response returns a 200, which means everything is OK
    except Exception as e:
        return make_response({'Error': 'Could not update profession'}, 400)
    #str(e)

'''
@app.route('/delete_student/<student_id>', methods=['DELETE'])
def delete_student(student_id):
    try: 
        cnx = mysql.connector.connect(user='new_user', password='password',
                                    host='127.0.0.1',
                                    database='uwi')
        cursor = cnx.cursor()
        cursor.execute(f"DELETE FROM student WHERE StudentID = {student_id}")
        cnx.commit()
        cursor.close()
        cnx.close()
        return make_response({'success': " Student deleted"}, 204)
    except Exception as e:
        return make_response({'error': str(e)}, 400)
'''
if __name__ == '__main__':
    app.run(port = 5000)
