from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group
from django.contrib.auth.models import Permission
from mainapp.models import Project, User


PROJECTS = [
    ('Macropad para Teclado', 'pioneer1', 'moderntimesmelon shares how to make a custom macro pad for keyboard shortcuts, this specific one is for Zoom video conferencing shortcuts for Windows. The keys functions are: toggle mute/unmute microphone, raise/lower hand, and video on/off. #Instructables #electronics #technology #computer #macropad '),
    ('Reciclar plástico en filamento 3D', 'pioneer2', 'nezonezo shares how you can recycle plastic into 3D printer filament at home. #Instructables #technology #electronics #3Dprinting #recycle'),
    ('Weatherbot', 'pioneer2', 'DIY Machines\'s WeatherBot is a 3D printed, motorized weather machine that uses ESP32 & OpenWeatherMap. #Instructables #electronics #technology #gadget #3Dprint'),
    ('Monitor de CO2 miniaturizado', 'pioneer2', 'tomatoskins covers how I followed the #engineering process to develop a 3D printed puzzle. #Instructables #3Dprint #puzzle #toy'),
    ('Air umbrella', 'pioneer1', 'This unique umbrella, which is designed to keep rain off of you by creating a shield of air, was made with 3D printed parts designed using Tinkercad. #Instructables #3Dprint #Tinkercad #invention #electronics' ),
    ('RFID Tap n\' Go Ring', 'pioneer2', 'Transfer the RFID chip from your credit card into a resin ring to make it quick and easy to pay at any establishment that accepts RFID credit cards without needing to take out your wallet. #Instructables #electronics #technology #wearable #creditcard #payment #contactless #epoxy #resin #3Dprint #moldmaking #casting'),
    ('Washing Machine Notifications', 'pioneer1', 'Set up a device that featured Google Home integration, random nagging notifications, Android notifications, cost of wash & total time of wash, and a neat graph. #Instructables #electronics #technology #Android #GoogleHome #laundry #household'),
    ('The Anywhere Outlet', 'pioneer2', 'The Anywhere Outlet: One wall of our living room is the virtual nerve center of our small apartment. I would venture that 80% of our electronics are either permanently located along this wall or are charged there. Power is supplied by two outlets in the wall'),
    
]

class Command(BaseCommand):
    def handle(self, *args, **options):
        for p in PROJECTS:
            u = User.objects.filter(username=p[1]).get()
            up = Project(name=p[0], pioneer=u, description=p[2])
            up.save()