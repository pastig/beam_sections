import os
import matplotlib
matplotlib.use('agg')  # To avoid Matplotlib GUI backend warnings
import matplotlib.pyplot as plt
from django.conf import settings
from django.urls import reverse
from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template, Context

def home(request):
    return render(request, 'home.html')

def generate_report(request):
    if request.method == 'POST':
        height = request.POST.get('height')
        width = request.POST.get('width')

        # Create and save the bar chart
        height_values = float(height)
        width_values = float(width)
        plt.bar(['Height', 'Width'], [height_values, width_values])
        plt.xlabel('Dimensions')
        plt.ylabel('Values')
        plt.title('Height and Width')

        # Get the URL for the report template
        report_template_url = request.build_absolute_uri(reverse('report_template'))

        # Get the absolute path for the chart image
        chart_image_path = os.path.join(settings.STATICFILES_DIRS[0], 'report_generator', 'figures', 'bar_chart.png')
        plt.savefig(chart_image_path)
        plt.close()

        # Read the markdown template and render it with the provided context
        template_path = 'report_generator/templates/report_template.md'
        with open(template_path, 'r') as file:
            template_content = file.read()
        template = Template(template_content)
        context = Context({
            'height': height,
            'width': width,
            'chart_image_url': chart_image_path,
            'report_template_url': report_template_url,
        })
        rendered_template = template.render(context)

        # Save the rendered template to a temporary file
        temp_md_file = 'temp_report.md'
        with open(temp_md_file, 'w') as file:
            file.write(rendered_template)

        # Convert the markdown to PDF using Pandoc
        os.system(f'pandoc {temp_md_file} -o temp_report.pdf')

        # Return the PDF file to the user for download
        with open('temp_report.pdf', 'rb') as file:
            response = HttpResponse(file.read(), content_type='application/pdf')
            response['Content-Disposition'] = 'attachment; filename="report.pdf"'
            return response

    return render(request, 'home.html')

def report_template(request):
    template_path = 'report_generator/templates/report_template.md'
    with open(template_path, 'r') as file:
        template_content = file.read()

    return HttpResponse(template_content, content_type='text/plain')
