from django.shortcuts import render

def runoob(request):
     views_list = ["a", "b", "c", "d", "e"]
     return render(request, "runoob.html", {"listvar": views_list})