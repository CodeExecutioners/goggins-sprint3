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

from google.appengine.api import mail

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)
	
class Login2Handler(webapp2.RequestHandler):
	def get(self):
		#insert a user
		#models.Users.insertUser('testUsername', 'testPassword', 'testEmail@dancingoggin.appspot.com')
		template_values ={}
		path = self.request.path
		template = JINJA_ENVIRONMENT.get_template('templates/contact.html')
		self.response.write(template.render(template_values))
	def post(self):
		user_address = self.request.get("inputEmail")
		me = "; fisher.robert26@gmail.com"
		user_address=user_address+me
		confirmation_url = "www.google.com"
		sender_address = "<fisher.robert26@gmail.com>"
		subject = self.request.get("inputSubject")
		body = self.request.get("inputMessage")
		mail.send_mail(sender_address, user_address, subject, body)
		self.redirect('/succes_message')
app = webapp2.WSGIApplication([
	('/contact_mail', Login2Handler),
		

], debug=True)