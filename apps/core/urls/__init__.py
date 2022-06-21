"""uRLs para core
"""
# Django Library
from django.conf.urls import include
from django.urls import path

urlpatterns = [
    # ============================ New URLs ============================ #
    path('', include('apps.core.urls.usercustom')),
    path('attribute/', include('apps.core.urls.attribute')),
    path('core/', include('apps.core.urls.core')),
    path('bi/', include('apps.core.urls.bi')),
    path('channel/', include('apps.core.urls.channel')),
    path('comment/', include('apps.core.urls.comment')),
    path('company/', include('apps.core.urls.company')),
    path('country/', include('apps.core.urls.country')),
    path('cron/', include('apps.core.urls.cron')),
    path('currency/', include('apps.core.urls.currency')),
    path('faq/', include('apps.core.urls.faq')),
    path('image/', include('apps.core.urls.image')),
    path('log/', include('apps.core.urls.log')),
    path('meta/', include('apps.core.urls.meta')),
    path('page/', include('apps.core.urls.page')),
    path('parameter/', include('apps.core.urls.parameter')),
    path('partner/', include('apps.core.urls.partner')),
    path('plugin/', include('apps.core.urls.plugin')),
    path('post/', include('apps.core.urls.post')),
    path('product/', include('apps.core.urls.product')),
    path('product_brand/', include('apps.core.urls.product_brand')),
    path('product_category/', include('apps.core.urls.product_category')),
    path('product_category_uom/', include('apps.core.urls.product_category_uom')),
    path('product-webcategory/', include('apps.core.urls.product_webcategory')),
    path('sequence/', include('apps.core.urls.sequence')),
    path('shop/', include('apps.core.urls.shop')),
    path('tag/', include('apps.core.urls.tag')),
    path('tax/', include('apps.core.urls.tax')),
    path('uom/', include('apps.core.urls.uom')),
    path('variant/', include('apps.core.urls.variant')),
    path('wparameter/', include('apps.core.urls.wparameter')),
    path('wpayment/', include('apps.core.urls.wpayment')),
    path('email/', include('apps.core.urls.email')),
    path('file/', include('apps.core.urls.file')),
    path('message/', include('apps.core.urls.message')),
    path('note/', include('apps.core.urls.note')),
    path('event/', include('apps.core.urls.event')),
    path('menu/', include('apps.core.urls.menu')),
    path('api/', include('apps.core.urls.rest')),
]
