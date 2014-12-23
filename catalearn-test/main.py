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
import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.redirect("/home")

class HomeHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('Home: Hello world!')

class LoginHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('Login: Hello world!')

class RegisterHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('Register: Hello world!')



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
