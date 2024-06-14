import io
from django.shortcuts import redirect, render, HttpResponse
from .models import MinutasCasei
from django.views.generic.list import ListView
from .forms import FormMinutaCasei
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Image, Paragraph, Spacer, KeepTogether
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from django.templatetags.static import static
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter, landscape
from reportlab.pdfgen import canvas

# CRUD MINUTAS

# CONSULTA DE MINUTAS
class ConsultaMinutas(ListView):
    model = MinutasCasei
    template_name = 'lista_minutas.html'

# AGERGAR MINUTA
def agregar_minuta(request):
    if(request.method == 'POST'):
        formM = FormMinutaCasei(request.POST, request.FILES)
        if(formM.is_valid()):
            formM.save()
            return redirect('consulta_minutas')
    else:
        formM = FormMinutaCasei()
    return render(request,'agregar_minuta.html',{'form':formM})

# ElIMINAR MINUTA
def eliminar_minuta(request,id):
    MinutasCasei.objects.get(id=id).delete()

    return redirect('consulta_minutas')

# EDITAR MINUTA
def editar_minuta(request,id):
    minuta = MinutasCasei.objects.get(id=id)

    if(request.method == 'POST'):
        formEM = FormMinutaCasei(request.POST, request.FILES, instance=minuta)
        if(formEM.is_valid()):
            formEM.save()
            return redirect('consulta_minutas')
    else:
        formEM = FormMinutaCasei(instance=minuta)

    return render(request,'editar_minuta.html',{'form':formEM})

# GENERAR PDF DE LA MINUTA
def generar_pdf_minuta(request, id):
    minuta = MinutasCasei.objects.get(id=id)

    filename = f"{minuta.titulominuta}.pdf"
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'inline; filename="{filename}"'

    buffer = io.BytesIO()
    p = canvas.Canvas(buffer, pagesize=letter)

    title_font = "Helvetica-Bold"
    title_size = 20
    subtitle_font = "Helvetica-Bold"
    subtitle_size = 14
    content_font = "Helvetica"
    content_size = 12

    x = 100
    y = 750
    line_height = 20

    # Título
    p.setFont(title_font, title_size)
    p.drawString(x, y, f"Título: {minuta.titulominuta}")

    # Fecha
    y -= line_height
    p.setFont(subtitle_font, subtitle_size)
    p.drawString(x, y, f"Fecha: {minuta.fechaminuta}")

    # Minuta
    y -= line_height * 2
    p.setFont(subtitle_font, subtitle_size)
    p.drawString(x, y, "Minuta:")
    y -= line_height
    p.setFont(content_font, content_size)
    for line in minuta.minuta.splitlines():
        p.drawString(x, y, line)
        y -= line_height
        if y < 40: 
            p.showPage()
            y = 750
            p.setFont(content_font, content_size)

    # Acuerdos
    y -= line_height
    p.setFont(subtitle_font, subtitle_size)
    p.drawString(x, y, "Acuerdos:")
    y -= line_height
    p.setFont(content_font, content_size)
    for line in minuta.acuerdos.splitlines():
        p.drawString(x, y, line)
        y -= line_height
        if y < 40:
            p.showPage()
            y = 750
            p.setFont(content_font, content_size)

    p.showPage()
    p.save()

    pdf = buffer.getvalue()
    buffer.close()

    response.write(pdf)
    
    return response

