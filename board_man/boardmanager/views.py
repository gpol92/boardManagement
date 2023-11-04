from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views import View
from django.views.generic.edit import FormView, CreateView, UpdateView, DeleteView
from django.views.generic import TemplateView
from django.urls import reverse_lazy, reverse
from .models import Board
from .forms import BoardForm

# Create your views here.

class HomepageView(TemplateView):
    template_name = 'homepage.html'

class RegisterBoardView(CreateView):
    model = Board
    template_name = 'register.html'
    form_class = BoardForm
    success_url = reverse_lazy('homepage')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
    
class ShowBoardsView(TemplateView):
    template_name = 'show.html'
    def get_context_data(self, **kwargs):
        boards = Board.objects.all()
        context = super().get_context_data(**kwargs)
        context['boards'] = boards
        return context

class ChangeStatusView(View):
    def get(self, request, pk):
        board = get_object_or_404(Board, pk=pk)
        if board.status == Board.OPEN:
            board.status = Board.CLOSED
        else:
            board.status = Board.OPEN
        board.save()
        return HttpResponseRedirect(reverse('show'))

class ClearDefectView(View):
    def get(self, request, pk):
        board = get_object_or_404(Board, pk=pk)
        if board.defects != '-':
            board.defects = '-'
        board.save()
        return HttpResponseRedirect(reverse('show'))

class UpdateDefectView(UpdateView):
    def post(self, request, pk):
        board = get_object_or_404(Board, pk=pk)
        defects = request.POST.get('defects', '')
        board.defects = defects
        board.save()
        return HttpResponseRedirect(reverse('show'))

class DeleteBoardView(DeleteView):
    model = Board
    template_name = 'show.html'
    success_url = reverse_lazy('show')

    def get(self, request, pk):
        board = get_object_or_404(Board, pk=pk)
        board.delete()
        return HttpResponseRedirect(reverse('show'))
    

    