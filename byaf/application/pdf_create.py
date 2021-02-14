import os
from django import forms


class DelDir(forms.Form):
    name = forms.CharField(label="name")


def del_dir():
    print("log")
    # console.log("ok")
