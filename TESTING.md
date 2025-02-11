# Testing: The Village Tap

## Table of Contents

* [Manual Testing](#manual-testing)
     * [Navigation](#navigation)
     * [Responsiveness](#responsiveness)
     * [Authentication](#authentication)
     * [CRUD Functionality](#crud-functionality)

* [Validator Testing](#validator-testing)
     * [PEP8](#pep8)
     * [W3C](#w3c)
     * [JSHint](#jshint)

* [Accessibility and Performance](#accessibility-and-performance)
     * [WAVE](#wave)
     * [Lighthouse](#lighthouse)

* [Bugs and Bug Fixes](#bugs-and-bug-fixes)


## Manual Testing


### Navigation

### Responsiveness

### Authentication

### CRUD Functionality


## Validator Testing

### PEP8

### W3C

### JSHint

The comments.js file has been passed through [JShint](https://jshint.com/) with one issue raised: "Functions declared within loops referencing an outer scoped variable may lead to confusing semantics. (bootstrap)"


## Accessibility and Performance

### WAVE

### Lighthouse


## Bugs and Bug Fixes

* 'The snug' forum page had no url path in the main urls.py file.

* Modify threads_page view so superuser can create and post threads from front-end without needing approval.

* Modify the Thread model so the slug field is filled out automatically

* Related article link display in thread.

* Restructure threads_page.html so logged out users can't see threads.

* Fix NameError by properly referncing and importing CATEGORY_CHOICES in article_list view.

* Fix the pathing issue in news/urls.py - wrong matching order

* 'Add New Article' link visible to non superusers - add an {% if %} template tag to base.html

* Edit thread form displays without clicking on 'edit thread' button - html and js code fix.

* Display related article URL as an actual clickable link under the thread.

* Redirect not previously imported in views.py.

* Add new decorator to create_article view to redirect non-superusers to login page.