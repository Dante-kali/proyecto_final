"""
URL configuration for whinter_official project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from django.http import HttpResponse

def welcome(request):
    return HttpResponse('''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Welcome to Whinter Official</title>
    <!-- Bootstrap CSS -->
    <link href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css" rel="stylesheet">
    <style>
        body {
            font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
            background-color: #f4f4f4;
            padding: 40px;
            margin: 0;
        }
        .container {
            max-width: 600px;
            margin: 0 auto;
        }
        .title {
            color: #333;
            font-weight: bold;
            font-size: 32px;
            margin-bottom: 20px;
            text-align: center;
        }
        .subtitle {
            color: #666;
            font-size: 24px;
            margin-top: 40px;
            margin-bottom: 20px;
            text-align: center;
        }
        .available-path {
            color: #007bff;
            text-decoration: none;
            border: 1px solid #007bff;
            padding: 10px 20px;
            border-radius: 20px;
        }
        .available-path:hover {
            text-decoration: none;
            background-color: #007bff;
            color: #fff;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1 class="title">Welcome to Whinter Official</h1>
        <h2 class="subtitle">Explore Whinter</h2>
        <p>Available Path: <a href="/whinter" class="list-group-item list-group-item-action btn btn-success btn-block btn-path">whinter</a>
    </div>
    <!-- Bootstrap JS (Optional) -->
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js"></script>
</body>
</html>

'''
        
        )
urlpatterns = [
    path('admin/', admin.site.urls),
    path("", welcome),
    path('whinter/', include('whinter.urls')),
]