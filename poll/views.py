from django.shortcuts import render,redirect

from .forms import *
from .models import *

def home(request):
	my_votes = Poll.objects.all()
	context = {'my_votes':my_votes}
	return render(request,"home.html",context)

def give_poll(request,pk):
	my_vote = Poll.objects.get(id=pk)
	form = PollForm(instance=my_vote)

	if request.method == "POST":
		data = request.POST.get('vote')

		if data == "option1":
			data = int(str(my_vote.count1))
			my_vote.count1 = my_vote.count1 + 1
			my_vote.save()
		elif data == "option2":
			data = int(str(my_vote.count2))
			my_vote.count2 = my_vote.count2 + 1
			my_vote.save()
		else:
			data = int(str(my_vote.count3))
			my_vote.count3 = my_vote.count3 + 1
			my_vote.save()			
		return redirect("/")

	context = {'my_vote':my_vote,'form':form}

	return render(request,"give_poll.html",context)

def poll_results(request,pk):
	my_vote = Poll.objects.get(id=pk)
	context = {'my_vote':my_vote}
	return render(request,"poll_results.html",context)
