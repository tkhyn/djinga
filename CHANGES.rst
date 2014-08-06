Changes
=======


1.1.1 (2014-08-06)
------------------

- Compatibility with Django 1.4 to 1.7
- Compatibility with Python 2.6 to 3.4 (depending on django version)


1.1 (2014-07-20)
----------------

- Added ``csrf_token`` extension (from coffin)
- Added warning when request context processor is not enabled and
  ``{% django %}`` is used
- Filters and globals can now be imported from any module


1.0 (2014-03-19)
----------------

- Birth!
- Available extensions: HtmlCompress and static files (static, css, js)
- makemessages override from coffin
- automatic selection of template engine
