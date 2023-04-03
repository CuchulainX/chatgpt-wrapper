Model: GPT-4

> How can I place a custom html footer into a page that will be inherited by all Django pages
> 
> 1 / 1

To place a custom HTML footer in a Django project that will be inherited by all pages, you should use Django's template inheritance feature. Here's a step-by-step guide to create a base template with a custom footer, which will be inherited by other templates:

1.  Create a base template:

In your Django app's `templates` folder, create a new file called `base.html` if you haven't already. This file will act as the base template for your entire project.

html

```html
<!-- templates/base.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{% block title %}My Site{% endblock %}</title>
    {% block extra_css %}{% endblock %}
</head>
<body>
    <div class="content">
        {% block content %}{% endblock %}
    </div>

    <footer>
        <!-- Add your custom footer HTML here -->
        <p>Custom Footer &copy; {{ year }}</p>
    </footer>

    {% block extra_js %}{% endblock %}
</body>
</html>
```

In this example, we've created a base template with several `{% block %}` tags. These blocks can be overridden in the child templates. The custom footer is placed inside the `<footer>` tag.

2.  Inherit the base template in other templates:

Now, for every template where you want the custom footer to be displayed, you need to extend the base template. For example, in your `index.html` file:

html

```html
<!-- templates/index.html -->
{% extends "base.html" %}

{% block title %}Home{% endblock %}

{% block content %}
    <h1>Welcome to My Site!</h1>
    <p>This is the homepage.</p>
{% endblock %}
```

By using the `{% extends "base.html" %}` tag, you're telling Django to use the `base.html` template and override the specified blocks.

3.  Pass the current year to the template context:

In order to display the current year in the footer, you need to pass the year to the template context. In your `views.py` file:

python

```python
from django.shortcuts import render
from datetime import datetime

def index(request):
    context = {
        'year': datetime.now().year
    }
    return render(request, 'index.html', context)
```

4.  Make sure your templates are properly configured:

Ensure that Django knows where to find your templates by checking the `TEMPLATES` setting in your project's `settings.py` file.

python

```python
TEMPLATES = [
    {
        ...
        'APP_DIRS': True,
        ...
    },
]
```

With these steps, you should now have a custom HTML footer that is inherited by all pages that extend the `base.html` template.

1 / 1