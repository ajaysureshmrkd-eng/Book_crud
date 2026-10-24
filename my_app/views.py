from django.shortcuts import render

from django.views.generic import View

from my_app.models import Book

from django.http import JsonResponse

from json import loads

from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator


# Create your views here.

@method_decorator(csrf_exempt,name="dispatch")
class BookCreateListView(View):

    def get(self,request):

        qs =Book.objects.all().values()

        book_lst =list(qs)

        return JsonResponse (book_lst,safe=False)

    def post(sefl,request):

        form_data=loads(request.body)

        Book.objects.create(
            title="The Alchemist",
            author="Paulo Coelho",
            price=399,
            page =600,
            publication="HarperCollins"
        )

        return JsonResponse({"message":"created"})


@method_decorator(csrf_exempt,name="dispatch")
class BookRetrieveUpdateDeleteView(View):

    def get(self,request,pk=None):

        qs =Book.objects.filter(id=pk).values()

        book_lst =list(qs)

        return JsonResponse(book_lst,safe=False)

    def delete(self,request,pk=None):

        Book.objects.get(id=pk).delete()

        return JsonResponse({"message":"deleted..."})

        
