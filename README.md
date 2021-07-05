# mi-fruit-python-django
This App is made with Django Python, This help to predict the fruit with the features.

This app is developed with Python Django Framework. 

As the part in embedded with Machine learing - Classification has been used to predict the fruit.

```python
    f = Feautres
    l = Labels

    c = tree.DecisionTreeClassifier()

    c = c.fit(f,l)
    o = cld()
    a = int(request.POST.get("color"))
    b = int(request.POST.get("taste"))
    t = int(request.POST.get("surface"))

    d =c.predict([[a,b,t]])
    print(d)

```
Kindly refer the views.py file inside the ml folder for more detials.

click on the link to redirect to the page for demo.

#[https://sabarish.xyz/ml-fruit/](https:// "# https://sabarish.xyz/ml-fruit/")

