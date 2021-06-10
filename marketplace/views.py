from django.shortcuts import get_object_or_404, render, redirect, HttpResponseRedirect

from marketplace.forms import MarketplaceForm

from marketplace.models import Marketplace


def marketplace_list(request):
    marketplace_list = Marketplace.objects.all()
    context = {
        "marketplace_list": marketplace_list,
    }

    return render(request, "marketplace/marketplace_list.html", context=context)


def marketplace_create(request):
    marketplace_form = MarketplaceForm(request.POST or None)

    if marketplace_form.is_valid():
        marketplace_form.save()
        return redirect("marketplace_list")

    context = {
        "marketplace_form": marketplace_form,
    }

    return render(request, "marketplace/marketplace_form.html", context=context)


def marketplace_update(request, id):

    marketplace_obj = get_object_or_404(Marketplace, id=id)
    marketplace_form = MarketplaceForm(request.POST or None, instance=marketplace_obj)

    if marketplace_form.is_valid():
        marketplace_form.save()

        return redirect("marketplace_list")

    context = {
        "marketplace_form": marketplace_form,
    }

    return render(request, "marketplace/marketplace_form.html", context=context)


def marketplace_delete(request, id):
    context = {}

    obj = get_object_or_404(Marketplace, id=id)

    if request.method == "GET":
        obj.delete()

        return redirect("marketplace_list")

    return render(request, "marketplace/marketplace_list.html", context=context)


def marketplace_detail(request, id):
    marketplace_obj = get_object_or_404(Marketplace, id=id)
    marketplace_form = MarketplaceForm(request.POST or None, instance=marketplace_obj)

    context = {
        "marketplace_form": marketplace_form,
    }

    return render(request, "marketplace/marketplace_form.html", context=context)
