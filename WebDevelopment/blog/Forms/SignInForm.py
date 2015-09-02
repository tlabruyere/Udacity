#!/usr/bin/env python
import webapp2
import re

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
        + "<font color=\"red\">{badUser}</font></br>" \
        + passStr +"<input type=\"password\" name=\""+ passStr +"\" value=\"{password}\">" \
        + "<font color=\"red\">{badPass}</font></br>" \
        + verStr + "<input type=\"password\" name=\""+verStr+"\" value=\"{verify}\">" \
        + "<font color=\"red\">{badPassMatch}</font></br>" \
        + emailStr + "<input type=\"email\" name=\""+emailStr+"\" value=\"{email}\">"  \
        + "<font color=\"red\">{badEmail}</font></br>" \
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
    _success = False

    def get(self, d=None):
        if d == None:
            return self.form.format(**self.emptyDic)
        else:
            return self.form.format(**d)

    def post(self, request=None):
        self.setItems(request)
        _success = False
        success = True
        success = self.validUsername(self.currDic[self.userStr]) and success
        success = self.validPassword(self.currDic[self.passStr]) and success
        success = self.passwordMatch(
                        self.currDic[self.passStr],
                        self.currDic[self.verStr]) and success
        success = self.validEmail(self.currDic[self.emailStr]) and success
        if success:
            self._success = True
        return self.get(self.currDic)

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
        elif username == '':
            self.currDic[self.badUserStr] = ""
        else:
            self.currDic[self.badUserStr] = "Bad user name"
        return isValid

    def validPassword(self,password):
        isValid = False
        PASS_RE = re.compile(r"^.{3,20}$")
        if PASS_RE.match(password):
            self.currDic[self.badPassStr] = ""
            isValid = True
        elif password == '':
            self.currDic[self.badPassStr] = ""
        else:
            self.currDic[self.badPassStr] = "Bad password"
        return isValid

    def passwordMatch(self,password,verifyPass):
        isValid = False
        if password == verifyPass:
            self.currDic[self.badPassMatchStr] = ""
            isValid = True
        else:
            self.currDic[self.badPassMatchStr] = "password does not match"
        return isValid

    def validEmail(self,email):
        isValid = False
        EMAIL_RE = re.compile(r"^[\S]+@[\S]+\.[\S]+$")
        if EMAIL_RE.match(email):
            self.currDic[self.badEmailStr] = ""
            isValid = True
        elif email == '':
            self.currDic[self.badEmailStr] = "Please entar a password"
        else:
            self.currDic[self.badEmailStr] = "Bad email"
        return isValid

    def postSuccussful(self):
        return self._success

if __name__ == "__main__":
#    print(SignInForm().get())
#    print(SignInForm().post())
    if SignInForm().validUsername("as"):
        print('true')
    else:
        print('false')
    print(SignInForm().post())

