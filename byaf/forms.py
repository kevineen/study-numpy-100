from django import forms


class DataForm(forms.Form):
    name = forms.CharField(label="name")
    dabe = forms.CharField(label="1111")

    print("ok")

    def get_dir(self):
        print("ok")
