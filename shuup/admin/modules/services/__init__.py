# -*- coding: utf-8 -*-
# This file is part of Shuup.
#
# Copyright (c) 2012-2017, Shoop Commerce Ltd. All rights reserved.
#
# This source code is licensed under the OSL-3.0 license found in the
# LICENSE file in the root directory of this source tree.

from __future__ import unicode_literals

from django.utils.translation import ugettext_lazy as _

from shuup.admin.base import AdminModule, MenuEntry
from shuup.admin.menu import SETTINGS_MENU_CATEGORY
from shuup.admin.utils.permissions import get_default_model_permissions
from shuup.admin.utils.urls import (
    admin_url, derive_model_url, get_edit_and_list_urls
)
from shuup.core.models import PaymentMethod, ShippingMethod


class ServiceModule(AdminModule):
    category = _("Payment and Shipping")
    model = None
    name = None
    url_prefix = None
    view_template = None
    name_template = None
    menu_entry_url = None
    menu_ordering = 999999
    url_name_prefix = None

    def get_urls(self):
        permissions = self.get_required_permissions()
        return [
            admin_url(
                "%s/(?P<pk>\d+)/delete/$" % self.url_prefix,
                self.view_template % "Delete",
                name=self.name_template % "delete",
                permissions=permissions
            )
        ] + get_edit_and_list_urls(
            url_prefix=self.url_prefix,
            view_template=self.view_template,
            name_template=self.name_template,
            permissions=permissions
        )

    def get_menu_entries(self, request):
        return [
            MenuEntry(
                text=self.name,
                url=self.menu_entry_url,
                category=SETTINGS_MENU_CATEGORY,
                subcategory="payment_shipping",
                ordering=self.menu_ordering
            )
        ]

    def get_required_permissions(self):
        return get_default_model_permissions(PaymentMethod) | get_default_model_permissions(ShippingMethod)

    def get_model_url(self, object, kind):
        return derive_model_url(self.model, self.url_name_prefix, object, kind)


class ShippingMethodModule(ServiceModule):
    model = ShippingMethod
    name = _("Shipping Methods")
    url_prefix = "^shipping_method"
    view_template = "shuup.admin.modules.services.views.ShippingMethod%sView"
    name_template = "shipping_method.%s"
    menu_entry_url = "shuup_admin:shipping_method.list"
    menu_ordering = 4
    url_name_prefix = "shuup_admin:shipping_method"

    breadcrumbs_menu_entry = MenuEntry(text=name, url="shuup_admin:shipping_method.list")


class PaymentMethodModule(ServiceModule):
    model = PaymentMethod
    name = _("Payment Methods")
    url_prefix = "^payment_method"
    view_template = "shuup.admin.modules.services.views.PaymentMethod%sView"
    name_template = "payment_method.%s"
    menu_entry_url = "shuup_admin:payment_method.list"
    menu_ordering = 5
    url_name_prefix = "shuup_admin:payment_method"

    breadcrumbs_menu_entry = MenuEntry(text=name, url="shuup_admin:payment_method.list")
