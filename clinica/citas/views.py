from django.shortcuts import render, redirect, get_object_or_404
from .models import Cita
from .forms import CitaForm
from django.http import HttpResponse
from reportlab.pdfgen import canvas

def listar_citas(request):
    citas = Cita.objects.all()
    return render(request, 'citas/listar.html', {'citas': citas})

def agregar_cita(request):
    form = CitaForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('listar')
    return render(request, 'citas/formulario.html', {'form': form})

def editar_cita(request, id):
    cita = get_object_or_404(Cita, id=id)
    form = CitaForm(request.POST or None, instance=cita)
    if form.is_valid():
        form.save()
        return redirect('listar')
    return render(request, 'citas/formulario.html', {'form': form})

def eliminar_cita(request, id):
    cita = get_object_or_404(Cita, id=id)
    if request.method == 'POST':
        cita.delete()
        return redirect('listar')
    return render(request, 'citas/eliminar.html', {'cita': cita})

def generar_pdf(request):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="citas.pdf"'

    p = canvas.Canvas(response)
    p.drawString(100, 800, "Reporte de Citas Médicas")

    y = 760
    for cita in Cita.objects.all():
        p.drawString(100, y, f"{cita.paciente} - {cita.doctor} - {cita.fecha}")
        y -= 20

    p.showPage()
    p.save()
    return response
