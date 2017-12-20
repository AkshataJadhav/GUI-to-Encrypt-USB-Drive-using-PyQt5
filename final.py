from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QCheckBox, QGridLayout, QGroupBox,QComboBox,QLabel,QLineEdit,QMessageBox,QProgressBar,
        QMenu, QPushButton, QRadioButton, QVBoxLayout,QHBoxLayout, QWidget)


class Window(QWidget):
	def __init__(self):
		super(Window, self).__init__()

		grid = QGridLayout()
		grid.addWidget(self.Encrypt(), 0, 0)
		grid.addWidget(self.Add_delete(), 1, 0)
	      
		self.setLayout(grid)

		self.setWindowTitle("GUI")
		self.resize(480, 320)

	

	

	def Encrypt(self):
		groupBox = QGroupBox("Encrypt USB Drive")
		groupBox.setCheckable(True)
		groupBox.setChecked(True)
		comboBox = QComboBox()
		comboBox.addItem(' Select your drive')
		comboBox.addItem('Windows')
		comboBox.addItem('cde')
		comboBox.addItem('Plastique')
		comboBox.addItem('Cleanlooks')
		comboBox.addItem('windowsvista')
		comboBox.setMinimumWidth(300)
		comboBox.setStyleSheet('''*    
		QComboBox QAbstractItemView 
			{
		 	min-width: 100px;
		   	}
		''')
		comboBox.move(150, 50)
		
		self.btn=QPushButton("Format",self)
		#self.btn.resize(100,50)
		self.btn.clicked.connect(self.format)
	
		
		self.label=QLabel()
		self.label.setText("Enter your Password")
		#self.label.move(150,150)
		#self.label.resize(200,30)

		self.textbox=QLineEdit()
		self.textbox.setEnabled(False)
		self.textbox.setEchoMode(QLineEdit.Password)
		#self.textbox.move(150,180)
		self.textbox.setMaxLength(10)
		#self.textbox.resize(280,40)
		
		self.label1=QLabel()
		#self.label1.move(150,240)
		self.label1.setText("Confirm Your Password")
		#self.label1.resize(200,30)

		self.textbox1=QLineEdit()
		self.textbox1.setEchoMode(QLineEdit.Password)
		self.textbox1.setEnabled(False)
		#self.textbox1.move(150,280)
		self.textbox1.setMaxLength(10)
		#self.textbox1.resize(280,40)

		self.btn1=QPushButton("Finish",self)
		#self.btn.resize(100,50)
		self.btn1.clicked.connect(self.Finish)
		

		vbox = QVBoxLayout()
		vbox.addWidget(comboBox)
		vbox.addWidget(self.btn)
		vbox.addWidget(self.label)
		vbox.addWidget(self.textbox)
		vbox.addWidget(self.label1)
		vbox.addWidget(self.textbox1)
		vbox.addWidget(self.btn1)
		vbox.addStretch(1)
		groupBox.setLayout(vbox)

		return groupBox

	
	def Add_delete(self):
		self.groupBox = QGroupBox("Add or Delete Keys")
		self.groupBox.setCheckable(True)
		self.groupBox.setChecked(False)
		
		
		btn=QPushButton("Add new key ")
		

		btn1=QPushButton("Delete Existing key")

		vbox = QVBoxLayout()
		vbox.addWidget(btn)
		vbox.addWidget(btn1)
		
		vbox.addStretch(1)
		self.groupBox.setLayout(vbox)

		return self.groupBox

	




	def format(self):
		choices=QMessageBox.question(self,'Message',"Do you want to format",QMessageBox.Yes | QMessageBox.No,QMessageBox.No)
		self.complete=0
		
		if choices==QMessageBox.Yes:
			self.progressLabel = QLabel('Progress Bar:', self)
		
			#self.window=QVBoxLayout(self)
			#self.window.addWidget(self.hboxLayoutG)
			#self.setLayout(self.window)

			# Creating a progress bar and setting the value limits
			self.progressBar = QProgressBar(self)
			self.progressBar.setMaximum(100)
			self.progressBar.setMinimum(0)

			self.btn=QPushButton("Cancel",self)
			#self.btn.move(50,50)
			

			
			# Creating a Horizontal Layout to add all the widgets
			#self.hboxLayoutG=QGroupBox()
			self.hboxLayout = QHBoxLayout(self)

			# Adding the widgets
			self.hboxLayout.addWidget(self.progressLabel)
			self.hboxLayout.addWidget(self.progressBar)
			self.hboxLayout.addWidget(self.btn)
			

			# Setting the hBoxLayout as the main layout
			self.widget=QWidget()
			self.widget.setLayout(self.hboxLayout)
			self.widget.setWindowTitle('Dialog with Progressbar')
			self.widget.setGeometry(50,50,500,100)
			self.widget.show()
		
			connect=0
			while connect<100:
				connect+=0.001
				#time.sleep(0.1)				
				self.progressBar.setValue(connect)
			
			self.widget.close()
			QMessageBox.information(self,'Message',"Drive is formatted.Now you can set password",QMessageBox.Ok) 
			self.textbox.setEnabled(True)
			self.textbox1.setEnabled(True)

	def Finish(self):
		choice=QMessageBox.information(self,'Message',"Drive is encrypted.Click 'No' to end .Click 'Yes'to add new key",QMessageBox.Yes|QMessageBox.No,QMessageBox.No)
		if choice==QMessageBox.Yes:
			self.groupBox.setChecked(True)
		else:	
			sys.exit()	
		
			

	


if __name__ == '__main__':

    import sys

    app = QApplication(sys.argv)
    clock = Window()
    clock.show()
sys.exit(app.exec_())
