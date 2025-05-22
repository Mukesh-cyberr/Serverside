
# Ex.05 Design a Website for Server Side Processing
## Date: 22/05/2025

## AIM:
 To design a website to calculate the power of a lamp filament in an incandescent bulb in the server side. 


## FORMULA:
P = I<sup>2</sup>R
<br> P --> Power (in watts)
<br> I --> Intensity
<br> R --> Resistance

## DESIGN STEPS:

### Step 1:
Clone the repository from GitHub.

### Step 2:
Create Django Admin project.

### Step 3:
Create a New App under the Django Admin project.

### Step 4:
Create python programs for views and urls to perform server side processing.

### Step 5:
Create a HTML file to implement form based input and output.

### Step 6:
Publish the website in the given URL.

## PROGRAM :
```
math.html

{% load static %}
<html>
<head>
    <title>math</title>
    <style>
        body {
            margin: 0;
            height: 100vh;
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            background: linear-gradient(to bottom right, #e6ccff, #a64dff); /* Violet gradient */
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        }

        h1 {
            background-color: #b366ff; /* Mild violet */
            padding: 20px 40px;
            border-radius: 10px;
            font-size: x-large;
            font-weight: bolder;
            font-variant: small-caps;
            color: white;
            margin-bottom: 20px;
        }

        form {
            background-color: #8000ff; /* Darker violet */
            padding: 30px;
            border-radius: 15px;
            color: white;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.3);
        }

        .power {
            margin-bottom: 15px;
        }

        label {
            display: inline-block;
            width: 120px;
            font-weight: bold;
        }

        input[type="text"] {
            padding: 6px;
            width: 200px;
            border: none;
            border-radius: 4px;
        }

        .button-container {
            text-align: center;
            margin-top: 10px;
        }

        input[type="submit"] {
            background-color: #d580ff; /* Soft violet button */
            color: black;
            padding: 10px 25px;
            font-weight: bold;
            border: none;
            border-radius: 6px;
            cursor: pointer;
        }

        input[readonly] {
            background-color: #f3e6ff;
        }
    </style>
</head>
<body>
    <h1>POWER OF A BULB</h1>
    <form method="POST">
        {% csrf_token %}
        <div class="power">
          <label>INTENSITY:</label>
          <input type="text" name="intensity" value="{{ i }}">
          <span>(amperes)</span>
      </div>
      <div class="power">
          <label>RESISTANCE:</label>
          <input type="text" name="resistance" value="{{ r }}">
          <span>(ohms)</span>
      </div>
      <div class="power">
          <label>POWER:</label>
          <input type="text" name="POWER" value="{{ power }}" readonly>
          <span>(watts)</span>
      </div>
      <div class="button-container">
        <input type="submit" value="CALCULATE">
    </div>
      
    </form>
</body>
</html>


views.py

from django.shortcuts import render 
def powerofabulb(request): 
    context={} 
    context['power'] = "0" 
    context['i'] = "0" 
    context['r'] = "0" 
    if request.method == 'POST': 
        print("POST method is used")
        i = request.POST.get('intensity','0')
        r = request.POST.get('resistance','0')
        print('request=',request) 
        print('intensity=',i) 
        print('resistance=',r) 
        power = (int(i)**2)*int(r) 
        context['power'] = power 
        context['i'] = i
        context['r'] = r 
        print('power=',power) 
    return render(request,'mathapp/math.html',context)


urls.py

from django.contrib import admin 
from django.urls import path 
from mathapp import views 
urlpatterns = [ 
    path('admin/', admin.site.urls), 
    path('powerofabulb/',views.powerofabulb,name="powerofabulb"),
    path('',views.powerofabulb,name="powerofabulbroot")
]
```

## SERVER SIDE PROCESSING:
![Screenshot 2025-05-21 142830](https://github.com/user-attachments/assets/2d918335-cc26-41fc-9d2a-c134509627ab)


## HOMEPAGE:

![Screenshot 2025-05-21 142803](https://github.com/user-attachments/assets/67e0100b-3bc3-441e-bb7c-540b299a5b01)


## RESULT:
The program for performing server side processing is completed successfully.
