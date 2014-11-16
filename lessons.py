import os
import urllib
import urllib2
import webapp2
import jinja2
import models
import json
from google.appengine.ext import ndb
from datetime import datetime
import sys
import logging

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)
	
class LessonsPage(webapp2.RequestHandler):
	def get(self):
		#models.Lesson.deleteAllLessons()
		privateLessons = models.Lesson.getAllLessonsByType('Private')
		dropInlessons = models.Lesson.getAllLessonsByType('Drop-In')
		groupLessons = models.Lesson.getAllLessonsByType('Group')
		#get lesson by city
		template_values ={'privateLessons': privateLessons,'lessons':dropInlessons, 'groupLessons': groupLessons}
		template = JINJA_ENVIRONMENT.get_template('templates/lessons.html')
		self.response.write(template.render(template_values))
		
	
	def post(self):
		
		#get all the table data
		jsonstring = self.request.body
		self.response.out.write(jsonstring)
		jsonObject = json.loads(jsonstring)
		
		#update or insert
		for lesson in jsonObject:
			type = lesson['Type']
			city = lesson['City']
			date = lesson['Date']
			location = lesson['Location']
			cost = lesson['Cost']
			models.Lesson.updateLessonByID(type, city, date, location, cost)
			#models.Lesson.insertLesson(id, city, date, location, cost)
			
		
		#self.redirect('/lessons')	
		

app = webapp2.WSGIApplication([
			('/lessons', LessonsPage),
			],debug=True)