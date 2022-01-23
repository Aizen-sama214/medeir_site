from multiprocessing import context
from tkinter import image_names
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.conf import settings

from .models import Import
from .models import Slice
import nibabel as nib
import numpy as np
from PIL import Image

from .forms import ImportForm
# Create your views here.

def index(request):
    images_list = Import.objects.all()
    image_urls = [img.image.url for img in images_list]
    # print(image_urls[0], "bbbbbbbbbbbb")
    # print(settings.MEDIA_ROOT, "aaaaaaaaaaaaaaaaaaa")
    # print("/".join(images_list[0].image.url.split("/")[2::]),'eeeeeeeee')

    media_root = settings.MEDIA_ROOT
    
    slices_list = Slice.objects.all()
    slices_list.delete()

    for cor_images in images_list:
        im_url = "/".join(cor_images.image.url.split("/")[2::])
        im = nib.load(media_root + im_url)
        num_img = np.array(im.dataobj)
        im_jpg = Image.fromarray(np.multiply(num_img[75],255))
        im_jpg = im_jpg.convert('L')


        img_path = media_root + im_url.replace("corrupted","slices").replace(".nii.gz",".jpeg")
        im_jpg.save(img_path)
        slice_path = "images/slices/" + im_url.split("/")[-1].replace(".nii.gz",".jpeg")
        new_slice = Slice(img_name = cor_images.img_name,image = slice_path)
        new_slice.save()

    slices_list = Slice.objects.all()


    #context = {'images_list':images_list,'slices_list':slices_list,'length':range(len(slices_list))}
    context = {'list':zip(images_list,slices_list)} 
    return render(request,"polls/index.html",context)

def entry(request):
    if request.method == "POST":
        form = ImportForm(request.POST,request.FILES)

        if form.is_valid:
            form.save()
        
        return redirect("polls:entry")

    form = ImportForm()
    context = {'image_form':form }
    return render(request, "polls/entry.html", context)