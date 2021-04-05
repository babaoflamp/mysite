import io
from django.shortcuts import render
from django.http import FileResponse
from reportlab.pdfgen import canvas

# Create your views here.
def some_view(request):
    buffer = io.BytesIO()
    p = canvas.Canvas(buffer)
    p.drawString(100,100,"Hello world.")
    p.showPage()
    p.save()
    buffer.seek(0)
    return FileResponse(buffer,
     as_attachment=True, filename='hello.pdf')