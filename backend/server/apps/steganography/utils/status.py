from apps.steganography.models import StatusTracker
from django.core.exceptions import ObjectDoesNotExist
from django.db import connection



def createStatus():
    status = StatusTracker(progress=0)
    status.save()

    return status

def getStatusObject(id):
    try:
        status = StatusTracker.objects.get(_id=id)
        return status
    except(ObjectDoesNotExist):
        return None

def getProgress(id):
    try:
        status = StatusTracker.objects.get(_id=id)
        return status.progress
    except(ObjectDoesNotExist):
        return -1

def setProgress(id, progress):
    try:
        status = StatusTracker.objects.get(_id=id)
        status.progress = progress
        status.save()
    except(ObjectDoesNotExist):
        pass 

def setProgressMultiProcessing(id, progress, lock):
    with lock:
        try:
            status = StatusTracker.objects.get(_id=id)
            if progress > status.progress:
                print(f"Setting Progress to {progress}")
                status.progress = progress
                status.save()
        except(ObjectDoesNotExist):
            pass 


def deleteStatus(id):
    try:
        status = StatusTracker.objects.get(_id=id)
        status.delete()
    except(ObjectDoesNotExist):
        pass

def temp():
    allItems = StatusTracker.objects.all()
    answer = []
    for item in allItems:
        answer.append(item.id)
    
    return answer