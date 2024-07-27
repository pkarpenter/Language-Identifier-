from django.http import HttpResponse
from django.shortcuts import render


def Welcome(request):
 return render(request, "index.html")


def user(request):
   username = request.GET['username']
   print(username)
   return render(request, "user.html", {'name': username})



def predictor(request):
 return render(request, 'main.html')

import joblib

model = joblib.load('D:\\django\\lan\\savemodels\\language.pkl') # your model path
# cv = CountVectorizer()
cv = joblib.load('D:\\django\\lan\\savemodels\\count_vectorizer.joblib')

def result(request):
    if 'data' in request.POST:
        data = request.POST['data']
        print(data)
        
        try:
            pred_data = cv.transform([data])
            y_pred = model.predict(pred_data)
            print(y_pred)
            return render(request, 'result.html', {'result': y_pred})
            
        
        except Exception as e:
            # Handle any errors occurred during model loading or prediction
            print("Error", e)
            return render(request, 'user.html', {'message': str(e)})
    else:
        print("error")
        # Handle case when 'Language' parameter is not present in the request
        return render(request, 'user.html', {'message': 'Language parameter is missing'})
    



# def Home(request):
#  return render(request, "home.html")

def about(request):
    return render(request, "about.html")

def Contect(request):
 return render(request, "contact.html")

def Services(request):
 return render(request, "services.html")