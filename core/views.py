from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from services.models import Service
# 1. ADICIONEI 'CarouselImage' NA IMPORTAÇÃO ABAIXO
from .models import Certification, HomeVideo, OperatingBase, Noticia, CanalContato, CarouselImage, CompanySettings


def home(request):
    # --- LÓGICA DE EXIBIÇÃO ---
    
    # 1. Carrossel de Imagens (Topo) - NOVO
    carousel_images = CarouselImage.objects.filter(is_active=True)

    # 2. Notícias (Meio - Pegar as 4 últimas)
    noticias = Noticia.objects.all()[:4] 

    # 3. Vídeo Hero (Fim)
    video = HomeVideo.objects.filter(is_active=True).first()
    
    # 4. Outros elementos (Serviços e Certificações)
    services = Service.objects.filter(is_active=True)[:6]
    certifications = Certification.objects.all()
    
    return render(request, 'home.html', {
        'carousel_images': carousel_images, # <--- Enviando para o template
        'noticias': noticias,
        'video': video,
        'services': services, 
        'certifications': certifications,
    })

def service_detail(request, slug):
    # Busca o serviço pelo slug ou retorna erro 404 se não achar
    service = get_object_or_404(Service, slug=slug, is_active=True)
    
    return render(request, 'service_detail.html', {
        'service': service
    })

def about(request):
    bases = OperatingBase.objects.all()
    certifications = Certification.objects.all()
    
    # 2. Busque as configurações (Singleton - pega o primeiro registro)
    settings = CompanySettings.objects.first()
    
    return render(request, 'about.html', {
        'bases': bases,
        'certifications': certifications,
        'settings': settings, # <--- ENVIE PARA O TEMPLATE
    })

def noticia_detail(request, slug):
    noticia = get_object_or_404(Noticia, slug=slug)
    return render(request, 'noticia_detail.html', {'noticia': noticia})

def todas_noticias(request):
    # Busca todas as notícias ordenadas da mais recente para a antiga
    noticias = Noticia.objects.all()
    return render(request, 'todas_noticias.html', {'noticias': noticias})

def contato(request):
    # Lógica de Exibição (Apenas busca os canais para mostrar)
    canais = CanalContato.objects.all()
    
    return render(request, 'contact.html', {
        'canais': canais
    })

def privacidade(request):
    return render(request, 'privacidade.html')