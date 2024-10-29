from django.shortcuts import render
from django.dispatch import Signal
from django.dispatch import receiver, Signal




#  QUESTION 1 : By default are django signals executed synchronously or asynchronously ?
#  ANSWER : The execution is synchronous because this print statement is executed after the signal is sent. When we send a signal, the execution does not move forward until the receiver completes its execution. ( The example code snippet is given below )

#  Make a Custom Signal
homePageLoadedSignal = Signal()

# Receiver
@receiver(homePageLoadedSignal)
def requestRecieverFunction(sender, **kwargs):
    print(f"{kwargs['data']['page']} page loaded, signal executed successfully")

# Sender
def synchronousFunction(request):
    # Signal Calling
    homePageLoadedSignal.send(sender=synchronousFunction, data={'page':'Home'})
    # After Signal
    print('This is Synchronous Function')
    return render(request,'question1.html')












# QUESTION 2 : Do django signals run in the same thread as the caller? 
# ANSWER : Yes , Django runs in a single thread in which the caller runs because the execution does not go to the sender until the receiver is completely executed, so Django is synchronous and runs in a single thread in which either the caller or the sender runs. ( The example code snippet is given below )

# Make a Custom Signal
coffeeSignal = Signal()

# Receiver
@receiver(coffeeSignal)
def makeCoffeeReceiver(sender, **kwargs):
    print('Your Coffee is ready')


#  Sender
def makeCoffeeSender(request):

    coffeeSignal.send(sender=makeCoffeeSender, data={'page':'Make Coffee'})
    print('I need a Coffee')
    return render(request,'question2.html')






# QUESTION 3 : Do django signals run in the same thread as the caller?
# ANSWER : Yes, by default, Django signals run in the same database transaction as the caller, If there are changes in the execution of the sender or the caller, there will be changes in the execution of the receiver as well. Signal executes in the same thread in which the caller executes so if sender's transaction fails , the database operation performed by the receiver will also failed. ( The example code snippet is given below ) 

from django.db import transaction
from databaseApp.models import Fruit
from django.db import transaction

def question3(request):
    try:
        with transaction.atomic():
            # Create a Fruit instance
            fruit = Fruit.objects.create(name="Apple", color="Red")
            # Log that fruit creation signal has run
            print("Fruit Instance created")

            # raising error to interrupt the execution
            raise Exception("Raising Exception to interrupt the execution")

    except Exception as e:
        print("Exception occurred:", e)

    # After the rollback, check if any Fruit instance exists
    print("Total Fruit count :", Fruit.objects.count()) 
    
    return  render(request,'question3.html')




