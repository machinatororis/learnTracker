from django.shortcuts import render


def index(reguest):
    """Домашня сторінка застосунку learnTracker"""
    return render(reguest, "learn_trackers/index.html")
