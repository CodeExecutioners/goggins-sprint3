import os
import urllib
import urllib2
import webapp2
import logging
import jinja2
import models
import json
from google.appengine.ext import ndb
from datetime import datetime
import sys

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)
	
class AdminResourcesPage(webapp2.RequestHandler):
	def get(self):
		logging.debug('post')
		#models.Resource.deleteAllResources()

		#get all resources
		resources = models.Resource.getAllResources()
		
        #self.response.write('Hello world!')
		template_values ={'resources':resources}
		template = JINJA_ENVIRONMENT.get_template('templates/adminResources.html')
		self.response.write(template.render(template_values))
		
	def post(self):
		logging.debug('post')
		
		if 'Delete' in self.request.POST:
			id = self.request.get("resID")
			models.Resource.deleteResourceByID(id)
		else:
			type = self.request.get("resType")
			title = self.request.get("resTitle")
			linkOrAddress = self.request.get("resAddress")
			desc = self.request.get("resDesc")
			id = self.request.get("resID")
			
			if id == "000":
				id = 'None'
			
			models.Resource.updateResourceByID(id, type, title, linkOrAddress, desc)
			#models.Lesson.insertLesson(id, city, date, location, cost)
	
		#title = self.request.get("linkName")
        #linkOrAddress = self.request.get("linkAddress")
        #desc = self.request.get("linkDesc")
		
		#models.Resource.updateResourceByID('link', 'None', title, linkOrAddress, desc)
		
	#def newResource(self):
	#	logging.debug('newResource')
	#	type = self.request.get("newResourceType")
	#	title = self.request.get("newResourceTitle")
	#	linkOrAddress = self.request.get("newResourceAddress")
	#	desc = self.request.get("newResourceDesc")
		
	#	models.Resource.updateResourceByID('None', type, title, linkOrAddress, desc)
	#	jsonstring = self.request.body
	#	self.response.out.write(jsonstring)
	#	jsonObject = json.loads(jsonstring)
	#	
	#	models.Resource.deleteAllResources()
	#	
	#	#update or insert
	#	for resource in jsonObject:
	#		type = resource['Type']
	#		title = resource['Title']
	#		linkOrAddress = resource['Link or Address']
	#		desc = resource['Desc']
	#		models.Resource.updateResourceByID(type, title, linkOrAddress, desc)
			#models.Lesson.insertLesson(id, city, date, location, cost)
			
		#for location in jsonObject:
		#	title = location['Title']
		#	link = location['Link']
		#	desc = location['Desc']
		#	address = location['Address']
		#	models.Location.updateLocationByID(title, link, desc, address);
			#models.Lesson.insertLesson(id, city, date, location, cost)
		
	

app = webapp2.WSGIApplication([('/adminResources', AdminResourcesPage)],
                              debug=True)