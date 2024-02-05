from django.shortcuts import render,redirect,get_object_or_404,HttpResponse
from .models import Travel,Book,Order
from django.shortcuts import render
from django.db.models import Q
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from datetime import date
from .forms import DateSelectorForm
import random
import razorpay


# Create your views here.
def index(request):
    username = request.user.username
    allplaces=Travel.objects.all()
    context={"allplaces":allplaces,"username":username}  
 
    return render(request,"index.html",context)

# def increase_quantity(request):
#     quantity = request.session.get('quantity', 0)
#     quantity += 1
#     request.session['quantity'] = quantity
#     return redirect('rajhasthan')

# def decrease_quantity(request):
#     quantity = request.session.get('quantity', 0)
#     if quantity > 0:
#         quantity -= 1
#         request.session['quantity'] = quantity
#     return redirect('rajhasthan') 

def contact(request):
    
    return render(request,"contact.html")

def explore(req):
    username = req.user.username
    context={"username":username} 
    return render(req,"explore.html",context)
     
def rajhasthan(request):
    
    return render(request,"rajhasthan.html")
   
     
def kerala(request):
    
    return render(request, 'kerala.html')


def himachal(request):
    
    return render(request, 'Himachal.html')

def goa(request):
    
    return render(request,"goa.html")

def hampi(request):
    
    return render(request,"hampi.html")

def coorg(request):
    
    return render(request,"coorg.html")

def taj(request):
    
    return render(request,"taj.html")

def andaman(request):
    
    return render(request,"andaman.html")

def searchproduct(request):
    query = request.GET.get("q")
    if query:
        allplaces = Travel.objects.filter(Q(place_name__icontains=query))
    else:
        allplaces = Travel.objects.all()
    context = {"allplaces": allplaces, "query": query}
    return render(request, "index.html", context)

def userlogin(req):
    if req.method == "POST":
        uname = req.POST["uname"]
        upass = req.POST["upass"]
        context = {}
        if uname == "" and upass == "":
            context["errmsg"] = "Field can't be empty"
            return render(req, "login.html", context)
        else:
            u = authenticate(username=uname, password=upass)
            if u is not None:
                login(req, u) 
                return redirect("/")
            else:
                context["errmsg"] = "Invalid username and password"
                return render(req, "login.html", context)
    else:
        return render(req,"login.html")
    

def register(req):
    if req.method == "POST":
        uname = req.POST["uname"]
        upass = req.POST["upass"]
        ucpass = req.POST["ucpass"]
        context = {}
        if uname == "" or upass == "" or ucpass == "":
            context["errmsg"] = "Field can't be empty"
            return render(req, "register.html", context)
        elif ucpass != upass:
            context["errmsg"] = "Password and confirm password doesn't match"
            return render(req, "register.html", context)
        else:
            try:
                u = User.objects.create(username=uname, password=upass)
                u.set_password(upass)
                u.save()
                return redirect("/userlogin")
            except Exception:
                context["errmsg"] = "User already exists"
                return render(req, "register.html", context)
    else:
        return render(req, "register.html")

def add_to_book(request, t_id):
    if request.user.is_authenticated:
        user = request.user
    else:
        user = None 
    allplaces = get_object_or_404(Travel,t_id=t_id)
    # dates = datetime.now().date()
    book_item, created = Book.objects.get_or_create(t_id=allplaces,userid=user)
    if not created:
        book_item.no_people += 1
    else:
        book_item.no_people = 1
    book_item.save()
    

    # Associate the date with the booking
   
  

  
   

    return redirect("/book")

def book(req):
    if req.user.is_authenticated:
        username = req.user.username
        allplaces = Book.objects.filter(userid=req.user.id)
        total_price = 0
       
        # allplaces=Book.objects.filter(t_id=dates)
        for x in allplaces:
            total_price += x.t_id.price * x.no_people 
           
            # dates=x.t_id=x.dates
        length = len(allplaces)
        context = {
            "book_item": allplaces,
            "total": total_price,
            "item": length,
            "username":username
           
        }
        return render(req, "book.html", context)
    else:
        allplaces = Book.objects.filter(userid=req.user.id)
        total_price = 0
       
       
        for x in allplaces:
            total_price += x.t_id.price * x.no_people
          
            
        length = len(allplaces)
        context = {
            "book_item": allplaces,
            "total": total_price,
            
            'item_count': len(allplaces),
           
        }
    return render(req, "book.html", context)

