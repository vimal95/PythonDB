from flask import Flask, render_template, json, request
import mysql.connector

app = Flask(__name__)
app.config["TEMPLATES_AUTO_RELOAD"] = True


@app.route('/')
def main():
    return render_template('index.html')

@app.route('/DB')
def showSignUp():
    return render_template('DB.html')



@app.route('/test', methods=['GET', 'POST'])
def Test():
    
    

    SQLStatement='''SELECT * from DBTEST.Sample;'''
    #SQLStatement1="USE DBTEST;"
    #SQLStatement2="INSERT INTO Sample (ID,EMPName) VALUES (%s,%s);"
    SQLStatement2="INSERT INTO Sample (EMPName,EMPRole,EMPNumber) VALUES (%s,%s,%s);"
    #SQLStatement3="UPDATE Sample SET EMPRole = %s WHERE EMPName = %s;"
    #SQLStatement4="UPDATE Sample SET EMPNumber = %s WHERE EMPName= %s;"
    
    try:
        if request.method=='POST':
            
            EmployeeName = request.form['inputName']
            EmployeeRole = request.form['inputRole']
            EmployeeNumber = request.form['inputNumber']
            
        #Number = request.form['inputNumber']
        #password = request.form['inputPassword']
        
            Connection = mysql.connector.connect(host='localhost',database='DBTEST',user='Admin',password='Guidanz@123')
            #return("Connected to MYSql DB Successfully")
            Cursor = Connection.cursor()
            Cursor.execute(SQLStatement)
        
            List=[]
        
            for row in Cursor:
                List.append(row[1])
            
            
            if EmployeeName in List:
            
                return("Entered input already found in database")
            
            else:
                
                #Cursor.execute(SQLStatement1)
            #Cursor.execute(SQLStatement2,(Number,name))
                Cursor.execute(SQLStatement2,(EmployeeName,EmployeeRole,EmployeeNumber))
                Connection.commit()
         
            Connection.close()
            
#return json.dumps({'message':'User created successfully !'})   
    except:
        return("Exception Occured")
    
    return render_template('DB.html')   


@app.route('/search', methods=['POST'])
def search():
    
    fetch_data = None
    test_string = ""
    if request.method=="POST":
        
        try:
            searchname = request.form['inputSearch']
            #SQLStatement7='''SELECT * from DBTEST.Sample;'''
            Connection = mysql.connector.connect(host='localhost',database='DBTEST',user='Admin',password='Guidanz@123')
            #return("Connected to MYSql DB Successfully")
            SQLStatement6='SELECT * from DBTEST.Sample where EMPName=%s;'
            Cursor = Connection.cursor()
            Cursor.execute(SQLStatement6,(searchname,))
            fetch_data = Cursor.fetchall()
            test_string="".join(str(datatest) for datatest in fetch_data)
        except Exception as e:
            str(e)
            
    return render_template("DB.html",data=test_string)
        
@app.route("/fetch")
def fetchall():
    
   
    SQLStatement='''SELECT * from DBTEST.Sample;'''
    
    Connection = mysql.connector.connect(host='localhost',database='DBTEST',user='Admin',password='Guidanz@123')
    #return("Connected to MYSql DB Successfully")
    Cursor = Connection.cursor()
    Cursor.execute(SQLStatement)
    
    data=Cursor.fetchall()
    
    return render_template("save.html",data=data)
    
    
            
           
if __name__ == "__main__":
    app.run(port=5002)
    
