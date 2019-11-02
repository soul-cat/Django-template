from django.utils.deprecation import MiddlewareMixin
from django.http import HttpRequest
from django.shortcuts import redirect
import re


class MD(MiddlewareMixin):

    def process_request(self, request: HttpRequest):
        path = []
        path.append('/Novel/create_code')
        path.append('/Novel/go_login')
        path.append('/Novel/goo_login')
        path.append('/Novel/login')
        path.append('/Novel/go_register')
        path.append('/Novel/register')
        path.append('^$')
        re.findall(r'','/Novel/create_code')
        if request.path in path:
            print('1111111111111111')

            pass
        else:
            try:
                if request.session['login_state']:
                    pass
                else:
                    return redirect('/Novel/go_login')
            except:
                return redirect('/Novel/go_login')
