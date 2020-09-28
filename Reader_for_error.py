Error:
Odoo Server Error

Traceback (most recent call last):
  File "/usr/lib/python3.7/site-packages/odoo/http.py", line 624, in _handle_exception
    return super(JsonRequest, self)._handle_exception(exception)
  File "/usr/lib/python3.7/site-packages/odoo/http.py", line 310, in _handle_exception
    raise pycompat.reraise(type(exception), exception, sys.exc_info()[2])
  File "/usr/lib/python3.7/site-packages/odoo/tools/pycompat.py", line 14, in reraise
    raise value
  File "/usr/lib/python3.7/site-packages/odoo/http.py", line 669, in dispatch
    result = self._call_function(**self.params)
  File "/usr/lib/python3.7/site-packages/odoo/http.py", line 350, in _call_function
    return checked_call(self.db, *args, **kwargs)
  File "/usr/lib/python3.7/site-packages/odoo/service/model.py", line 94, in wrapper
    return f(dbname, *args, **kwargs)
  File "/usr/lib/python3.7/site-packages/odoo/http.py", line 339, in checked_call
    result = self.endpoint(*a, **kw)
  File "/usr/lib/python3.7/site-packages/odoo/http.py", line 915, in __call__
    return self.method(*args, **kw)
  File "/usr/lib/python3.7/site-packages/odoo/http.py", line 515, in response_wrap
    response = f(*args, **kw)
TypeError: edit_custom() missing 1 required positional argument: 'custom_id'