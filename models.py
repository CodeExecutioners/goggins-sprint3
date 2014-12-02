import webapp2
import datetime
import logging
import math
from google.appengine.ext import ndb
from google.appengine.ext import db

class LessonTest(ndb.Model):
	"""Models an individual lesson"""
	#should really use date time property
	type = ndb.StringProperty()
	city = ndb.StringProperty()
	date = ndb.StringProperty()
	time = ndb.StringProperty()
	location = ndb.StringProperty()
	cost = ndb.StringProperty()
	details = ndb.TextProperty()
	
	@classmethod
	def getAllLessons(self):
		try:
			return self.query()
		except:
			logging.error('getAllLessons failed')
	
	@classmethod
	def getAllLessonsByType(self, type):
		#Group, DropIn
		try:
			return self.query(self.type==type)
		except:
			logging.error('getAllLessonsByType failed')
	
	
	
	@classmethod
	def getNLessons(self, n):
		try:
			return self.query().fetch(n)
		except:
			logging.error('getNLesssons failed')
	
	#insert
	@classmethod
	def insertLesson(self, type, city, date, time, location, cost, details):
			logging.debug('insertLesson start')
			detailsText = db.Text(details)
			try:
				lesson = self(type = type, city = city, date = date, time = time, location = location, cost = cost, details = detailsText)
				lesson.put()
				logging.debug('insertLesson success')
			except:
				logging.error('insertLesson failed')
		
	
	#insert
	@classmethod
	def updateLessonByID(self, id,type, city, date, time,  location, cost, details):
			
			
			try:
			
				if(id != 'None'):
					#lesson_key = ndb.Key(self,id)
					updated_lesson = LessonTest.get_by_id(int(id))
					logging.debug(updated_lesson)
				
					if(updated_lesson != None):
					
						logging.debug("Updated city" + updated_lesson.city)
						updated_lesson.city =city
						updated_lesson.type = type
						updated_lesson.date = date
						updated_lesson.time = time
						updated_lesson.location = location
						updated_lesson.cost = cost
						detailsText = db.Text(details)
						updated_lesson.details = detailsText
						updated_lesson.put()
						logging.debug('updateLesson success')
				else:
					logging.debug('Inserting new record')
					self.insertLesson(type, city, date, time,  location, cost, details)
			except:
				logging.error('updateLesson failed')
		

	@classmethod
	def getLessonByID(self, id):
			try:
			
				if(id != 'None'):
					#lesson_key = ndb.Key(self,id)
					lesson = LessonTest.get_by_id(int(id))
					logging.debug(lesson)
				
					if(lesson != None):
						return lesson
				else:
					logging.debug('Get lesson by id failed')
					
			except:
				logging.error('Get lesson by id failed ')
		

	
	#delete
	@classmethod
	def deleteAllLessons(self):
		try:
			lesson_keys = self.query().fetch(keys_only=True)
			ndb.delete_multi(lesson_keys)
			logging.debug('deleteAllLessons success')
		except:
			logging.error('deleteAllLessons failed')
		
	#insert
	@classmethod
	def deleteLessonByID(self, id):
			try:
			
				if(id != 'None'):
					delete_lesson = LessonTest.get_by_id(int(id))
					delete_lesson.key.delete()
					logging.debug('deleteLessonByID success')
			except:
				logging.error('deleteLessonByID failed')
		

		
	#filtering
	@classmethod
	def getLessonsByCity(self, city):
		logging.debug('getLessonsByCity started')
		try:
			return self.query(self.city == city);
		except:
			logging.error('getLessonsByCity failed')
			



class Editor(ndb.Model):
	#perhaps needs an CK Editor ID
	editorID = ndb.StringProperty
	html = ndb.StringProperty()

	@classmethod
	def insertEditor(self, html):
			logging.debug('insertEditor start')
			try:
				editor = self(html = html)
				editor.put()
				logging.debug('insertEditor success')
			except:
				logging.error('insertEditor failed')
				
	@classmethod
	def getAllEditors(self):
		try:
			return self.query()
		except:
			logging.error('getAllEditors failed')
			
	@classmethod
	def getEditorByID(self):
		try:
			return self.query()
		except:
			logging.error('getAllEditors failed')


class Lesson(ndb.Model):
	"""Models an individual lesson"""
	type = ndb.StringProperty()
	city = ndb.StringProperty()
	date = ndb.StringProperty()
	time = ndb.StringProperty();
	location = ndb.StringProperty()
	cost = ndb.StringProperty()
	
	@classmethod
	def getAllLessons(self):
		try:
			return self.query()
		except:
			logging.error('getAllLessons failed')
	
	@classmethod
	def getAllLessonsByType(self, type):
		#Group, DropIn
		try:
			return self.query(self.type==type)
		except:
			logging.error('getAllLessonsByType failed')
	
	
	
	@classmethod
	def getNLessons(self, n):
		try:
			return self.query().fetch(n)
		except:
			logging.error('getNLesssons failed')
	
	#insert
	@classmethod
	def insertLesson(self, type, city, date, time, location, cost):
			logging.debug('insertLesson start')
			try:
				lesson = self(type = type, city = city, date = date, time = time, location = location, cost = cost)
				lesson.put()
				logging.debug('insertLesson success')
			except:
				logging.error('insertLesson failed')
		
	
	#insert
	@classmethod
	def updateLessonByID(self, id, type, city, date, time, location, cost):
			
			
			try:
			
				if(id != 'None'):
					#lesson_key = ndb.Key(self,id)
					updated_lesson = Lesson.get_by_id(int(id))
					logging.debug(updated_lesson)
				
					if(updated_lesson != None):
						logging.debug("Updated city" + updated_lesson.city)
						updated_lesson.city =city
						updated_lesson.type = type
						updated_lesson.date = date
						updated_lesson.time = time
						updated_lesson.location = location
						updated_lesson.cost = cost
						updated_lesson.put()
						logging.debug('updateLesson success')
				else:
					logging.debug('Inserting new record')
					self.insertLesson(type, city, date, time, location, cost)
			except:
				logging.error('updateLesson failed')
		

	
	#delete
	@classmethod
	def deleteAllLessons(self):
		try:
			lesson_keys = self.query().fetch(keys_only=True)
			ndb.delete_multi(lesson_keys)
			logging.debug('deleteAllLessons success')
		except:
			logging.error('deleteAllLessons failed')
		
	#insert
	@classmethod
	def deleteLessonByID(self, id):
			try:
			
				if(id != 'None'):
					delete_lesson = Lesson.get_by_id(int(id))
					delete_lesson.key.delete()
					logging.debug('deleteLessonByID success')
			except:
				logging.error('deleteLessonByID failed')
		

		
	#filtering
	@classmethod
	def getLessonsByCity(self, city):
		logging.debug('getLessonsByCity started')
		try:
			return self.query(self.city == city);
		except:
			logging.error('getLessonsByCity failed')
			
			
