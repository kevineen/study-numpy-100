from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .models import PDFPack
from .application import pdf_create
import subprocess
import logging

from byaf.forms import DataForm
from django.views.generic.edit import FormView

# from logging import getLogger, StreamHandler, DEBUG

# logger = getLogger(__name__)
# handler = StreamHandler()
# handler.setLevel(DEBUG)
# logger.setLevel(DEBUG)
# logger.addHandler(handler)
# logger.propagate = False

import os

print(os.getcwd())

print("プリント")
logging.debug("まえ")


class DataView(FormView):
    template_name = "byaf/index.html"
    form_class = DataForm
    success_url = ""
    logging.debug("あほ")

    def post(self, request, *args, **kwargs):
        form = self.get_form(self.form_class)
        if form.is_valid():
            if request.is_ajax():
                """Ajax 処理を別メソッドに切り離す"""
                print("### Ajax request")
                return self.ajax_response(form)
            # Ajax 以外のPOSTメソッドの処理
            return super().form_valid(form)
        # フォームデータが正しくない場合の処理
        return super().form_invalid(form)

    def ajax_response(self, form):
        """jQuery に対してレスポンスを返すメソッド"""
        name = form.cleaned_data.get("name")
        return HttpResponse(f"こんにちは、{name}さん！")

    def form_valid(self, form):
        form.get_dir()
        return super().form_valid(form)

    def test_ajax_response(request):
        input_text = request.POST.getlist("name_input_text")
        hoge = "Ajax Response: " + input_text[0]

        return HttpResponse(hoge)


def te(request):
    template_name = "byaf/index.html"
    print("lkfjda;")

    form = DataForm
    return render(request, template_name, {"form": form})


# def index(request):

#     logger.debug("hello")

#     template_name = "byaf/index.html"

#     param = {
#         "app": "byaf",
#     }

#     if request.method == "POST" and "pdf_crate" in request.POST:
#         pdf_create.del_dir()

#     return render(request, template_name, param)


def file_upload_view(request):
    print(request.FILES)
    if request.method == "POST":
        my_file = request.FILES.get("file")
        PDFPack.objects.create(upload=my_file)
        return HttpResponse("")
    return JsonResponse({"post: false"})


def del_dir(request):
    template_name = "byaf/index.html"

    process = subprocess.run(
        ["python", "applications/pdf_create.py", "del_dir"], stdout=subprocess.PIPE,
    )

    output = process.stdout

    param = {
        "output": output,
    }

    if request.method == "GET":
        print("実行")
        return render(request, template_name, param)