def remove_from_book(request, t_id):
    if request.user.is_authenticated:
        user = request.user
    else:
        user = None
    book_item = Book.objects.filter(t_id=t_id, userid=user)
    book_item.delete()
    return redirect("/book")
    

# def book(req):
#     if req.user.is_authenticated:
#         username = req.user.username
#         allplaces = Book.objects.filter(userid=req.user.id)
#         total_price = 0
#         dates = []

#         for x in allplaces:
#             if x.t_id and x.t_id.price:
#                 total_price += x.t_id.price * x.no_people
#                 dates.extend(x.dates.all())

#         length = len(allplaces)
#         context = { 
#             "book_item": allplaces,
#             "total": total_price,
#             "item": length,
#             "dates": dates,
#             "username": username
#         }
#     else:
#         allplaces = Book.objects.filter(userid=req.user.id)
#         total_price = 0
#         dates = []

#         for x in allplaces:
#             if x.t_id and x.t_id.price:
#                 total_price += x.t_id.price * x.no_people
#                 dates.append(x.dates)

#         length = len(allplaces)
#         context = {
#             "book_item": allplaces,
#             "total": total_price,
#             "item": length,
#             "dates": dates,
#         }

#     return render(req, "book.html", context)

 

def updatepeople(request, qv, t_id):
    allbook = Book.objects.filter(t_id=t_id)

    if qv == "1":
        total = allbook[0].no_people + 1
        allbook.update(no_people=total)
    else:
        if allbook[0].no_people > 1:
            total = allbook[0].no_people - 1
            allbook.update(no_people=total)
        else:
            allbook = Book.objects.filter(t_id=t_id)
            allbook.delete()

    return redirect("/book")


    

   

def userlogout(req):
    logout(req)
    return redirect("/")




def orders(request):
    if request.user.is_authenticated:
        user=request.user
    else:
        user=None
    allbook = Book.objects.filter(userid=user)
    total_price = 0 
  
    for x in allbook:
        total_price += x.t_id.price * x.no_people 
    context={}
    context['book_item']= allbook
    context['total']=total_price
    context['item'] =len(allbook)
    context['username']=user
  
    return render(request,'orders.html',context)

   

def dateselect(request):
    if request.method == 'POST':
        form = DateSelectorForm(request.POST)
        if form.is_valid():
            selected_date = form.cleaned_data['date']
 
            context={'selected_date':selected_date}

    else:
        form = DateSelectorForm()
        context={'form':form}
    return render(request,'dateselect.html',context)


def makepayment(request):
    if request.user.is_authenticated:
        user=request.user
        order_id=random.randrange(1000,9999)
        allbook = Book.objects.filter(userid=user)
        for x in allbook:
            o=Order.objects.create(order_id=order_id,t_id=x.t_id,userid=x.userid,no_people=x.no_people)
            o.save()
            x.delete()
        orders=Order.objects.filter(userid=user)
        total_price = 0
        for x in orders:
            total_price += x.t_id.price * x.no_people
            oid=x.order_id
        client = razorpay.Client(auth=("rzp_test_DTDZYV0quyrBBB", "a4TQ7ba6bcCy9ZXIxP1Fh3CG"))
        data = { "amount": total_price*100, "currency": "INR", "receipt": str(oid) }
        payment = client.order.create(data=data)
     
        context={}
        context['data']=payment
        context['amount']=payment
        return render(request,'payment.html',context)
    else:
        user=None
        return redirect('/userlogin')





def showorders(req):
    if req.user.is_authenticated:
        user=req.user
        allorders = Order.objects.filter(userid=user)
        context = {"allorders": allorders, "username": user}
        return render(req, "showorders.html", context)
    else:
        user=None
        return redirect('/userlogin')