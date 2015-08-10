#!/usr/bin/env python
import webapp2
import re
from Forms.Welcome import Welcome

class SignInForm():
    uri = "signin"
    userStr = "username"
    passStr = "password"
    verStr = "verify"
    emailStr = "email"
    badUserStr = "badUser"
    badEmailStr = "badEmail"
    badPassStr = "badPass"
    badPassMatchStr = "badPassMatch"
    form = "<form method=\"post\" action=\"/" + uri + "\">" \
        + userStr + "<input type=\"text\" name=\""+ userStr +"\" value=\"{username}\">" \
        + "<text>{badUser}</text></br>" \
        + passStr +"<input type=\"text\" name=\""+ passStr +"\" value=\"{password}\">" \
        + "<text>{badPass}</text></br>" \
        + verStr + "<input type=\"text\" name=\""+verStr+"\" value=\"{verify}\">" \
        + "<text>{badPassMatch}</text></br>" \
        + emailStr + "<input type=\"text\" name=\""+emailStr+"\" value=\"{email}\">"  \
        + "<text>{badEmail}</text></br>" \
        + "<input type=\"submit\"/>" \
    + "</form>"
    emptyDic = {
        userStr:"",
        passStr:"",
        verStr:"",
        emailStr:"",
        badUserStr:"",
        badEmailStr:"",
        badPassStr:"",
        badPassMatchStr:""
    }
    currDic = {}

    def get(self, d=None):
        if d == None:
            return self.form.format(**self.emptyDic)
        else:
            return self.form.format(**d)

    def post(self, request=None):
#        self.setItems(request)
#        if self.validUsername(self.currDic[self.userStr]) and \
#            self.validPassword(self.currDic[self.passStr]) and \
#            self.passwordMatch(
#                self.currDic[self.passStr],
#                self.currDic[self.verStr]) and \
#            self.validEmail(self.currDic[self.emailStr]):
#         return Welcome(self.currDic[self.userStr]).get()
         return Welcome("fread").get()
#        return self.get(self.currDic)

    def setItems(self, request):
        self.currDic[self.userStr] = request.get("username")
        self.currDic[self.passStr] = request.get("password")
        self.currDic[self.emailStr] = request.get("email")
        self.currDic[self.verStr] = request.get("verify")

    def validUsername(self,username):
        isValid = False
        USER_RE = re.compile(r"^[a-zA-Z0-9_-]{3,20}$")
        if USER_RE.match(username):
            self.currDic[self.badUserStr] = ""
            isValid = True
        else:
            self.currDic[self.badUserStr] = "Bad user name"
        return isValid

    def validPassword(self,password):
        isValid = False
        PASS_RE = re.compile(r"^.{3,20}$")
        if PASS_RE.match(password):
            self.currDic[self.badPassStr] = ""
            isValid = True
        else:
            self.currDic[self.badPassStr] = "Bad pass"
        return isValid

    def passwordMatch(self,password,verifyPass):
        isValid = False
        if password == verifyPass:
            self.currDic[self.badPassMatchStr] = ""
            isValid = True
        else:
            self.currDic[self.badPassMatchStr] = "Bad pass match"
        return isValid

    def validEmail(self,email):
        isValid = False
        EMAIL_RE = re.compile(r"^[\S]+@[\S]+\.[\S]+$")
        if EMAIL_RE.match(email):
            self.currDic[self.badEmailStr] = ""
            isValid = True
        else:
            self.currDic[self.badEmailStr] = "Bad email"
        return isValid

if __name__ == "__main__":
#    print(SignInForm().get())
#    print(SignInForm().post())
    if SignInForm().validUsername("as"):
        print('true')
    else:
        print('false')
    SignInForm().post

