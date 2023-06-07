from django.shortcuts import render

# Create your views here.
def example_view(request):
    # my_app/templates/MY_APP/EXAMPLE.HTML
    return render(request, 'my_app/example.html')


def variable_view(request):

    my_var = {
        'first_name':'Jonny',
        'last_name':'Brownrigg',
        'some_list':['list item 1','list item 2','list item 3'],
        'some_dict':{'inside_key':'inside_value'},
    }

    return render(
        request,
        'my_app/variable.html',
        context=my_var,
        )