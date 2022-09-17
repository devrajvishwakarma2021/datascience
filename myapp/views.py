
from django.shortcuts import render
from .models import Product, Purchase
import pandas as pd
from .utils import get_simple_plot
from .forms import PurchaseForm

# Create your views here.


def chart_select_view(request):

    graph = None
    error_message = None
    df = None
    price = None

    try: 

        product_df = pd.DataFrame(Product.objects.all().values())
        purchase_df = pd.DataFrame(Purchase.objects.all().values())
        product_df['product_id'] = product_df['id']
    
   

        if purchase_df.shape[0] > 0:
            df = pd.merge(purchase_df, product_df, on='product_id').drop(['id_y', 'date_y'], axis=1).rename({'id_x': 'id', 'date_x': 'date'}, axis=1)
            price = df['price']
            if request.method == 'POST':
                chart_type = request.POST.get('sales')
                date_from = request.POST['date_from']
                date_to = request.POST['date_to']
                print(chart_type)
                df['date'] = df['date'].apply(lambda x: x.strftime('%Y-%m-%d'))
                df2 = df.groupby('date', as_index=False)['total_price'].agg('sum')

                if chart_type != "":
                    if date_from != "" and date_to != "":
                        df = df[(df['date']>date_from) & (df['date']< date_to)]
                        df2 = df.groupby('date', as_index=False)['total_price'].agg('sum')
                    graph = get_simple_plot(chart_type, x=df2['date'], y=df2['total_price'], data=df)
                else:
                    error_message = 'Please select a chart type to continue'

        else:
            error_message = 'No records in the database'
    except:
         
         product_df =None
         purchase_df = None
         error_message ='No records in the database'
    
    
    context = {
        'graph' : graph,
        'price': price,
        'error_message': error_message,
    }
    return render(request, 'myapp/main.html', context)

def add_purchase_view(request):
    form = PurchaseForm(request.POST or None)
    added_message =None

    if form.is_valid():
         obj = form.save(commit=False)
         obj.salesman = request.user
         obj.save()
         
         form = PurchaseForm()
         added_message ="the purchase has been added"
         
    context = {
        'form' : form,
        'added_message ': added_message,
    }
    return render(request, 'myapp/add.html',context)
























# from django.shortcuts import render
# from .models import Product, purchase
# import pandas as pd
# from  .utils import get_simple_plot

# def chart_select_view(request):
#        graph =None
#        error_message = None
#        df = None
#        price = None
       
#        product_df = pd.DataFrame(Product.objects.all().values())
#        purchase_df = pd.DataFrame(purchase.objects.all().values())
#        product_df['product_id'] = product_df['id']

#                                                                                                                #   print(purchase_df.shape)
#        if purchase_df.shape[0] > 0:
#               df = pd.merge(purchase_df, product_df, on='product_id').drop( ['id_y', 'date_y'], axis=1).rename({'id_x': 'id', 'date_x': 'date'}, axis=1)
#               price = df['price']
#                                                                                                            #      print(df['date'][0])
#                                                                                                          #      print(type(df['date'][0]))                                                                                                                                  #       print(type(df['date'][0]))
# #  data sending view
#               if request.method == 'POST':                                                                    # print(request.POST)
#                      chart_type = request.POST.get('sales')
#                      date_from = request.POST['date_from']
#                      date_to = request.POST['date_to']
#                      print(chart_type)
#                      df['date'] = df['date'].apply(lambda x:  x.strftime('%Y-%m-%d'))
#                                                                                                                 # print(df['date'])
#                      df2 = df.groupby('date', as_index=False)['total_price'].agg('sum')

#                                                                                                               # print(df2)
#                      if chart_type != "":
#                             if date_from !="" and date_to !="":

#                                    df =df[(df['date']>date_from) & (df['date']<date_to)]
#                                    df2 = df.groupby('date', as_index=False)['total_price'].agg('sum')  

#                                    #function to get a graph
#                             graph=get_simple_plot(chart_type, x=df2['date'], y=df2['total_price'], data=df)
                            

#                      else:
#                             error_message ="please select a chart type to continue"  
#                                                                                                             # print(chart_type)
#                                                                                                             # print(date_form, date_to)
#        else:
#               error_message = "no records in the database"




#        context = {
#             'graph' : graph,     
#             'price' : price,
#             'error_message': error_message,
#        #  'products': product_df.to_html(),
#        #  'purchase': purchase_df.to_html(),
#        #  'df': df,
#         #     'df' : df.to_html(),
#        }
#        return render(request, "myapp/main.html", context)

#     # queryset data
#     # qs1 = Product.objects.all().values_list()
#     # qs2 = Product.objects.all().values_list()
#     # print(qs1)
#     # print("------------")
#     # print(qs2)

#     # enumerate data
#     # Product_df = pd.DataFrame(Product.objects.all().values())
#     # print(Product_df)

#     # return render(request, "myapp/main.html", {})
