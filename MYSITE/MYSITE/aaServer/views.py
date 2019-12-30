from django.shortcuts import render

def index(request):
    context = {}
    template = 'main/index.html'
    return render(request, template, context)






def about(request):
    context = {'title': "About"}
    template = 'main/about.html'
    return render(request, template, context)


from .forms import ContactForm
def contact(request):
    form = ContactForm(request.POST or None)
    if request.POST:
        print(request.POST)
    context = {'title': "Contact Us", "form": form}
    template = 'main/form.html'
    return render(request, template, context)
