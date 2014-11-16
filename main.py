#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import os
import urllib
import webapp2
import jinja2
import models

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)
	
class MainHandler(webapp2.RequestHandler):
    def get(self):
        #self.response.write('Hello world!')
		template_values ={}
		path = self.request.path
		template = JINJA_ENVIRONMENT.get_template('templates/index.html')
		self.response.write(template.render(template_values))

class SubmitForm(webapp2.RequestHandler):
	def post(self):
		firstname = self.request.get('firstname')
		lastname = self.request.get('lastname')
		email = self.request.get('email')
		phone = self.request.get('phone')
		message = self.request.get('message')
		emailItem = models.Email(firstname = firstname,lastname = lastname,	email = email,phone = phone,message = message)
		emailItem.put()
		self.redirect('/')

		
app = webapp2.WSGIApplication([
    ('/', MainHandler),
	('/submit', SubmitForm),

], debug=True)
