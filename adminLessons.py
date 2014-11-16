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
import webapp2

from webapp2_extras import sessions
JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)
	
class AdminLessonsPage(webapp2.RequestHandler):
	def dispatch(self):
		# Get a session store for this request.
		self.session_store = sessions.get_store(request=self.request)
		try:
		# Dispatch the request.
			webapp2.RequestHandler.dispatch(self)
		finally:
			# Save all sessions.
			self.session_store.save_sessions(self.response)
	def get(self):
		#models.Lesson.deleteAllLessons()
		initiated = self.session.get('initiated')
		x='true'
		if initiated != x:
			self.redirect('/login')
		dropInlessons = models.Lesson.getAllLessonsByType('Drop')
		groupLessons = models.Lesson.getAllLessonsByType('Group')
		#get lesson by city
		template_values ={'lessons':dropInlessons, 'groupLessons': groupLessons}
		template = JINJA_ENVIRONMENT.get_template('templates/adminLessons.html')
		self.response.write(template.render(template_values))
		
	
	def post(self):
		#shouldn't really do this
		
		#get all the table data
		jsonstring = self.request.body
		self.response.out.write(jsonstring)
		jsonObject = json.loads(jsonstring)
		
		#update or insert
		for lesson in jsonObject:
			models.Lesson.deleteAllLessons()
			type = lesson['Type']
			city = lesson['City']
			date = lesson['Date']
			location = lesson['Location']
			cost = lesson['Cost']
			models.Lesson.updateLessonByID(type, city, date, location, cost)
			#models.Lesson.insertLesson(id, city, date, location, cost)
			
		
		#self.redirect('/lessons')	
	@webapp2.cached_property
	def session(self):
		# Returns a session using the default cookie key.
		return self.session_store.get_session()

config = {}
config['webapp2_extras.sessions'] = {
    'secret_key': 'my-super-secret-key',
}		
app = webapp2.WSGIApplication([
		('/adminLessons', AdminLessonsPage),
		],config = config, debug=True)