class Email(ndb.Model):
	"""Models an individual email"""
	firstname = ndb.StringProperty()
	lastname = ndb.StringProperty()
	phone = ndb.StringProperty()
	email = ndb.StringProperty()
	message = ndb.StringProperty()

class Users(ndb.Model):
	"""Models an individual user"""
	username = ndb.StringProperty()
	password = ndb.StringProperty()
	email = ndb.StringProperty()
	
	@classmethod
	def getAllUsers(self):
		try:
			return self.query()
		except:
			logging.error('getAllUsers failed')

	#insert
	@classmethod
	def insertUser(self, username, password, email):
		
		try:
			user = self(username=username, password = password, email=email)
			user.put()
			logging.debug('insertUser success')
		except:
			logging.error('insertUser failed')
		
	#delete
	@classmethod
	def deleteAllUsers(self):
		try:
			user_keys = self.query().fetch(keys_only=True)
			ndb.delete_multi(user_keys)
		except:
			logging.error('deleteAllUsers failed')
	
		
	#filtering
	@classmethod
	def getUserByUsername(self, username):
		try:
			return self.query(self.username == username);
		except:
			logging.error('getUserByUsername failed')
	
	#return true if user is found, false otherwise
	@classmethod
	def loginProcess(self, username, password):
		loginSuccess = False;
		try:
			loginSuccess = (self.query(self.username == username and self.password==password).count()==1)
			logging.debug('loginProcess success:' + loginSucess)
			return loginSuccess
		except:
			logging.error('loginProcess failed')
			return loginSuccess
		

class ResourceText(ndb.Model):
	type = ndb.StringProperty()
	title = ndb.StringProperty()
	linkOrAddress = ndb.StringProperty()
	desc = ndb.TextProperty()
	
	
	@classmethod
	def getAllResources(self):
		try:
			return self.query()
		except:
			logging.error('getAllResource failed')
			
	def getAllResourcesByType(self, type):
		try:
			return self.query(self.type==type)
		except:
			logging.error('getAllLessonsByType failed')
	
	@classmethod
	def getNResources(self, n):
		try:
			return self.query().fetch(n)
		except:
			logging.error('getNResource failed')
	
	#insert
	@classmethod
	def insertResource(self, type, title, linkOrAddress, desc):
		try:
			
			text = db.Text(desc)
			logging.debug("made text object")
			resource = self(type = type, title = title, linkOrAddress = linkOrAddress, desc = text)
			resource.put()
			logging.debug('insertResource success')
		except:
			logging.error('insertResource failed')
	
	
	@classmethod
	def getNChildren(self, desc):
		nchildren = (math.floor((len(desc)) / 500.0))
		return nchildren
	
	#insert
	@classmethod
	def updateResourceDescByID(self, id, desc):
			
			
			try:
				if(id != 'None'):
					logging.debug('updateResourceDescByID started')
					logging.debug(id)
					logging.debug(int(id))
					logging.debug(desc)
					updated_resource = ResourceText.get_by_id(int(id))
					
					if(updated_resource != None):
						logging.debug(updated_resource)
						
						
						#logging.debug("Desc size: " +str(len(desc)))
						#logging.debug("N children: " + str(nchildren))
						logging.debug('Updating record')
						updated_resource.desc = db.Text(desc)
						updated_resource.put()
						logging.debug('updateResourceDescByID success')
					
			except:
				logging.error('updateResourceDescByID failed')
		

	
	

	#insert
	@classmethod
	def updateResourceByID(self, type, title, linkOrAddress, desc):
			try:
				resource_key = ndb.Key(self, (type+title))
				logging.debug(resource_key)
				updated_resource = resource_key.get()
				if(updated_resource != None):
					logging.debug('Updating record')
					updated_resource.type = type
					updated_resource.title = title
					updated_resource.linkOrAddress = linkOrAddress
					updated_resource.desc = desc
					updated_resource.put()
					logging.debug('updateResource success')
				else:
					logging.debug('Inserting new record')
					self.insertResource(type, title, linkOrAddress, desc)
			except:
				logging.error('updateResource failed')	
		
	#delete
	@classmethod
	def deleteAllResources(self):
		try:
			resource_keys = self.query().fetch(keys_only=True)
			ndb.delete_multi(resource_keys)
			logging.debug('deleteAllResources success')
		except:
			logging.error('deleteAllResources failed')
						
			
			