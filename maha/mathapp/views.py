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
