import os
import urllib
import webapp2
import jinja2
import models

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)
	
class ResourcesPage(webapp2.RequestHandler):
   def get(self):
        #get all resources
		resources = models.Resource.getAllResources()
		
        #self.response.write('Hello world!')
		template_values ={'resources':resources}
		template = JINJA_ENVIRONMENT.get_template('templates/resources.html')
		self.response.write(template.render(template_values))

app = webapp2.WSGIApplication([('/resources', ResourcesPage)],
                              debug=True)