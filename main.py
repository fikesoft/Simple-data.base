import wx 
from view import finder
import psycopg2

app = wx.App()

# Making the variable to login   
HOST = "localhost"
DATA = "test0"
PORT = "2401" 
USER = "postgres"
PASS = "floare123"



class finder2(finder):
	
	def connect(self):
		# Making the connection with the database 
		connect = psycopg2.connect(
			host=HOST,
			database=DATA,
			port=PORT,
			user=USER,
			password=PASS)
		
		return connect
	
	def execute(self, query):
		

		# Establish the connection 
		conn = self.connect()
		
		#Connecting the cursor 
		cursor = conn.cursor()
		
		#Executing the statement
		cursor.execute(query)
		
		#Showing the result 
		results = cursor.fetchall()
		
		for row in results:
			value=row
			
		#Closing conection 
		cursor.close()
		conn.close()
		
		return value
		
		
		
		    
	def find(self, event):
		
		LIST_OF_CTRL=[self.m_textCtrl3,self.m_textCtrl4,self.m_textCtrl5,\
		self.m_textCtrl6,self.m_textCtrl7,self.m_textCtrl8,self.m_textCtrl9,\
		self.m_textCtrl10]
		
		Name = self.m_textCtrl1.GetValue().strip()

		
		Sur = self.m_textCtrl2.GetValue().strip()

		
		query = "SELECT * FROM findme WHERE Name='" + Name + "' AND Surname='" + Sur + "'"
		
		#Try except block to avoid issues 
		try:
			
			#Executing the query to find the name and surname 
			values = self.execute(query)
			
			#Doble iteration 
			for i,x in zip(range(len(values)),LIST_OF_CTRL):
				x.SetValue(values[i])
		
		except:
			wx.MessageBox("OOPPSSSS.... SOME ISSUES WITH THE DATABASE ", 'ERROR',\
		wx.OK | wx.ICON_INFORMATION)

frame = finder2(None)
frame.Show()
app.MainLoop()
