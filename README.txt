djinga
======

(c) 2014 Thomas Khyn

Unobtrusive jinja2 integration in Django

Freely inspired from django-jinja and django-jinja2


Usage
-----

- Install djinga using the method of your choice
- Add 'djinga' to your INSTALLED_APPS
- Change the TEMPLATE_LOADERS settings to::

	TEMPLATE_LOADERS = (
	    'djinga.loaders.FileSystemLoader',
	    'djinga.loaders.AppLoader',
	)

- Add the relevant settings for jinja2


How it works
------------

By default, a template will be rendered using Django's built-in template engine
if it has a .html, .htm, .djhtml or .djhtm file extension. If it has a .jjhtml
or .jjhtm file extension, it will be rendered by Jinja2, using the setting
values provided in django's setting module.


Settings
--------

JINJA2_DJ_EXTS
	The file extensions for templates that should be rendered with Django's
	internal template engine. Defaults to :code:`('html', 'htm', 'jjhtml',
	'jjhtm')`

JINJA2_JJ_EXTS
	The file extensions for templates that should be rendered with Jinja2.
	Defaults to :code:`('jjhtml', 'jjhtm')`

JINJA2_CONDITION
	A function taking as sole argument the path of the template file and
	returning True if the file should be rendered with Jinja2. Defaults to a
	function returning True if the extension is in JINJA2_JJ_EXTS

JINJA2_EXTENSIONS
	The extensions to be loaded by jinja2. Some extensions are shipped with
	djinga under :code:`djinga.ext.*`

JINJA2_ENV_ARGS
	The jinja2 environment's constructor keyword arguments as a dictionary.

JINJA2_GLOBALS
	The jinja2 globals as a dictionary.

JINJA2_FILTERS
	The jinja2 filters as a dictionary.


Built-in Jinja2 extensions
--------------------------

Djinga comes with several Jinja2 extensions

djinga.ext.static
	Provides a :code:`{% static 'path' %}` tag to refer to Django's staticfiles
	directory

djinga.ext.css
	Provides a :code:`{% css 'rel/path/to/file.css' %}` tag that generates a
	HTML link element refering to the css file located at a relative path in
	a css directory. The css directory's path can be defined relatively to
	Django's staticfiles directory through the setting JINJA2_STATIC_CSS

djinga.ext.js
	Same as djinga.ext.css but generates a HTML script element refering to a
	javascript file. The js directory's relative path can be set through the
	setting JINJA2_STATIC_JS


Other Jinja2 extensions
-----------------------

djinga.ext.htmlcompress.HTMLCompress / SelectiveHTMLCompress
	(c) 2011 Armin Ronacher.
	Eliminates useless whitespace at template compilation time without extra
	overhead.
