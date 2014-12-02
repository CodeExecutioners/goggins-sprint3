import webapp2
import datetime
import logging
from google.appengine.ext import ndb




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
		
#Alex's stuff			
class Resource(ndb.Model):
	type = ndb.StringProperty()
	title = ndb.StringProperty()
	linkOrAddress = ndb.StringProperty()
	desc = ndb.StringProperty()
	
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
			resource = self(type = type, title = title, linkOrAddress = linkOrAddress, desc = desc)
			resource.put()
			logging.debug('insertResource success')
		except:
			logging.error('insertResource failed')
	

	@classmethod
	def updateResourceByID(self, id, type, title, linkOrAddress, desc):
			logging.debug('updatingResource')
			
			try:
			
				if(id != 'None'):
					updated_resource = Resource.get_by_id(int(id))
					logging.debug(updated_resource)
				
					if(updated_resource != None):
						updated_resource.title =title
						updated_resource.type = type
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
						
	@classmethod	
	def deleteResourceByID(self, id):
			try:
			
				if(id != 'None'):
					delete_resource = Resource.get_by_id(int(id))
					delete_resource.key.delete()
					logging.debug('deleteResourceByID success')
			except:
				logging.error('deleteResourceByID failed')