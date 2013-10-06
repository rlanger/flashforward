from flask import Flask, Response, request, session, g, redirect, url_for, \
	abort, render_template, flash, jsonify

from flashforward import flashforward

TIME_STORE_FORMAT = '%Y-%m-%d %H:%M'
TIME_DISPLAY_FORMAT = '%d %b, %Y %H:%M'

PAGE_SEQUENCE = ["welcome.html", "demographics.html", "flash2.html", "questionaire1.html", "instructions1.html", "questionaire2.html", "instructions2.html", "post_trial.html", "freeplay.html"]

@flashforward.route('/')
def index():
	session['pageNum'] = 0
	print ("PAGE NUMBER = %d" % session['pageNum'])
	return render_template('welcome.html')
	
@flashforward.route('/ff')
def ff():
	session['pageNum'] = 2
	print ("PAGE NUMBER = %d" % session['pageNum'])
	return render_template(PAGE_SEQUENCE[2])
	
@flashforward.route('/next')
def next():
	if 'pageNum' in session:
		if session['pageNum'] < (len(PAGE_SEQUENCE)-1):
			session['pageNum'] += 1
			print ("PAGE NUMBER = %d" % session['pageNum'])
			pageNum = session['pageNum']
			nextpage = PAGE_SEQUENCE[pageNum]
			return render_template(nextpage)
		else:
			print("ERROR: out of bounds")
			return render_template(PAGE_SEQUENCE[-1])
	else:
		print("ERROR: PageNum not set")

@flashforward.route('/back')
def back():
	session['pageNum'] -= 1
	print ("PAGE NUMBER = %d" % session['pageNum'])
	pageNum = session['pageNum']
	prevpage = PAGE_SEQUENCE[pageNum]
	return render_template(prevpage)