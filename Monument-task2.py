import MySQLdb

##Please write a simple script in Python that goes over our
##user database and creates users on Intercom.

##
##DROP TABLE IF EXISTS `user`;
##CREATE TABLE `user` (
##  `id` int(11) NOT NULL AUTO_INCREMENT,
##  `name` text NOT NULL,
##  `email` varchar(120) NOT NULL
##  PRIMARY KEY (`id`),
##  UNIQUE KEY `email` (`email`)
##) ENGINE=InnoDB DEFAULT CHARSET=utf8;

def main():
    task2(cursor,sql)
    
#database_connection[0]=db, ""[1]=user, ""[2]=passwd, ""[3]=host
database_connection=["user.db"]
##select all rows from user table
sql="SELECT * FROM user"

##task 2 -- takes arguments for a database connection and a sql command and calls executes method on cursor
    ##Specifically -takes data from database connection and creates users and appends into a list
def task2(database_connection,sql):
    
    #if database_connection[] contains 4 arguments for connection method
    if(len(database_connection)==4):
        db=MySQLdb.connect(db=database_connection[0],user=database_connection[1],passwd=database_connection[2],host=database_connection[3])
    else:
        ##connect to Monument Labs 'user' MySQL database
        db=MySQLdb.connect(db=database_connection[0])
        
    try:
        #prepare cursor object
        cursor=db.cursor()
    except:
        print("Error preparing cursor object: invalid connection")

    
    #list which holds all user objects
    users_list=[]
    
    #extracting data from user database and adding it to the users_list
    try:
        #execute SQL, sql, command
        cursor.execute(sql)
        users = cursor.fetchall()
        #create user objects for each Monument_user, add to users_list
        for user in users:
            id_code=user[0]
            name=user[1]
            email=user[2]
            userItem=user(id_code, name, email)
            users_list.append(userItem)
            
            print("id= {}, name= {}, email= {}".format(id_code,name,email))
    except:
        print("Error executing sql command: Unable to fetch data")

    db.close()
    createIntercomUser(users_list)
    
##take users_list as parameter and create users of intercom for each element 
def createIntercomUser(users_list):
    #create instance of IntercomClient
    intercom=IntercomClient("<Your-Access-Token>")
    for uItem in users_list:
        #creates user object of Intercom
        intercom.users.create(user_id=uItem.get_id(),email=uItem.get_email(),name=uItem.get_name())
    
# user object, holds a id, a name, and an email
class user(object):
    def __init__(self,id_code,name,email):
        'constructor'
        self.id=id_code
        self.name=name
        self.email=email

    def get_id(self):
        'returns id of user'
        return self.id
    
    def get_name(self):
        'returns name of user'
        return self.name
    
    def get_email(self):
        'returns email of user'
        return self.email

##code taken from itercoms developer page (https://developers.intercom.com/v2.0/docs/creating-users)
class IntercomClient(Intercom):
    def __init__(self,your_token):
        'contructor'
        Intercom.__init__(self)
        intercom = Client.new(token= your_token)

if __name__ == "__main__":
   main()
  
