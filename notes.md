# **Tabel of Contents**
- [**Tabel of Contents**](#tabel-of-contents)
- [**Common Commands \& Code Snippets:**](#common-commands--code-snippets)
- [**Key Django Features**](#key-django-features)
    - [**Additional features not shown in MTV structure above:**](#additional-features-not-shown-in-mtv-structure-above)
    - [**Django Drawbacks:**](#django-drawbacks)
- [**Django Project vs Django App:**](#django-project-vs-django-app)
- [**Views, Routing and URLs:**](#views-routing-and-urls)
    - [Simple Case](#simple-case)
- [**Templates:**](#templates)
- [**Passing variables into an html template / filters:**](#passing-variables-into-an-html-template--filters)
- [**Django Tags:**](#django-tags)
  - [**'for loops' tags:**](#for-loops-tags)


<br><br>

# **Common Commands & Code Snippets:**

Find code snippets [here](https://docs.google.com/spreadsheets/d/1Y5z9UxCh-aFkXUYMTqtE2UQR3YHjotAPrqOAKdQTkc0/edit#gid=1802607629)


<br><br>

# **Key Django Features**

- Model-Template-View (MTV) Structure
    - ORM - Object-relational Mapper
    - Models
    - URLs and Views
    - Templates
 
<br>

The basic MTV structure is as follows, with python picking up the serverside (back-end) section of the workflow.

<img src="screenshots/mtv_structure.png" width="600">

<br>

Where using python comes into its own is by applying python logic that works in tandem with the mtv structure to bring additional features. E.g. machine learning algos working with the models etc.

<img src="screenshots/python_logic_in_mtv.png" width="600">

<br>

### **Additional features not shown in MTV structure above:**
  * Authentication
  * Administration

<br>

### **Django Drawbacks:**

  * Django is heavily reliant on idea of a Model; i.e.  a representation of a table in a database. This makes it easy to query data but does mean that you need to understand Models and setting them up for views.

<br><br>

# **Django Project vs Django App:**

  * Django is set up to take advantage of reusable 'apps' within their projects. This means that you can associate all of the required code, models etc. with the specific app that needs it an create a more organised project overall.


<br><br>

# **Views, Routing and URLs:**

### Simple Case
* Creating a simple view in a django app and connecting it to the main site takes three steps:

1. **Create a view within the target app:**
```
from django.http import HttpResponse

def simple_view(request):
    return HttpResponse('This is a simple view!')
```
<br>

2. **Add the path within the urls file of the app:**
```
from django.urls import path
from . import views

urlpatterns = [
    path('', views.simple_view)
]
```
<br>

3. **Connects the main site's urls file to the apps urls file:**
```
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('first_app/', include('first_app.urls')),
]
```

<br><br>

# **Templates:**

To connect a django app to a project - so that you can create a seperate templates section - you would follow the following steps:

1. Setup the Django App
   1. Create App Directory with `manage.py startapp <name_of_app>` comand
   2. Creaqte the relevant URLs and Views
   3. Mapp the app's URLs to the project
   
2. Run the migrate command
   * `python mange.py migrate`
   * Ths command looks inside the INSTALLED_APPS the settings and creates any necessary db tables
   
3. Inside of Django App check the apps.py file created automatically for you and register the AppConfig class to the ISTALLED_APPS inside of settings.py
   
4. Register the app and any db changes with Django by running:
   * `python manage.py makemigrations myapp`
   * Note, this is relevant only when models have been created.
   
5. Run `python manage.py migrate` again to create the model tables in our database.
   * Again, only relevant when we have created models.
   
6. Create a template directory inside your app directory with theis structure:
   * my_side
     * my_app
       * templates
         * my_app
           * example.html
   *  The second my_app folder is to ensure django doesn't choose a template with the same name that is actually associated with another app.

<br><br>

# **Passing variables into an html template / filters:**

   * When creating a view that renders to an html template, context can be parsed (rendered) to the template by adding in the 'context' argument. E.g. The following renderes the the my_var dict to the variable.html template.

```
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
```
<br>

   * To use the values parsed to the template. You can use the {{}} notation. In addition, filters can be applied to perform certain 'python inspired' operations on the variables. E.g.

```
<h1>VARIABLE.HTML</h1>
    <h2>Hello {{first_name}} {{last_name}}</h2>
    <h2>I have used an upper filter to print this name: {{first_name | upper}} {{last_name | upper}}</h2>
    <h2>And a length filter to print this name: {{first_name | length}} {{last_name | length}}</h2>
    <ol>
        <li>{{some_list.0}}</li>
        <li>{{some_list.1}}</li>
        <li>{{some_list.2}}</li>
    </ol>
```
<br>

   * To find more filters & tags - you can search for built in filters and tags in the django documentation. These can become quite complex, for instance grabbing the time that the user accesses something, date formatting or formatting an extract from a db to be consistent (e.g. upper).

<br><br>

# **Django Tags:**

   * Django tags are able to provide further logic at the template in th erendering process
     * This includes a lot of functionality, such as for loops, if-else statements and linking to URLs.

<br>

## **'for loops' tags:**

