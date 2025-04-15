import requests
from django.shortcuts import render, redirect
from django.conf import settings
from django.http import JsonResponse
from .models import Website  # Assuming a Website model exists
import cohere
from django.shortcuts import get_object_or_404, redirect

# View to generate a website layout using DeepAI
def generate_view(request):
    if not request.session.get('access_token'):
        return redirect('users/login')

    if request.method == 'POST':
        business_type = request.POST.get('business_type')
        industry = request.POST.get('industry')

        # 👇 Hardcoded API key instead of settings.COHERE_API_KEY
        co = cohere.Client("mGtDlroIVjKJiLgH2YmsSGVLcyjdq0viIVUWK9la")

        prompt = f"Generate a website layout for a {business_type} business in the {industry} industry."

        response = co.generate(
            model='command',
            prompt=prompt,
            max_tokens=500
        )

        generated_text = response.generations[0].text if response.generations else "No output"

        website_data = {
            'title': f"{business_type} Website",
            'content': generated_text,
            'layout': {"layout": generated_text}
        }

        create_response = requests.post(
            'http://localhost:8000/websites/api/websites/',
            headers={'Authorization': f'Bearer {request.session["access_token"]}'},
            json=website_data
        )

        print("Create Website API:", create_response.status_code, create_response.text)

        if create_response.status_code == 201:
            return redirect('websites:manage')

    return render(request, 'websites/generate.html')

# View to manage websites
def manage_view(request):
    if not request.session.get('access_token'):
        return redirect('users/login')

    response = requests.get(
        'http://localhost:8000/websites/api/websites/',
        headers={'Authorization': f'Bearer {request.session["access_token"]}'}
    )

    print("Status Code:", response.status_code)
    print("Response Text:", response.text)

    try:
        websites = response.json() if response.status_code == 200 else []
    except Exception as e:
        print("JSON error:", e)
        websites = []

    return render(request, 'websites/manage.html', {'websites': websites})

# API view to create and list websites
def website_api_view(request):
    if request.method == 'POST':
        title = request.data.get('title')
        content = request.data.get('content')

        # Assuming a Website model exists
        website = Website.objects.create(title=title, content=content)

        return JsonResponse({'message': 'Website created successfully!', 'id': website.id}, status=201)

    elif request.method == 'GET':
        websites = Website.objects.all()
        websites_data = [{'title': website.title, 'content': website.content} for website in websites]
        return JsonResponse(websites_data, safe=False)
    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)


def delete_view(request, website_id):
    # Ensure the user is logged in
    if not request.session.get('access_token'):
        return redirect('users/login')

    # Get the website object by ID
    website = get_object_or_404(Website, id=website_id)

    # Delete the website
    website.delete()

    # Redirect to the manage view after deletion
    return redirect('websites:manage')  # You can change this if needed


from .forms import WebsiteForm  

def edit_view(request, website_id):
    # Ensure the user is logged in
    if not request.session.get('access_token'):
        return redirect('users/login')

    # Get the website object by ID
    website = get_object_or_404(Website, id=website_id)

    if request.method == 'POST':
        # Update the website data if the form is submitted
        form = WebsiteForm(request.POST, instance=website)

        if form.is_valid():
            form.save()  # Save the updated website data
            return redirect('websites:manage')  # Redirect to manage view after saving
    else:
        # Display the existing website data in the form
        form = WebsiteForm(instance=website)

    return render(request, 'websites/edit.html', {'form': form, 'website': website})
def edit_view(request, website_id):
    # Ensure the user is logged in
    if not request.session.get('access_token'):
        return redirect('users/login')

    # Get the website object by ID
    website = get_object_or_404(Website, id=website_id)

    if request.method == 'POST':
        # Update the website data if the form is submitted
        form = WebsiteForm(request.POST, instance=website)

        if form.is_valid():
            form.save()  # Save the updated website data
            return redirect('websites:manage')  # Redirect to manage view after saving
    else:
        # Display the existing website data in the form
        form = WebsiteForm(instance=website)

    return render(request, 'websites/edit.html', {'form': form, 'website': website})


def preview_view(request, pk):
    if not request.session.get('access_token'):
        return redirect('users:login')

    response = requests.get(
        f'http://localhost:8000/websites/api/websites/{pk}/',
        headers={'Authorization': f'Bearer {request.session["access_token"]}'}
    )

    if response.status_code == 200:
        website = response.json()
    else:
        website = {'title': 'Not Found', 'content': 'Website not found or unauthorized'}

    return render(request, 'websites/preview.html', {'website': website})
