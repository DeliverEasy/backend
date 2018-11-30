from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):

    lote = models.OneToManyField(Lote)


    name = models.CharField(max_length=40, null=False)
    TYPES_CHOICES = (
        ("F", "Food"),
        ("HA", "Home Appliances")
        ("D", "Drinks")
        ("FU", "Furniture")
        ("C", "Clothing")

    )


    type = models.CharField(
        max_length=40,
        choices=TYPES_CHOICES,

    )


    description = models.TextField(max_length=300)



class xxx(models.Model):

    user = models.OneToManyField(User, null=False)
    product = models.ForeignKey(Product, null=False)
    quantity = models.IntegerField(null=False)
    price = models.DecimalField(null=False)
    description = models.TextField(blank=True, max_length=250)

class Sale(models.Model):


    fecha = models.DateField(auto_now_add=True)
    descripion = models.CharField(max_length=300, blank=True, verbose_name='Detalle del pedido')
    total = models.DecimalField(decimal_places=2, max_digits=7, verbose_name='Total de la venta')



    def __str__(self):
        return '{}'.format(self.id)


class DetailSales(models.Model):


        Product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Producto')
        cantidad = models.IntegerField(verbose_name='Cantidad')
        sales = models.ForeignKey(Sale, on_delete=models.CASCADE, verbose_name='Sale')


    def __str__(self):
        return '{} - {}'.format(self.sale, self.producto)


class CreateSales(CreateView):


        Model = DetailSales
        template_name = 'sale/sale_form.html'
        form_class = DetailForm
        second_form_class = SalesForm
        success_url = reverse_lazy('sale:sales_listar')


class UpdateSales(object):
    pass


    def get_context_data(self, **kwargs):
        context = super(UpdateSales, self).get_context_data(**kwargs)
        pk = self.kwargs.get('pk', 0)
        detalle = self.model.objects.get(id=pk)
        venta = self.second_model.objects.get(id=detalle.venta_id)
        if 'form' not in context:
            context['form'] = self.form_class()
        if 'form2' not in context:
            context['form2'] = self.second_form_class(instance=venta)
        context['id'] = pk
        return context


    def post(self, request, *args, **kwargs):
        self.object = self.get_object
        id_detale = kwargs['pk']
        detalle = self.model.objects.get(id=id_detale)
        venta = self.second_model.objects.get(id=detalle.venta_id)
        form = self.form_class(request.POST, instance=detalle)
        form2 = self.second_form_class(request.POST, instance=venta)
        if form.is_valid() and form2.is_valid():
            form.save()
            form2.save()
            return HttpResponseRedirect(self.get_success_url())
        else:
            return HttpResponseRedirect(self.get_success_url())

class Lote(models.Model):

        valor = models.IntegerField
        cantidad = models.IntegerField
        peso = models.IntegerField
        tipo = models.TextField(max_length=100)
        id = models.ForeignKey()


    def __unicode__(self):
        return self.name








