import os
import urllib
import webapp2
import jinja2
import models
import logging
import json

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)
	
class ResourcesPage(webapp2.RequestHandler):
	def get(self):
		type = 'link'
		title = 'testTitle2'
		linkOrAddress = 'testLinkOrAddress'
		desc = 'testDescText'
		#models.ResourceText.deleteAllResources()
		#models.ResourceText.insertResource(type, title, linkOrAddress, desc)
		resources = models.ResourceText.getAllResources()
		template_values ={'resources': resources}
		template = JINJA_ENVIRONMENT.get_template('templates/resources.html')
		self.response.write(template.render(template_values))

	def post(self):
		logging.debug('post start')
		#models.Resources.insertEditor(data)
		#get the json and post
		#get all the table data
		
		jsonstring = self.request.body
		logging.debug(jsonstring)
		self.response.out.write(jsonstring)
		jsonResources = json.loads(jsonstring)
		logging.debug(jsonResources)
		for resource in jsonResources:
			id = resource['ID']
			desc = resource['DATA']
			models.ResourceText.updateResourceDescByID(id, desc)
		logging.debug('post end')
	
app = webapp2.WSGIApplication([('/resources', ResourcesPage)],
                              debug=True)