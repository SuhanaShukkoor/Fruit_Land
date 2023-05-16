from django.contrib.syndication.views import Feed
from django.db.models.base import Model
from django.template.defaultfilters import truncatewords
from django.utils.safestring import SafeText
from product.models import fruits
from django.urls import reverse
from django.shortcuts import redirect

class latest(Feed):
    title="Fruit Land"
    link="/drcomments/"
    description="Fruit Land is a site for purchase fresh fruits"

    def items(self):
        return fruits.objects.all()[:5]
    def item_title(self,data):
        return data.name
    def item_description(self,data):
        return truncatewords(data.desc,3)
    def item_link(self,data):
        return reverse("homepage")
    