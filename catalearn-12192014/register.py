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


import os
import jinja2
import webapp2
import hashlib
import hmac
import random
import string
import cgi
from google.appengine.ext import db

SECRET = "I AM A SECRET"

template_dir = os.path.join(os.path.dirname(__file__), 'static/templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir),
																autoescape = True)

class Handler(webapp2.RequestHandler):
	def write(self, *a, **kw):
		self.response.out.write(*a, **kw)
	
	def render_str(self, template, **params):
		t = jinja_env.get_template(template)
		return t.render(params)
		
	def render(self, template, **kw):
		self.write(self.render_str(template, **kw))

class RegisterHandler(Handler):
	def get(self):
		self.render('register.html')

app = webapp2.WSGIApplication([('/register', RegisterHandler)], debug=True)

def hash_str(s):
    return hmac.new(SECRET, s).hexdigest()

def make_secure_val(s):
    return "%s|%s" % (s, hash_str(s))
	
def check_secure_val(h):
	temp = h.split("|")[0]
	if make_secure_val(temp) == h:
		return temp

def make_pw_hash(name, pw, salt = None):
	h = hashlib.sha256(name + pw + salt).hexdigest()
	return '%s|%s' % (h, salt)
	
def make_pw_hash(name, pw):
	salt = make_salt()
	return hashlib.sha256(name + pw + salt).hexdigest() + "," + salt	
	
def valid_pw(name, pw, h):
	salt = h.split('|')[1]
	return h == make_pw_hash(name, pw, salt)
