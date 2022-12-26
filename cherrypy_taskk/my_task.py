import cherrypy
import psycopg2,datetime


class HelloWorld(object):
    @cherrypy.expose
    def index(self):
        return """<html>
<head><link rel="stylesheet"href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css
"</head>
<body>
 
    <div class="container h-100">
      <div class="row d-flex justify-content-center align-items-center h-100">
        <div class="col-3>
          <div class="card" style="border-radius: 15px;">
            <div class="card-body p-5">
              <h2 class="text-uppercase text-center mb-5">Enter Your Details</h2>

                <form action="insert_value" method="get">

                <div class="form-outline mb-4">
                  <label class="form-label" for="form3Example1cg">Your Name</label>
                  <input type="text" id="form3Example1cg" class="form-control form-control-lg" placeholder="Enter Name" name="name"/>
                </div>

                <div class="form-outline mb-4">
                  <label class="form-label" for="form3Example3cg">Your Email</label>
                  <input type="email" id="form3Example3cg" class="form-control form-control-lg" placeholder="Enter Email" name="email"/>
                </div>

            
                 <div class="form-group" id="phoneid">
                            <label for="getphno">Age</label>
                            <input class="form-control"  name="age" type="number" placeholder="Enter Age" name="age"/>
                </div> 
                <div class="form-group" id="phoneid">
                            <label for="getphno">Phone Number</label>
                            <input class="form-control" id="getphno" maxlength="10" name="phone" pattern="[7-9]{1}[0-9]{9}" placeholder="Enter Phone Number" t-att-value="contact_phone" type="phone"/>
                </div>


                <div class="d-flex justify-content-center">
                  <button type="submit"
                    class="btn btn-success btn-block btn-lg gradient-custom-4 text-body">Submit</button>
                </div>

                
              </form>

            </div>
          </div>
        </div>
      </div>
    </div>
 

</body>
            </html>"""


    @cherrypy.expose
    def insert_value(self,*args,**kwargs):
        my_name=cherrypy.request.params.get('name')
        my_age=cherrypy.request.params.get('age')
        my_mail=cherrypy.request.params.get('email')
        my_no=cherrypy.request.params.get('phone')
        
        # print("------------------",name)
        conn = psycopg2.connect(
        database="cherrypytest",
        )
    #Setting auto commit false
        conn.autocommit = True

        #Creating a cursor object using the cursor() method
        cursor = conn.cursor()
        date=datetime.date.today()
        # Preparing SQL queries to INSERT a record into the database.
        cursor.execute('''INSERT INTO MYTABLE(NAME,AGE,EMAIL,PHONE) VALUES (%s,%s,%s,%s)''',(str(my_name),my_age,str(my_mail),str(my_no)))
        # Commit your changes in the database
        conn.commit()
        print("Records inserted........")

        # Closing the connection
        conn.close()

if __name__ == '__main__':
    cherrypy.quickstart(HelloWorld())