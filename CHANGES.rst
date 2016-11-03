Changes
=======


2.0 (03-11-2016)
----------------

- Django 1.10 support added
- Django < 1.8 support dropped
- HTMLCompressor now compresses inline javascript


1.1 (20-07-2014)
----------------

- Added ``csrf_token`` extension (from coffin)
- Added warning when request context processor is not enabled and
  ``{% django %}`` is used
- Filters and globals can now be imported from any module

1.1.7 (22-10-2015)
..................

- Fixes python 3 issue (use of basestring in register.py), issue #2

1.1.6 (22-10-2015)
..................

- Django 1.9 compatibility
- Drops support for Django 1.4
- Fixes ``csrf_token`` issue

1.1.5 (10-05-2015)
..................

- Bugfix: fixes context processors import on django 1.8+
- Enables loaders on django 1.8 (e.g. to ammend the order of the loaders)

1.1.4 (08-05-2015)
..................

- Bugfix: JINJA2_LOAD_FROM setting was not loaded correctly on django < 1.7
- Django 1.5 and 1.6 are no longer supported

1.1.3 (16-04-2015)
..................

- Compatibility with Django 1.8
- Backwards incompatible: djinga.env is no longer exposed as the jinja2
  environment

1.1.2 (15-08-2014)
..................

Bugfixes:

- extensions package import issues
- JINJA2_[DJ]J_EXTS handling:
   * an exception is raised if the value is not a list or tuple
   * file extensions tolerate leading dot
   * clarified documentation
- issues with Python 3

Documentation:

- added previously missing doc relative to jj_global and jj_filter decorators
  and JINJA2_FROM_MODULE setting value

1.1.1 (06-08-2014)
..................

- Compatibility with Django 1.4 to 1.7
- Compatibility with Python 2.6 to 3.4 (depending on django version)


1.0 (19-03-2014)
----------------

- Birth!
- Available extensions: HtmlCompress and static files (static, css, js)
- makemessages override from coffin
- automatic selection of template engine
