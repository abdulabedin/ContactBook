import sqlite3
conn = sqlite3.connect("contact.db")
c = conn.cursor()
c.execute("CREATE TABLE IF NOT EXISTS info(firstname TEXT,lastname TEXT,phonenumber INTEGER, email TEXT )")
conn.commit
class Contact:
  def __init__(self):
    self.firstname = ""
    self.lastname = ""
    self.number = 0
    self.email = ""
  def add(self):
    print ("\n")
    self.firstname = input("Enter first name:")
    self.lastname = input("Enter last name:")
    self.number = int(input("Enter phone number:"))
    self.email = input ("Enter email:")
    c.execute ('INSERT INTO info VALUES(?,?,?,?)',(self.firstname,self.lastname,self.number,self.email))
    conn.commit ()
    print("\n")
    print ("Contact Added")
    print("\n")
  def retrive(self):
    print("\n")
    pick = int(input("Enter 1 to print all contacts. Enter 2 to find a specific contact: "))
    print ("\n")
    if pick ==1:
      c.execute ('SELECT * FROM info')
      data = c.fetchall()
      for i in range (len(data)):
        print ("First Name:",data[i][0])
        print ("Last Name:",data[i][1])
        print ("Phone Number Name:",data[i][2])
        print ("Email:",data[i][3])
        print("\n")
    elif pick ==2:
      choose = input('Enter the first name of the contact your trying to find:')
      data =  ('SELECT * FROM info where firstname = ?')
      c.execute(data,(choose,))
      data = c.fetchall()
      print ("First Name:",data[0][0])
      print ("Last Name:",data[0][1])
      print ("Phone Number:",data[0][2])
      print ("Email:",data[0][3])
      print("\n")
  def delete(self):
    print()
    pick = int(input("Enter 1 to delete all contacts. Enter 2 to delete a specific contact: "))
    if pick == 1:
      deltes = 'DELETE FROM info'
      c.execute (deltes)
      conn.commit ()
    elif pick==2:
      option = input("Enter the first name of the contact you want to delete")
      deltes = 'DELETE FROM info WHERE firstname = ? '
      c.execute (deltes,(option,))
      conn.commit ()
    print ("Contact Deleted")
    print("\n")
  def update (self):
      print()
      new = input("Enter the first name of the contact you want to update")
      self.firstname = input("Enter first name:")
      self.lastname = input("Enter last name:")
      self.number = int(input("Enter phone number:"))
      self.email = input ("Enter email:")
     # updates = 'UPDATE info SET firstname = ?, lastname = ? where firstname = ?' 
      updates = 'UPDATE info SET firstname = ?, lastname = ?,phonenumber = ?, email = ? where firstname = ?'
      c.execute (updates,(self.firstname,self.lastname,self.number,self.email,new))
      conn.commit ()
      print("\n")
      print ("Contact Updated")
      print("\n")