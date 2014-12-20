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
#import jinja2
import webapp2
import hmac
import hashlib
import re
import cgi

form="""<h1>Home Page:</h1>
		<a href="/login">Login</a>
		<a href="/register">Register</a>"""

class MainHandler(webapp2.RequestHandler):
	def get(self):
		self.redirect("/home")

class HomeHandler(webapp2.RequestHandler):
	def get(self):
		self.response.out.write(form)

class LoginHandler(webapp2.RequestHandler):
	def get(self):
		self.response.out.write("""Login: Hello world! <a href="/home">Home</a>""")

class RegisterHandler(webapp2.RequestHandler):
	def get(self):
		self.response.out.write("""Register: Hello world! <a href="/home">Home</a>""")


app = webapp2.WSGIApplication([('/', MainHandler), ('/home', HomeHandler), ('/login', LoginHandler), ('/register', RegisterHandler)], debug=True)


#following three functions use regular expressions
USER_RE = re.compile(r"^[a-zA-Z0-9_-]{3,20}$")
def verifyUsername(username):
	return USER_RE.match(username)
	
PASSWORD_RE = re.compile(r"^.{3,20}$")
def verifyPassword(password):
	return PASSWORD_RE.match(password)
	
EMAIL_RE = re.compile(r"^[\S]+@[\S]+\.[\S]+$")
def verifyEmail(email):
	return EMAIL_RE.match(email)
